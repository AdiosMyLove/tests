import json
import sys
from docx import Document

def parse_docx_to_json(docx_path):
    try:
        doc = Document(docx_path)
        content = "".join(paragraph.text for paragraph in doc.paragraphs)
        return json.loads(content)
    except Exception as error:
        print(f"Ошибка при обработке файла {docx_path}: {error}")
        sys.exit(1)

def populate_values(tests, values_lookup):
    for test in tests:
        test_id = test.get("id")
        if test_id in values_lookup:
            test["value"] = values_lookup[test_id]
        if "values" in test:
            populate_values(test["values"], values_lookup)

def execute():
    if len(sys.argv) != 4:
        print("Использование: python script.py tests.docx values.docx report.json")
        return

    test_file = sys.argv[1]
    value_file = sys.argv[2]
    output_file = sys.argv[3]

    try:
        test_data = parse_docx_to_json(test_file)
        value_data = parse_docx_to_json(value_file)

        value_map = {item["id"]: item["value"] for item in value_data["values"]}

        populate_values(test_data["tests"], value_map)

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(test_data, file, indent=4, ensure_ascii=False)

        print(f"Результат сохранен в {output_file}")

    except Exception as error:
        print(f"Произошла ошибка: {error}")

if __name__ == "__main__":
    execute()
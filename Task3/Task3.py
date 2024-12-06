import json
import sys

def fill_values(tests, values):
    for test in tests:
        if test["id"] in values:
            test["value"] = values[test["id"]]
        if "values" in test:
            fill_values(test["values"], values)

def run(tests_file, values_file, output_file):
    with open(values_file, 'r') as vf:
        values_data = json.load(vf)

    with open(tests_file, 'r') as tf:
        tests_data = json.load(tf)

    values = {item["id"]: item["value"] for item in values_data["values"]}
    fill_values(tests_data["tests"], values)

    with open(output_file, 'w') as of:
        json.dump(tests_data, of, indent=4)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])
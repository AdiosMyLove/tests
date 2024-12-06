import sys

def circular_array_path(n, m):
    # Создаём круговой массив
    array = list(range(1, n + 1))
    path = []
    current_index = 0
    
    while True:
        # Запоминаем начальный элемент текущего интервала
        path.append(array[current_index])
        # Вычисляем индекс конца интервала
        next_index = (current_index + m - 1) % n
        # Если вернулись к первому элементу, останавливаемся
        if next_index == 0:
            break
        # Переходим к следующему интервалу
        current_index = next_index
    
    return ''.join(map(str, path))

if __name__ == "__main__":
    # Считываем аргументы командной строки
    if len(sys.argv) < 3:
        print("Пожалуйста, введите два аргумента: n и m.")
        sys.exit(1)
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    # Вызываем функцию и выводим результат
    result = circular_array_path(n, m)
    print(result)
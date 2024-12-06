import sys

def path(n, m):
    arr = list(range(1, n + 1))
    path = []
    current_index = 0
    
    while True:
        interval = [arr[(current_index + i) % n] for i in range(m)]
        path.append(interval[0])
        current_index = (current_index + m - 1) % n
        if current_index == 0:
            break
    
    return ''.join(map(str, path))

if __name__ == "__main__":
    n, m = int(sys.argv[1]), int(sys.argv[2])
    result = path(n, m)
    print(result)
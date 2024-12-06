import sys
import math

def position_of_point(x0, y0, r, x1, y1):
    distance = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    if distance == r:
        return 0
    elif distance < r:
        return 1
    else:
        return 2

def main():
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    with open(circle_file, 'r') as f:
        x0, y0 = map(float, f.readline().split())
        r = float(f.readline())
    
    with open(points_file, 'r') as f:
        points = [tuple(map(float, line.split())) for line in f.readlines()]
    
    for (x1, y1) in points:
        result = position_of_point(x0, y0, r, x1, y1)
        print(result)

if __name__ == "__main__":
    main()
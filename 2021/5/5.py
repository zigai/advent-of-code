import math
from pprint import pprint


def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


class Point:

    def __init__(self, val: str) -> None:
        val = val.split(",")
        self.x = int(val[0])
        self.y = int(val[1])

    def __repr__(self):
        return f"{self.x},{self.y}"


def parse_data(data: list):
    d = []
    for i in data:
        i = i.split(" -> ")
        d.append([Point(i[0]), Point(i[1])])
    return d


def is_straight_line(p1, p2):
    return p1.x == p2.x or p1.y == p2.y


def make_2d_array(size: int):
    return [[0] * size for _ in range(size)]


def get_points(p1: Point, p2: Point):
    if p1.x == p2.x:
        p_min = min([p1.y, p2.y])
        p_max = max([p1.y, p2.y])
        points = [[p1.x, i] for i in range(p_min, p_max + 1)]
    elif p1.y == p2.y:
        p_min = min([p1.x, p2.x])
        p_max = max([p1.x, p2.x])
        points = [[i, p1.y] for i in range(p_min, p_max + 1)]
    return points


def get_diagonal_points(p1: Point, p2: Point):
    if p1.x > p2.x:
        start_x, start_y, end_x, end_y = p2.x, p2.y, p1.x, p1.y
    else:
        start_x, start_y, end_x, end_y = p1.x, p1.y, p2.x, p2.y

    points = []
    slope = (end_y - start_y) // (end_x - start_x)
    for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
        points.append([i, j])
    points.append([end_x, end_y])
    return points


def part_1(data: list):
    data = parse_data(data)
    array = make_2d_array(1000)
    for line in data:
        p1 = line[0]
        p2 = line[1]
        if not is_straight_line(p1, p2):
            continue
        points = get_points(p1, p2)
        for point in points:
            array[point[1]][point[0]] += 1
    s = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] > 1:
                s += 1
    print(s)


def part_2(data: list):
    data = parse_data(data)
    array = make_2d_array(1000)
    for line in data:
        p1 = line[0]
        p2 = line[1]
        if is_straight_line(p1, p2):
            points = get_points(p1, p2)
        else:
            points = get_diagonal_points(p1, p2)
        for point in points:
            array[point[1]][point[0]] += 1
    s = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] > 1:
                s += 1
    print(s)


if __name__ == "__main__":
    data = read_file("./input")
    #data = read_file("./example")
    part_1(data)
    part_2(data)
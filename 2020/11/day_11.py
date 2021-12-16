from copy import deepcopy


def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
              (1, 1)]


def print_2d_array(array):
    for i in array:
        for j in i:
            print(j, end="")
        print("")


def adjacent_seats(data: list, x: int, y: int):
    array = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y: continue
            if i < 0 or j < 0: continue
            try:
                array.append(data[i][j])
            except IndexError:
                continue
    return array


def one_cycle_part_1(data: list):
    data_copy = deepcopy(data)
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            adjacent = adjacent_seats(data, i, j)
            if seat == EMPTY:
                if adjacent.count(OCCUPIED) == 0:
                    data_copy[i][j] = OCCUPIED
            elif seat == OCCUPIED:
                if adjacent.count(OCCUPIED) >= 4:
                    data_copy[i][j] = EMPTY
    return data_copy


def part_1(data: list):
    while 1:
        data_new = one_cycle_part_1(data)
        if data_new == data:
            break
        data = deepcopy(data_new)
    return sum(i.count(OCCUPIED) for i in data)


def adjacent_part_2(data: list, x: int, y: int):
    array = []
    for direction in directions:
        pos_x = x
        pos_y = y
        while 1:
            pos_x += direction[0]
            pos_y += direction[1]

            if pos_x < 0 or pos_y < 0:
                array.append(".")
                break

            try:
                seat = data[pos_x][pos_y]
            except IndexError:
                array.append(".")
                break

            #print(f"x :{pos_x}y: {pos_y} - {d}")
            if seat == EMPTY or seat == OCCUPIED:
                array.append(seat)
                break
    return array


def one_cycle_part_2(data: list):
    data_copy = deepcopy(data)
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == FLOOR:
                continue
            adjacent = adjacent_part_2(data, i, j)
            if seat == EMPTY:
                if adjacent.count(OCCUPIED) == 0:
                    data_copy[i][j] = OCCUPIED
            elif seat == OCCUPIED:
                if adjacent.count(OCCUPIED) >= 5:
                    data_copy[i][j] = EMPTY
    return data_copy


def part_2(data: list):
    while 1:
        data_new = one_cycle_part_2(data)
        if data_new == data:
            break
        data = deepcopy(data_new)
    return sum(i.count(OCCUPIED) for i in data)


if __name__ == "__main__":
    data = read_file("./input")
    data = [list(i) for i in data]
    print(part_1(data))
    print(part_2(data))
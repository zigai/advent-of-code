def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def part_1(data: list):
    data.append(data[-1] + 3)
    one_j, three_j, = 1, 0
    for i in range(len(data)):
        if data[i] - data[i - 1] == 1:
            one_j += 1
        elif data[i] - data[i - 1] == 3:
            three_j += 1
    return one_j * three_j


def part_2(data: list):
    values = {0: 1}
    for adapter in data:
        a = values.get(adapter - 1, 0)
        b = values.get(adapter - 2, 0)
        c = values.get(adapter - 3, 0)
        print(adapter, "=", a + b + c)
        values[adapter] = a + b + c
    return (list(values.values())[-1])


data = sorted([int(i) for i in read_file("./input")])
print("Part 1:", part_1(data))
print("Part 2:", part_2(data))
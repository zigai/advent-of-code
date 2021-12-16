def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def part_1(data: list):
    data = [int(i) for i in data]
    s = sum([data[i + 1] > data[i] for i in range(0, len(data) - 1)])
    print(s)


def part_2(data: list):
    data = [int(i) for i in data]
    s = sum(
        [data[i] + data[i + 1] + data[i + 2] > data[i - 1] + data[i] + data[i + 1] for i in range(0,
                                                                                                  len(data) - 2)])
    print(s)


if __name__ == "__main__":
    data = read_file("./input")
    #data = read_file("./example")
    part_1(data)
    part_2(data)
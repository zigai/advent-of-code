def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def part_1(data: list):
    h, d = 0, 0
    for i in data:
        cmd = i.split(" ")[0]
        x = int(i.split(" ")[1])
        match cmd:
            case "forward":
                h += x
            case "up":
                d -= x
            case "down":
                d += x
    print(h * d)


def part_2(data: list):
    h, d, aim = 0, 0, 0
    for i in data:
        cmd = i.split(" ")[0]
        x = int(i.split(" ")[1])
        match cmd:
            case "forward":    
                h += x
                d += aim * x
            case "up":
                aim -= x
            case "down":
                aim += x
    print(h * d)


if __name__ == "__main__":
    data = read_file("./input")
    part_1(data)
    part_2(data)
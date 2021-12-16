def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def part_1(data: list):
    gamma = []
    for i in range(12):
        col = [j[i] for j in data]
        ones = col.count("1")
        if ones > len(data) // 2:
            gamma.append("1")
        else:
            gamma.append("0")
    epsilon = [str(int(not int(i))) for i in gamma]
    epsilon = int("".join(epsilon), 2)
    gamma = int("".join(gamma), 2)
    print(gamma * epsilon)


def get_rating(data, var:str):
    for i in range(len(data[0])):
        if len(data) == 1:
            break
        col = [int(j[i]) for j in data]
        avg = sum(col) / len(data)
        match var:
            case "oxygen":
                val = 1 if avg >= 0.5 else 0
            case "co2":
                val = 1 if avg < 0.5 else 0
        data = [j for j in data if j[i] == val]
    oxygen = int("".join([str(i) for i in data[0]]), 2)
    return oxygen

def part_2(data: list):
    data = [[int(j) for j in i] for i in data]
    oxy = get_rating(data, "oxygen")
    co2 = get_rating(data, "co2")
    print(co2 * oxy)


if __name__ == "__main__":
    data = read_file("./input")
    part_1(data)
    part_2(data)
def read_data(name):
    with open(name) as f:
        data = f.readlines()
    n = []
    for password in data:
        n.append(password.strip("\n"))
    return n


def part_1(data):
    r = 0
    for item in data:
        item = item.split(": ")
        req = item[0]
        password = item[1]

        req = req.split(" ")
        letter = req[1]
        bounds = req[0].split("-")
        counter = password.count(letter)

        if counter >= int(bounds[0]) and counter <= int(bounds[1]):
            r += 1
    print(f"Part 1: {r}")


def part_2(data):
    r = 0
    for item in data:
        item = item.split(": ")
        req = item[0]
        password = item[1]
        req = req.split(" ")
        letter = req[1]
        bounds = req[0].split("-")

        occ = 0
        if password[int(bounds[0]) - 1] == letter: occ += 1
        if password[int(bounds[1]) - 1] == letter: occ += 1
        if occ == 1: r += 1
    print(f"Part 2: {r}")


if __name__ == "__main__":
    data = read_data("input.txt")
    part_1(data)
    part_2(data)

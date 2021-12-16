def parse_data(data, part: str):
    d = {}
    for line in data:
        line = line.split(" contain ")
        color = line[0]
        color = color.replace(" bags", "").replace(" bag", "").strip()
        if "no other bags" in line[1]:
            d[color] = []
            continue
        bags_array = []
        k = line[1].split(",")
        for l in k:
            l = l.replace(" bags",
                          "").replace(" bag",
                                      "").strip("\n").strip(".").strip()
            if part == "1": bags_array.append(l[2:])
            elif part == "2": bags_array.append(l)
        d[color] = bags_array
    return d


def reverse_dict(d):
    e = {}
    for key, value in d.items():
        for v in value:
            e.setdefault(v, []).append(key)
    return e


def part_1(data, color):
    r = data[color]
    for p in r:
        if p in data:
            key_data = data[p]
            if key_data:
                for d in key_data:
                    if d not in r:
                        r.append(d)
    print(f"Part 1: {len(r)}")


def part_2(data):
    bag_list = ["shiny gold"]
    counter, i = 0, 0
    level = [1]
    while (len(bag_list)) > i:
        if bag_list[i] in data:
            for bags in data[bag_list[i]]:
                number = int(bags[0])
                color = bags[2:]
                bag_list.append(color)
                level.append(level[i] * number)
                counter += level[i] * number
        i += 1
    print(f"Part 2: {counter}")


if __name__ == "__main__":
    with open("input") as f:
        data = f.readlines()

    data_part_1 = parse_data(data, part="1")
    data_part_2 = parse_data(data, part="2")
    part_1(reverse_dict(data_part_1), "shiny gold")
    part_2(data_part_2)

def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


compass = ["N", "E", "S", "W"]


def part_1(data: list):
    direction = "E"
    postion = {"N": 0, "E": 0, "S": 0, "W": 0}
    for i in data:
        action = i[0]
        value = int(i[1:])
        if action == "F":
            postion[direction] += value
        elif action in compass:
            postion[action] += value
        elif action == "L":
            index = compass.index(direction) - int(value / 90)
            direction = compass[index]
        elif action == "R":
            index = (compass.index(direction) + int(value / 90)) % 4
            direction = compass[index]
    ew = abs(postion["W"] - postion["E"])
    ns = abs(postion["S"] - postion["N"])
    print(ew + ns)


def part_2(data: list):
    ship = [0, 0, 0, 0]
    waypoint = [1, 10, 0, 0]
    for i in data:
        action = i[0]
        value = int(i[1:])
        if action == "F":
            for i, v in enumerate(waypoint):
                ship[i] += v * value
        elif action in compass:
            waypoint[compass.index(action)] += value
        elif action == "L":
            for _ in range(int(value / 90)):
                waypoint.append(waypoint.pop(0))
        elif action == "R":
            for _ in range(int(value / 90)):
                waypoint.insert(0, waypoint.pop())
        # print("Ship:", ship)
        # print("Waypoint:", waypoint)
    ew = abs(ship[1] - ship[3])
    ns = abs(ship[0] - ship[2])
    print(ew + ns)


if __name__ == "__main__":
    data = read_file("./input")
    #data = read_file("./example")
    part_1(data)
    part_2(data)
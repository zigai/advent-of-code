import math
from functools import lru_cache


def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


"""
def part_1(data: list):
    print([int(i) for i in data[1].split(",") if i != "x"][[
        math.ceil(int(data[0]) / b_id) * b_id
        for b_id in [int(i) for i in data[1].split(",") if i != "x"]
    ].index(
        min([
            math.ceil(int(data[0]) / b_id) * b_id
            for b_id in [int(i) for i in data[1].split(",") if i != "x"]
        ]))] * (min([
            math.ceil(int(data[0]) / b_id) * b_id
            for b_id in [int(i) for i in data[1].split(",") if i != "x"]
        ]) - int(data[0])))
"""


def part_1(data: list):
    earliest = int(data[0])
    buses = [int(i) for i in data[1].split(",") if i != "x"]
    bus_times = [math.ceil(earliest / b_id) * b_id for b_id in buses]
    id_ = bus_times.index(min(bus_times))
    print(buses[id_] * (min(bus_times) - earliest))


def check_p2(val: int, offests: tuple, buses: tuple):
    for offset, bus in zip(offests, buses):
        x = (val + offset) % bus
        if x != 0:
            return False
    return True


def part_2(data: list):
    # too slow
    buses = [int(i) for i in data[1].split(",") if i != "x"]
    data = [None if i == 'x' else int(i) for i in data[1].split(",")]
    max_id = max(buses)
    max_id_data_index = data.index(max_id)
    offests = [data.index(bus) - max_id_data_index for bus in buses]
    val = max_id
    while 1:
        if check_p2(val, tuple(offests), tuple(buses)):
            break
        val += max_id
    print(val + offests[0])


if __name__ == "__main__":
    data = read_file("./input")
    #data = read_file("./example")
    #part_1(data)
    part_2(data)
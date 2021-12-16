import math
from pprint import pprint


def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_boards(data: list):
    data = [i for i in data if i != ""]
    data = [i.replace("  ", " ").strip() for i in data]

    boards = []
    for i in range(0, len(data), 5):
        row = data[i:i + 5]
        row = [[int(i) for i in i.split(" ")] for i in row]
        boards.append(row)
    return boards


def get_score(board: list, picked_nums: list):
    unmarked_sum = 0
    for b in board:
        unmarked = [i for i in b if i not in picked_nums]
        unmarked_sum += sum(unmarked)
    return unmarked_sum


def is_bingo(board: list, picked_nums: list):
    for index, row in enumerate(board):
        rows = all([i in picked_nums for i in row])
        cols = all([i[index] in picked_nums for i in board])
        if cols or rows:
            return True
    return False


def part_1(data: str):
    data = data.split("\n")
    random_picks = data[0].split(",")
    random_picks = [int(i) for i in random_picks]
    picked = []
    boards = get_boards(data[1:])
    for i in range(0, len(random_picks)):
        picked.append(random_picks[i])
        for b in boards:
            if is_bingo(b, picked):
                print(get_score(b, picked) * picked[-1])
                return


def part_2(data: list):
    data = data.split("\n")
    random_picks = data[0].split(",")
    random_picks = [int(i) for i in random_picks]
    boards = get_boards(data[1:])
    picked = []
    boards_complete = {}
    scores = []
    for i in range(0, len(random_picks)):
        picked.append(random_picks[i])
        for index, b in enumerate(boards):
            if is_bingo(b, picked):
                if boards_complete.get(index, 0):
                    continue
                boards_complete[index] = True
                score = get_score(b, picked) * picked[-1]
                scores.append(score)
    print(scores[-1])


if __name__ == "__main__":
    data = read_file("./input")
    #data = read_file("./example")
    part_1(data)
    part_2(data)
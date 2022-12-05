import copy

from aoc.api import *


def read_input(filename: str) -> list:
    parts = FileStream(filename, "\n\n").list()
    moves = Stream(parts[1].split("\n"))\
        .map(Stream.split(" ").filter(String.isdigit).map(int)).list()
    containers = list(reversed(parts[0].split("\n")))
    stacks = [[] for _ in range(sum(c.isdigit() for c in containers[0]))]
    for row in containers[1:]:
        idx = 0
        for i in range(1, len(row), 4):
            if row[i] != " ":
                stacks[idx].append(row[i])
            idx += 1
    return [stacks, moves]


def part_1(values: list) -> str:
    stacks: list = copy.deepcopy(values[0])
    for move in values[1]:
        for _ in range(move[0]):
            stacks[move[2] - 1].append(stacks[move[1] - 1].pop())
    return "".join([i.pop() if i else "" for i in stacks])


def part_2(values: list) -> str:
    stacks: list = copy.deepcopy(values[0])
    for move in values[1]:
        new = []
        for _ in range(move[0]):
            new.append(stacks[move[1] - 1].pop())
        stacks[move[2] - 1].extend(reversed(new))
    return "".join([i.pop() if i else "" for i in stacks])


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == "CMZ"
    assert part_2(test_input) == "MCD"

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

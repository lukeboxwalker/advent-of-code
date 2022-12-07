from aoc.api import *


def read_input(filename: str) -> dict:
    disc, stack = {'/': 0}, []
    with open(filename, "r") as f:
        for line in f.read().replace("$ ls\n", "").split("\n"):
            if line.startswith("$ cd"):
                stack.pop() if line.split(" ")[-1] == ".." else stack.append(line.split(" ")[-1])
            elif line.startswith("dir"):
                disc["".join(stack) + line.split(" ")[1]] = 0
            else:
                for i in range(len(stack)):
                    disc["".join(stack[:i]) + stack[i]] += int(line.split(" ")[0])
    return disc


def part_1(disc: dict) -> int:
    return Stream(disc.values()).filter(lambda x: x < 100_000).sum()


def part_2(disc: dict) -> int:
    return Stream(disc.values()).filter(lambda x: x > disc["/"] - 40_000_000).min()


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 95437
    assert part_2(test_input) == 24933642

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

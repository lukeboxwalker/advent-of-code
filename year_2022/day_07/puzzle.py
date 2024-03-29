from aoc.api import *


def read_input(filename: str) -> list:
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
    return sorted(disc.values())


def part_1(disc: list) -> int:
    return sum(filter(lambda x: x < 100_000, disc))


def part_2(disc: list) -> int:
    return min(filter(lambda x: x > disc[-1] - 40_000_000, disc))


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 95437
    assert part_2(read_input("test_input.txt")) == 24933642

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

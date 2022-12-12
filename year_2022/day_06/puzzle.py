from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return Stream(f.read()).list()

def solve(values: list, size: int):
    for i in range(len(values)):
        if len(set(values[i: i + size])) == size:
            return i + size

def part_1(values: list) -> int:
    return solve(values, 4)


def part_2(values: list) -> int:
    return solve(values, 14)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 7
    assert part_2(read_input("test_input.txt")) == 19

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

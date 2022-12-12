from aoc.api import *


def read_input(filename: str) -> list:
    return FileStream(filename).list()


def part_1(values: list) -> int:
    return 0


def part_2(values: list) -> int:
    return 0


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 0
    assert part_2(read_input("test_input.txt")) == 0

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

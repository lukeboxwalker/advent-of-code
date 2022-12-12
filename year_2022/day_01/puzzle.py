from aoc.api import *


def read_input(filename: str) -> Stream:
    return FileStream(filename, "\n\n").map(Stream.split("\n").map(int))


def part_1(values: Stream) -> int:
    return values.map(sum).max()


def part_2(values: Stream) -> int:
    return values.map(sum).sorted().last(3).sum()


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 24000
    assert part_2(read_input("test_input.txt")) == 45000

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

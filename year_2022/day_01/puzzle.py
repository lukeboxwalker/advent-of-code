from aoc.api import *


def read_input(filename: str) -> Stream:
    return FileStream(filename, "\n\n").map(MapStream.split("\n").map(int)).list()


def part_1(values: Stream) -> int:
    return values.map(sum).max()


def part_2(values: Stream) -> int:
    return values.map(sum).sorted().last(3).sum()


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 24000
    assert part_2(test_input) == 45000

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

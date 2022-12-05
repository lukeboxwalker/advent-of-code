from aoc.api import *


def read_input(filename: str) -> Stream:
    return FileStream(filename).map(
        MapStream(list).map(ord).map(lambda x: x - 96 if x > 90 else x - 38)
    )


def part_1(values: Stream) -> int:
    return values.map(
        MapStream(String.divide).map(set).reduce(Set.intersection)
    ).map(Set.pop).sum()


def part_2(values: Stream) -> int:
    return values.group(3).map(
        MapStream().map(set).reduce(Set.intersection)
    ).map(Set.pop).sum()


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 157
    assert part_2(test_input) == 70

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))
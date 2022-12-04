from aoc.api import *


def read_input(filename: str) -> list:
    return FileStream(filename).map(
        MapStream.split(",").map(
            MapStream.split("-").map(int).to(IntTuple)
        ).to(Tuple)
    ).list()


def part_1(values: list) -> int:
    return Stream(values).map(IntTuple.includes).map(int).sum()


def part_2(values: list) -> int:
    return Stream(values).map(IntTuple.overlaps).map(int).sum()


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 2
    assert part_2(test_input) == 4

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

from aoc.api import *


def read_input(filename: str) -> Stream:
    return FileStream(filename).map(
        Stream.split(",").map(
            Stream.split("-").map(int).to(IntTuple)
        ).to(Tuple)
    )


def part_1(values: Stream) -> int:
    return values.map(IntTuple.include_other).map(int).sum()


def part_2(values: Stream) -> int:
    return values.map(IntTuple.overlap_other).map(int).sum()


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 2
    assert part_2(test_input) == 4

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

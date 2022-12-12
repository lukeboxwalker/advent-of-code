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
    assert part_1(read_input("test_input.txt")) == 2
    assert part_2(read_input("test_input.txt")) == 4

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

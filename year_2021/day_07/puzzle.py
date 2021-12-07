from aoc.utils import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return list(map(int, f.read().splitlines()[0].split(",")))


def solve(values: list, f) -> int:
    return int(min([sum(map(lambda x: f(abs(x - i)), values)) for i in range(max(values))]))


def part_1(values: list) -> int:
    return solve(values, lambda x: x)


def part_2(values: list) -> int:
    return solve(values, lambda x: x * (x + 1) / 2)


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 37
    assert part_2(test_input) == 168

    my_input = read_input("input.txt")
    log(f"Part 1: {part_1(my_input)}, {timings(lambda: part_1(my_input))}")
    log(f"Part 2: {part_2(my_input)}, {timings(lambda: part_2(my_input))}")

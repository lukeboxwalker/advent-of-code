import numpy as np

from aoc.utils import *


def read_input(filename: str) -> np.array:
    with open(filename, "r") as f:
        return np.array(f.read().splitlines()[0].split(",")).astype(int)


def calc(values: np.array, i: int, f):
    return sum(map(lambda x: f(abs(x - i)), values))


def solve(values: np.array, f, g):
    m = f(values)
    upper = int(np.ceil(m))
    lower = int(np.floor(m))
    return int(min(calc(values, upper, g), calc(values, lower, g)))


def part_1(values: np.array) -> int:
    return solve(values, np.median, lambda x: x)


def part_2(values: np.array) -> int:
    return solve(values, np.mean, lambda x: x * (x + 1) / 2)


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 37
    assert part_2(test_input) == 168

    my_input = read_input("input.txt")
    log(f"Part 1: {part_1(my_input)}, {timings(lambda: part_1(my_input))}")
    log(f"Part 2: {part_2(my_input)}, {timings(lambda: part_2(my_input))}")

import functools
import itertools

from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(eval, i.split("\n"))) for i in f.read().split("\n\n")]

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:  # are equal
            return 0
        if a < b:  # a is smaller
            return -1
        if a > b:  # a is bigger
            return 1

    if isinstance(a, int):
        return compare([a], b)

    if isinstance(b, int):
        return compare(a, [b])

    a_size = len(a)
    b_size = len(b)
    for i in range(a_size):
        if i >= b_size:
            return 1  # b run out
        order = compare(a[i], b[i])
        if order == 0:  # i's elem is equal
            continue
        return order  # a is smaller or bigger
    if a_size < b_size:
        return -1  # a run out
    return 0  # all elems are equal


def part_1(values: list) -> int:
    return sum((i + 1) * abs((compare(val[0], val[1]) - 1) // -2) for i, val in enumerate(values))


def part_2(values: list) -> int:
    values = list(itertools.chain.from_iterable(values))
    values.extend([[6], [2]])
    values = sorted(values, key=functools.cmp_to_key(compare))
    return (values.index([2]) + 1) * (values.index([6]) + 1)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 13
    assert part_2(read_input("test_input.txt")) == 140

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

from functools import reduce

import aoc.api as aoc


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(lambda x: ord(x) - (96 if x.islower() else 38), list(i))) for i in f.read().splitlines()]


def part_1(values: list) -> int:
    return sum(map(lambda x: (set(x[:len(x) // 2]) & set(x[len(x) // 2:])).pop(), values))


def part_2(values: list) -> int:
    return sum([reduce(lambda a, b: a & b, map(set, values[i:i + 3])).pop() for i in range(0, len(values), 3)])


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 157
    assert part_2(test_input) == 70

    my_input = read_input("input.txt")
    aoc.print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

from functools import reduce

from aoc.api import print_solution


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().splitlines()


def priority(letter: str):
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 38


def part_1(values: list) -> int:
    return sum(map(lambda x: priority((set(x[:len(x) // 2]) & set(x[len(x) // 2:])).pop()), values))


def part_2(values: list) -> int:
    labels = [reduce(lambda a, b: a & b, map(set, values[i:i + 3])) for i in range(0, len(values), 3)]
    return sum(map(lambda x: priority(x.pop()), labels))


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 157
    assert part_2(test_input) == 70

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

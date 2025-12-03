from aoc.api import *


def read_input(filename: str) -> list:
    return FileStream(filename).map(MapStream(String.split("")).map(int)).list()

def get_max_jolt(value: list, digits: int):
    max_jolt = [0] * digits
    for (i, x) in enumerate(value):
        for (j, jolt) in enumerate(max_jolt):
            rev_j = len(max_jolt) - 1 - j
            if x > jolt and i < len(value) - rev_j:
                max_jolt[j] = x
                for k in range(j + 1, len(max_jolt)):
                    max_jolt[k] = 0
                break
    return int("".join(map(str, max_jolt)))


def part_1(values: list) -> int:
    result = []
    for value in values:
        result.append(get_max_jolt(value, 2))
    return sum(result)


def part_2(values: list) -> int:
    result = []
    for value in values:
        result.append(get_max_jolt(value, 12))
    return sum(result)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 357
    assert part_2(read_input("test_input.txt")) == 3121910778619

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

import re

from aoc.api import *


def read_input(filename: str) -> list:
    return FileStream(filename).map(Stream.split(",").map(Stream.split("-").map(int))).list()[0]

def part_1(values: list) -> int:
    result = 0
    regex = re.compile(r"^(\d+?)\1$")
    for value in values:
        for x in range(value[0], value[1] + 1):
            if regex.search(str(x)):
                result += x
    return result


def part_2(values: list) -> int:
    result = 0
    regex = re.compile(r"^(\d+?)\1+$")
    for value in values:
        for x in range(value[0], value[1] + 1):
            if regex.search(str(x)):
                result += x
    return result


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 1227775554
    assert part_2(read_input("test_input.txt")) == 4174379265

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

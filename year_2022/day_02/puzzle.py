from aoc.api import *

def read_input(filename: str) -> Stream:
    return FileStream(filename).map(String.replace(" ", ""))


def part_1(values: Stream) -> int:
    points = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}
    return values.map(lambda x: points[x]).sum()


def part_2(values: Stream) -> int:
    points = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
    return values.map(lambda x: points[x]).sum()


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 15
    assert part_2(test_input) == 12

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

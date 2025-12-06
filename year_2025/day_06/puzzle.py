import re

from aoc.api import *


def read_input(filename: str) -> list:
    return FileStream(filename).list()


def part_1(values: list) -> int:
    numbers = list(map(lambda x: list(map(int, re.findall("(\\d+)", x))), values[:len(values) - 1]))
    operations = [sum if x == "+" else prod for x in list(values[-1]) if x != " "]
    return sum(operations[col_index]([row[col_index] for row in numbers]) for col_index in range(len(numbers[0])))


def part_2(values: list) -> int:
    operations = [(sum if x == "+" else prod, []) for x in list(values[-1]) if x != " "]
    max_len = max(map(len, values[:len(values) - 1]))
    operation_index = 0
    for i in range(max_len + 1):
        col = ''.join(["" if len(r) - 1 < i else r[i] for r in values[:len(values) - 1]]).replace(" ", "")
        if col.isdigit():
            operations[operation_index][1].append(int(col))
        else:
            operation_index += 1
    return sum(map(lambda x: x[0](x[1]), operations))


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 4277556
    assert part_2(read_input("test_input.txt")) == 3263827

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

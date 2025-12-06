import re

from aoc.api import *

def read_input(filename: str) -> list:
    return FileStream(filename).list()


def part_1(values: list) -> int:
    numbers = Stream(values[:len(values) - 1]).map(lambda x: Stream(re.findall("(\\d+) *", x)).map(int).list()).list()
    operations = [x for x in list(values[-1]) if x != " "]
    result = 0
    for col_index in range(len(numbers[0])):
        col = [row[col_index] for row in numbers]
        if operations[col_index] == "+":
            result += sum(col)
        if operations[col_index] == "*":
            result += prod(col)
    return result


def part_2(values: list) -> int:
    operations = [(x, []) for x in list(values[-1]) if x != " "]
    grid = values[:len(values) - 1]
    max_len = max(map(len, grid))
    operation_index = 0
    for col_index in range(max_len + 1):
        col = ''.join(["" if len(row)-1 < col_index else row[col_index] for row in grid]).replace(" ","")
        if col.isdigit():
            operations[operation_index][1].append(int(col))
        else:
            operation_index += 1
    result = 0
    for operation in operations:
        if operation[0] == "+":
            result += sum(operation[1])
        if operation[0] == "*":
            result += prod(operation[1])
    return result


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 4277556
    assert part_2(read_input("test_input.txt")) == 3263827

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

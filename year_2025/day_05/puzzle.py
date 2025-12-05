import math

from aoc.api import *


def read_input(filename: str) -> list:
    data = FileStream(filename).list()
    result = [[], []]
    for line in data:
        if "-" in line:
            ranges = line.split("-")
            result[0].append((int(ranges[0]), int(ranges[1])))
        elif line.isdigit():
            result[1].append(int(line))
    result[0] = merge_ranges(result[0])
    return result

def merge_ranges(values):
    ranges = sorted(values, key=lambda x: x[0])
    merged = [ranges[0]]
    for current in ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

def part_1(values: list) -> int:
    fresh = 0
    for num_id in values[1]:
        for id_min, id_max in values[0]:
            if id_min <= num_id <= id_max:
                fresh += 1
                break
    return fresh


def part_2(values: list) -> int:
    values_in_ranges = list(map(lambda x: x[1] - x[0] + 1, values[0]))
    return sum(values_in_ranges)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 3
    assert part_2(read_input("test_input.txt")) == 14

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

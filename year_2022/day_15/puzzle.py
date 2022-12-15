from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        zone = []
        for line in f.read().splitlines():
            split = line.replace("Sensor at ", "").replace("closest beacon is at ", "").split(": ")
            split = list(map(lambda x: x.split(", "), split))
            sensor = (int(split[0][0][2:]), int(split[0][1][2:]))
            beacon = (int(split[1][0][2:]), int(split[1][1][2:]))
            zone.append([sensor, beacon])
        return zone

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def blocked_ranges(values: list, y: int):
    min_max = []
    for value in values:
        d = manhattan(value[0], value[1])
        min_row = value[0][1] - d
        max_row = value[0][1] + d
        min_col = value[0][0] - d
        max_col = value[0][0] + d
        if min_row <= y <= max_row:  # if y is in range of sensor
            dist = abs(value[0][1] - y)
            new_min = min_col + dist
            new_max = max_col - dist
            min_max.append((new_min, new_max))
    for i in range(-len(min_max), len(min_max)):
        base = min_max[i]
        for j in range(len(min_max)):
            new_base = combine_ranges(base, min_max[j])
            if base != new_base:
                min_max[j] = new_base
                base = new_base
        min_max[i] = base
    return set(min_max)

def combine_ranges(a, b):
    if a[0] <= b[0] and a[1] >= b[1]:  # a0 b0 b1 a1
        return a
    if b[0] <= a[0] and b[1] >= a[1]:  # b0 a0 a1 b1
        return b
    if b[0] <= a[0] - 1 <= b[1] <= a[1]:   # b0 a0 b1 a1
        return b[0], a[1]
    if a[0] <= b[0] <= a[1] + 1 <= b[1]:   # a0 b0 a1 b1
        return a[0], b[1]
    return a

def part_1(values: list, y: int) -> int:
    blocked = set()
    for value in values:
        blocked.add(value[0])
        blocked.add(value[1])
    min_max = blocked_ranges(values, y)
    block_range = min_max.pop()
    count = 0
    for i in blocked:
        if i[1] == y and block_range[0] <= i[0] <= block_range[1]:
            count -= 1
    count += abs(block_range[0]) + abs(block_range[1]) + 1
    return count


def part_2(values: list, bounds: int) -> int:
    for y in range(bounds):
        blocked = blocked_ranges(values, y)
        if len(blocked) == 2:
            first = blocked.pop()
            second = blocked.pop()
            if first[1] < second[0]:
                return (first[1] + 1) * 4000000 + y
            if second[1] < first[0]:
                return (second[1] + 1) * 4000000 + y


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt"), 10) == 26
    assert part_2(read_input("test_input.txt"), 20) == 56000011

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"), 2_000_000)))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"), 4_000_000)))


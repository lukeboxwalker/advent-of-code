from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        blocked, depth = set(), 0
        for line in f.read().splitlines():
            values = line.split(" -> ")
            for i in range(1, len(values)):
                a, b = (eval(values[i - 1])), (eval(values[i]))
                depth = depth if depth > a[1] else a[1]
                d = (0, int_compare(b[1], a[1])) if a[0] == b[0] else (int_compare(b[0], a[0]), 0)
                while a != b:
                    blocked.add(a)
                    a = (a[0] + d[0], a[1] + d[1])
            blocked.add((eval(values[-1])))
            depth = depth if depth > (eval(values[-1]))[1] else (eval(values[-1]))[1]
    return [blocked, depth]


def int_compare(a: int, b: int):
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def drop_sand_part_1(sand: tuple, blocked: set, depth: int):
    if sand[1] > depth:
        return -1

    if (sand[0], sand[1]) in blocked:
        left = (sand[0] - 1, sand[1])
        if left not in blocked:
            dropped = drop_sand_part_1(left, blocked, depth)
            if dropped == -1 or dropped == 0:
                return dropped
        right = (sand[0] + 1, sand[1])
        if right not in blocked:
            dropped = drop_sand_part_1(right, blocked, depth)
            if dropped == -1 or dropped == 0:
                return dropped
        blocked.add((sand[0], sand[1] - 1))
        return 0
    return drop_sand_part_1((sand[0], sand[1] + 1), blocked, depth)


def part_1(values: list) -> int:
    count = 0
    while drop_sand_part_1((500, 0), values[0], values[1]) == 0:
        count += 1
    return count


def drop_sand_part_2(sand: tuple, blocked: set, depth: int):
    if (sand[0], sand[1]) in blocked or sand[1] == depth + 2:
        left = (sand[0] - 1, sand[1])
        if left not in blocked and sand[1] < depth + 2:
            dropped = drop_sand_part_2(left, blocked, depth)
            if dropped == -1 or dropped == 0:
                return dropped
        right = (sand[0] + 1, sand[1])
        if right not in blocked and sand[1] < depth + 2:
            dropped = drop_sand_part_2(right, blocked, depth)
            if dropped == -1 or dropped == 0:
                return dropped
        if (sand[0], sand[1] - 1) == (500, 0):
            return -1
        blocked.add((sand[0], sand[1] - 1))
        return 0
    return drop_sand_part_2((sand[0], sand[1] + 1), blocked, depth)


def part_2(values: list) -> int:
    count = 0
    while drop_sand_part_2((500, 0), values[0], values[1]) == 0:
        count += 1
    return count + 1


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 24
    assert part_2(read_input("test_input.txt")) == 93
    #
    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

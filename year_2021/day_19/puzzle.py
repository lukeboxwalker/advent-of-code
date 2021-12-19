import itertools
import re


def read_input(filename: str) -> tuple:
    with open(filename, "r") as f:
        def coordinates(i):
            return set(map(lambda x: tuple(map(int, x.split(","))), i.split("\n")))

        return solve([coordinates(i) for i in re.sub("-.*-\n", "", f.read()).split("\n\n")])


def transform(factor: tuple, shuffle: tuple, x: tuple) -> tuple:
    new = [x[0], x[1], x[2]]
    new[shuffle[0]] = factor[0] * x[0]
    new[shuffle[1]] = factor[1] * x[1]
    new[shuffle[2]] = factor[2] * x[2]
    return new[0], new[1], new[2]


def sub(a: tuple, b: tuple):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def add(a: tuple, b: tuple):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


factors: list = [(i, j, k) for i in [1, -1] for j in [1, -1] for k in [1, -1]]
shuffles: list = list(itertools.permutations([0, 1, 2], r=3))


def find_scanner(current_map, origin_scan):
    scans = []
    for factor in factors:
        for shuffle in shuffles:
            scans.append(set(map(lambda x: transform(factor, shuffle, x), origin_scan)))
    for fix_point in current_map:
        fix_map = {sub(point, fix_point) for point in current_map}
        for beacons in scans:
            for beacon in beacons:
                if sum([1 if sub(point, beacon) in fix_map else 0 for point in beacons]) >= 12:
                    return sub(fix_point, beacon), beacons

def solve(values: list):
    scanner_pos = {0: (0, 0, 0)}
    beacon_map = values[0].copy()
    while len(scanner_pos) != len(values):
        for i in range(len(values)):
            if i in scanner_pos:
                continue
            scanner = values[i]
            optional = find_scanner(beacon_map, scanner)
            if optional is not None:
                scanner = optional[0]
                beacons = optional[1]
                for point in beacons:
                    beacon_map.add(add(point, scanner))
                scanner_pos[i] = scanner
    return scanner_pos, beacon_map


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def part_1(values: tuple) -> int:
    scanner_pos, beacon_map = values

    return len(beacon_map)


def part_2(values: tuple) -> int:
    scanner_pos, beacon_map = values
    return max([manhattan_distance(scanner_pos[a], scanner_pos[b]) for a in scanner_pos for b in scanner_pos])


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 79
    assert part_2(test_input) == 3621

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}")
    print(f"Part 2: {part_2(my_input)}")

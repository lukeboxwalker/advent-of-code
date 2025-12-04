from aoc.api import *


def read_input(filename: str) -> set:
    grid = FileStream(filename).map(MapStream(String.split(""))).list()
    return {(x, y) for x, row in enumerate(grid) for y, c in enumerate(row) if c == "@"}


def get_accessible_positions(values: set):
    return {(x, y) for x, y in values if len(get_neighbors(x, y, values)) < 4}


def get_neighbors(x: int, y: int, values: set):
    return {(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)} & values


def remove_scrolls(values: set, accessible: set):
    return values - accessible


def part_1(values: set) -> int:
    return len(get_accessible_positions(values))


def part_2(values: set) -> int:
    accessible = 0
    while accessible_positions := get_accessible_positions(values):
        accessible += len(accessible_positions)
        values = remove_scrolls(values, accessible_positions)
    return accessible


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 13
    assert part_2(read_input("test_input.txt")) == 43

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

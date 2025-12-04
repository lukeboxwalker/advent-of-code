from typing import Any

from numpy import ndarray, dtype

from aoc.api import *


def read_input(filename: str) -> ndarray[int, dtype[int]]:
    return np.array(FileStream(filename).map(MapStream(String.split(""))).list())

def get_accessible_positions(values: ndarray[int, dtype[int]]):
    accessible = []
    for x in range(len(values)):
        for y in range(len(values[x])):
            if values[x][y] != "@":
                continue
            rows, cols = values.shape

            x0 = max(x - 1, 0)
            x1 = min(x + 2, rows)
            y0 = max(y - 1, 0)
            y1 = min(y + 2, cols)

            neighbor_slice = values[x0:x1, y0:y1]
            sx = x - x0
            sy = y - y0
            at_count = 0
            for nx in range(len(neighbor_slice)):
                for ny in range(len(neighbor_slice[nx])):
                    if nx == sx and ny == sy:
                        continue
                    if neighbor_slice[nx][ny] == "@":
                        at_count += 1
            if at_count < 4:
                accessible.append([x, y])
    return accessible

def remove_scrolls(values: ndarray[int, dtype[int]], accessible: list):
    for pos in accessible:
        values[pos[0]][pos[1]] = "."

def part_1(values: ndarray[int, dtype[int]]) -> int:
    return len(get_accessible_positions(values))


def part_2(values: ndarray[int, dtype[int]]) -> int:
    accessible = 0
    accessible_positions = get_accessible_positions(values)
    while len(accessible_positions) > 0:
        accessible += len(accessible_positions)
        remove_scrolls(values, accessible_positions)
        accessible_positions = get_accessible_positions(values)
    return accessible


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 13
    assert part_2(read_input("test_input.txt")) == 43

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

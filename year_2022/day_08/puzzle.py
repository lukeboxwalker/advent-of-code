import numpy as np
from numpy import ndarray

from aoc.api import *


def read_input(filename: str) -> ndarray:
    with open(filename, "r") as f:
        return np.array([list(map(int, row)) for row in f.read().splitlines()])


def directions(values, i, j):
    return [list(reversed(values[i][:j])), values[i][j + 1:],  # left, right
            list(reversed(values[:, j][:i])), values[:, j][i + 1:]]  # top, bottom


def part_1(values: ndarray) -> int:
    return Stream(np.ndindex(values.shape)).map(
        lambda x: Stream(directions(values, x[0], x[1]))
            .map(lambda y: max(y) if len(y) > 0 else -1)
            .map(lambda y: y < values[x[0], x[1]])
            .reduce(lambda a, b: a or b)
    ).map(int).sum()


def part_2(values: ndarray) -> int:
    count = []
    for i, j in np.ndindex(values.shape):
        scenic_score = [0, 0, 0, 0]
        sides = directions(values, i, j)
        for k in range(4):
            for m in sides[k]:
                scenic_score[k] += 1
                if m >= values[i, j]:
                    break
        count.append(Stream(scenic_score).reduce(lambda a, b: a * b))
    return max(count)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 21
    assert part_2(read_input("test_input.txt")) == 8

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

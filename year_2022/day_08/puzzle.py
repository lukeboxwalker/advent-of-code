import numpy as np
from numpy import ndarray

from aoc.api import *


def read_input(filename: str) -> ndarray:
    with open(filename, "r") as f:
        return np.array([list(map(int, row)) for row in f.read().splitlines()])

def part_1(values: ndarray) -> int:
    count = 0
    for i, j in np.ndindex(values.shape):
        sides = Stream([values[i][:j], values[i][j + 1:], values[:, j][:i], values[:, j][i + 1:]]) \
            .map(lambda x: x if x.size > 0 else np.array([-1])).list()
        count += int(Stream(sides).map(lambda x: max(x) < values[i, j]).reduce(lambda a, b: a or b))
    return count


def part_2(values: ndarray) -> int:
    count = []
    for i, j in np.ndindex(values.shape):
        scenic_score = [0, 0, 0, 0]
        sides = [reversed(values[i][:j]), values[i][j + 1:], reversed(values[:, j][:i]), values[:, j][i + 1:]]
        for k in range(4):
            for m in sides[k]:
                scenic_score[k] += 1
                if m >= values[i, j]:
                    break
        count.append(Stream(scenic_score).reduce(lambda a, b: a * b))
    return max(count)


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 21
    assert part_2(test_input) == 8

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

from timeit import timeit

import numpy as np


def read_input(filename: str) -> np.array:
    with open(filename, "r") as f:
        return np.array([np.array(list(i)).astype(int) for i in f.read().splitlines()])


def flash(values: np.array, i: int, j: int) -> int:
    if values[i, j] <= 9:
        return 0
    values[i, j], flashes = 0, 1
    for di in range(i - 1, i + 2):
        for dj in range(j - 1, j + 2):
            if -1 < di < values.shape[0] and -1 < dj < values.shape[1] and (di != i or j != dj):
                if values[di, dj] != 0:
                    values[di, dj] += 1
                if values[di, dj] > 9:
                    flashes += flash(values, di, dj)
    return flashes


def part_1(values: np.array) -> int:
    current = np.copy(values)
    step = np.ones(values.shape).astype(int)
    flashes = 0
    for k in range(100):
        current += step
        flashes += sum([flash(current, i, j) for i in range(10) for j in range(10)])
    return flashes


def part_2(values: np.array) -> int:
    current = np.copy(values)
    step = np.ones(values.shape).astype(int)
    idx = 1
    while True:
        current += step
        flashes = sum([flash(current, i, j) for i in range(10) for j in range(10)])
        if flashes == 100:
            return idx
        idx += 1


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 1656
    assert part_2(test_input) == 195

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

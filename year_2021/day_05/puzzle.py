from timeit import timeit

import numpy as np

from setup.console import console


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(lambda x: np.array(x.split(",")).astype(int), i.split(" -> "))) for i in f.read().splitlines()]


def part_1(values: list) -> int:
    values, count = [np.copy(i) for i in values if i[0][0] == i[1][0] or i[0][1] == i[1][1]], {}
    for i in values:
        delta, vec = (i[1] - i[0]) // abs((i[1] - i[0])[0] + (i[1] - i[0])[1]), i[0]
        while not np.array_equal(vec, i[1] + delta):
            if (vec[0], vec[1]) in count:
                count[(vec[0], vec[1])] += 1
            else:
                count[(vec[0], vec[1])] = 1
            vec += delta
    return sum([1 for i in count if count[i] > 1])


def part_2(values: list) -> int:
    count = {}
    for i in values:
        delta, vec = (i[1] - i[0]) // max(abs((i[1] - i[0])[1]), abs((i[1] - i[0])[0])), i[0]
        while not np.array_equal(vec, i[1] + delta):
            if (vec[0], vec[1]) in count:
                count[(vec[0], vec[1])] += 1
            else:
                count[(vec[0], vec[1])] = 1
            vec += delta
    return sum([1 for i in count if count[i] > 1])


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 5
    assert part_2(test_input) == 12

    my_input = read_input("input.txt")
    console.print(f"Part 1: {part_1(my_input)}, Timing: {timeit(lambda: part_1(my_input), number=1)}")
    console.print(f"Part 2: {part_2(my_input)}, Timing: {timeit(lambda: part_2(my_input), number=1)}")

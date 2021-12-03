from timeit import timeit

import numpy as np


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(int, list(i))) for i in f.read().splitlines()]


def part_1(values: list) -> int:
    gamma = np.array(list(map(lambda x: sum(x) > len(values) // 2, np.array(values).T)))
    epsilon = np.invert(gamma)
    int_gamma = int("".join(gamma.astype(int).astype(str)), 2)
    int_epsilon = int("".join(epsilon.astype(int).astype(str)), 2)
    return int_gamma * int_epsilon


def part_2(values: list) -> int:
    transpose = np.array(values).T
    idx_ox = list(range(len(transpose[0])))
    idx_co2 = list(range(len(transpose[0])))
    for i in range(len(transpose)):
        if len(idx_ox) != 1:
            sub_set = transpose[i][idx_ox]
            most = 1 if sum(sub_set) >= len(sub_set) / 2 else 0
            idx_ox = [j for j in idx_ox if transpose[i][j] == most]
        if len(idx_co2) != 1:
            sub_set = transpose[i][idx_co2]
            least = 1 if sum(sub_set) < len(sub_set) / 2 else 0
            idx_co2 = [j for j in idx_co2 if transpose[i][j] == least]
    int_ox = int("".join(np.array(values[idx_ox[0]]).astype(str)), 2)
    int_co2 = int("".join(np.array(values[idx_co2[0]]).astype(str)), 2)
    return int_ox * int_co2


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 198
    assert part_2(test_input) == 230

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: {timeit(lambda: part_1(my_input), number=1)}")
    print(f"Part 2: {part_2(my_input)}, Timing: {timeit(lambda: part_2(my_input), number=1)}")

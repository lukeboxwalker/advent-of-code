from functools import reduce
from timeit import timeit


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(int, list(i))) for i in f.read().splitlines()]


def part_1(values: list) -> int:
    gamma, epsilon, half = 0, 0, len(values) / 2
    for i in range(len(values[0])):
        s = sum([values[j][i] for j in range(len(values))])
        gamma = (gamma << 1) | (s > half)
        epsilon = (epsilon << 1) | (s < half)
    return gamma * epsilon


def part_2(values: list) -> int:
    idx_ox = list(range(len(values)))
    idx_co2 = list(range(len(values)))
    for i in range(len(values[0])):
        if len(idx_ox) != 1:
            sub_set = [values[j][i] for j in idx_ox]
            most = 1 if sum(sub_set) >= len(sub_set) / 2 else 0
            idx_ox = [j for j in idx_ox if values[j][i] == most]
        if len(idx_co2) != 1:
            sub_set = [values[j][i] for j in idx_co2]
            least = 1 if sum(sub_set) < len(sub_set) / 2 else 0
            idx_co2 = [j for j in idx_co2 if values[j][i] == least]
    int_ox = reduce(lambda a, b: (a << 1) | b, [0] + values[idx_ox[0]])
    int_co2 = reduce(lambda a, b: (a << 1) | b, [0] + values[idx_co2[0]])
    return int_ox * int_co2


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 198
    assert part_2(test_input) == 230

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

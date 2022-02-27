from timeit import timeit

import numpy as np


class Die:

    def __init__(self):
        self.value = 0
        self.thrown = 0

    def next(self, throw=1):
        sum_values = 0
        for i in range(throw):
            self.value += 1
            self.value = self.value if self.value <= 100 else self.value % 101 + 1
            sum_values += self.value
        self.thrown += throw
        return sum_values


def read_input(filename: str) -> np.array:
    with open(filename, "r") as f:
        return np.array([int(i[-1]) for i in f.read().splitlines()])


def part_1(values: np.array) -> int:
    score = np.zeros(2).astype(int)
    positions = values.copy()
    die = Die()
    player = 0
    while max(score) < 1000:
        moves = die.next(3)
        positions[player] += moves
        if positions[player] % 10 == 0:
            positions[player] = 10
        else:
            positions[player] = positions[player] % 10
        score[player] += positions[player]
        player = int(not player)
    return min(score) * die.thrown


def part_2(values: np.array) -> int:
    return 0


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 739785
    # assert part_2(test_input) == 0
    #
    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    # print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

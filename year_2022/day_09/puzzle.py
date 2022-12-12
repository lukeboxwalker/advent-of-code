import numpy as np

from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        actions = {"R": np.array([1, 0]), "L": np.array([-1, 0]), "U": np.array([0, 1]), "D": np.array([0, -1])}
        moves = []
        for value in [i.split(" ") for i in f.read().splitlines()]:
            for _ in range(int(value[1])):
                moves.append(actions[value[0]])
        return moves

def solve(values: list, length: int):
    rope = [np.array([0, 0]) for _ in range(length)]
    positions = {(0, 0)}
    for move in values:
        rope[0] += move
        for i in range(1, length):
            if np.linalg.norm(rope[i - 1] - rope[i]) > 1.5:
                change = rope[i - 1] - rope[i]
                change[0] = change[0] / 2 if abs(change[0]) == 2 else change[0]
                change[1] = change[1] / 2 if abs(change[1]) == 2 else change[1]
                rope[i] += change
        positions.add(tuple(rope[length - 1]))
    return len(positions)

def part_1(values: list) -> int:
    return solve(values, 2)


def part_2(values: list) -> int:
    return solve(values, 10)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 13
    assert part_2(read_input("test_input.txt")) == 1

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

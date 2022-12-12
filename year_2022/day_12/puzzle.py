from collections import defaultdict

import numpy as np
from numpy import ndarray

from aoc.api import *


def read_input(filename: str) -> ndarray:
    with open(filename, "r") as f:
        return np.array([list(i) for i in f.read().splitlines()])

def pathfinder(values, start, goal) -> int:
    open_set = [start]

    g_score = defaultdict(lambda: np.inf)
    g_score[start] = 0

    f_score = defaultdict(lambda: np.inf)
    f_score[start] = np.linalg.norm(np.array(start) - np.array(goal))

    p_score = dict()
    p_score[start] = 0

    while open_set:
        current = min(open_set, key=lambda pos: f_score[pos])
        if current == goal:
            return p_score[current]

        open_set.remove(current)
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            child = (current[0] + x, current[1] + y)
            if 0 > child[0] or child[0] >= values.shape[0] or 0 > child[1] or child[1] >= values.shape[1]:
                continue
            value = ord(values[child]) - ord(values[current])
            if value > 1:
                continue
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[child]:
                g_score[child] = tentative_g_score
                f_score[child] = tentative_g_score + np.linalg.norm(np.array(child) - np.array(goal))
                p_score[child] = p_score[current] + 1
                if child not in open_set:
                    open_set.append(child)
    return np.inf

def start_and_goal(values: ndarray):
    start = tuple(np.array(np.where(values == "S")).reshape(2))
    goal = tuple(np.array(np.where(values == "E")).reshape(2))
    values[start] = "a"
    values[goal] = "z"
    return start, goal


def part_1(values: ndarray) -> int:
    start, goal = start_and_goal(values)
    return pathfinder(values, start, goal)


def part_2(values: ndarray) -> int:
    _, goal = start_and_goal(values)
    return min([pathfinder(values, (x, y), goal) for x, y in np.ndindex(values.shape) if values[x, y] == "a"])


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 31
    assert part_2(read_input("test_input.txt")) == 29

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

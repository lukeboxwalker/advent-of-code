from collections import defaultdict
from queue import PriorityQueue
from timeit import timeit

import numpy as np


def read_input(filename: str) -> np.array:
    with open(filename, "r") as f:
        return np.array([list(map(int, i)) for i in f.read().splitlines()])


def h(start, end):
    return np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)


def a_star(start: tuple, goal: tuple, values: np.array):
    g_score = defaultdict(lambda: np.inf)
    g_score[start] = 0

    open_queue = PriorityQueue()
    open_queue.put((h(start, goal), start))
    open_set = {start}

    while not open_queue.empty():
        current = open_queue.get()[1]
        if current == goal:
            return g_score[current]

        open_set.remove(current)
        for dn in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            neighbor = (current[0] + dn[0], current[1] + dn[1])
            if -1 < neighbor[0] < values.shape[0] and -1 < neighbor[1] < values.shape[1]:
                tentative_g_score = g_score[current] + values[neighbor[0]][neighbor[1]]
                if tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + h(neighbor, goal)
                    if neighbor not in open_set:
                        open_queue.put((f_score, neighbor))
                        open_set.add(neighbor)


def part_1(values: np.array) -> int:
    return a_star((0, 0), (values.shape[0] - 1, values.shape[1] - 1), values)


def part_2(values: np.array) -> int:
    expansion = np.zeros((values.shape[0] * 5, values.shape[1] * 5)).astype(int)
    for i in range(values.shape[0] * 5):
        for j in range(values.shape[1] * 5):
            val = values[i % values.shape[0]][j % values.shape[1]] + i // values.shape[0] + j // values.shape[0]
            expansion[i][j] = val if val < 10 else val % 10 + 1
    return part_1(expansion)


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 40
    assert part_2(test_input) == 315

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

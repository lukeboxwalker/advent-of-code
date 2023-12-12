from aoc.api import *


def read_input(filename: str) -> tuple:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        grid = []
        start = None
        for i in range(len(lines)):
            row = []
            for j in range(len(lines[i])):
                row.append(lines[i][j])
                if lines[i][j] == "S":
                    start = [i, j]
            grid.append(row)
    return start, grid


def next_node(prev, current, tube_type):
    if tube_type == "F":
        if current[0] + 1 == prev[0]:
            return [current[0], current[1] + 1]
        else:
            return [current[0] + 1, current[1]]
    if tube_type == "J":
        if current[0] - 1 == prev[0]:
            return [current[0], current[1] - 1]
        else:
            return [current[0] - 1, current[1]]
    if tube_type == "7":
        if current[0] + 1 == prev[0]:
            return [current[0], current[1] - 1]
        else:
            return [current[0] + 1, current[1]]
    if tube_type == "L":
        if current[0] - 1 == prev[0]:
            return [current[0], current[1] + 1]
        else:
            return [current[0] - 1, current[1]]
    if tube_type == "-":
        if current[1] + 1 == prev[1]:
            return [current[0], current[1] - 1]
        else:
            return [current[0], current[1] + 1]
    if tube_type == "|":
        if current[0] + 1 == prev[0]:
            return [current[0] - 1, current[1]]
        else:
            return [current[0] + 1, current[1]]


def part_1(values: tuple) -> int:
    start = values[0]
    neighbors = []
    if 0 <= start[0] + 1 < len(values[1]):
        tube_type = values[1][start[0] + 1][start[1]]
        if tube_type == "|" or tube_type == "L" or tube_type == "J":
            neighbors.append([start[0] + 1, start[1]])
    if 0 <= start[0] - 1 < len(values[1]):
        tube_type = values[1][start[0] - 1][start[1]]
        if tube_type == "|" or tube_type == "F" or tube_type == "7":
            neighbors.append([start[0] - 1, start[1]])
    if 0 <= start[1] + 1 < len(values[1]):
        tube_type = values[1][start[0]][start[1] + 1]
        if tube_type == "-" or tube_type == "7" or tube_type == "J":
            neighbors.append([start[0], start[1] + 1])
    if 0 <= start[1] - 1 < len(values[1]):
        tube_type = values[1][start[0]][start[1] - 1]
        if tube_type == "-" or tube_type == "F" or tube_type == "L":
            neighbors.append([start[0], start[1] - 1])

    forward = neighbors[0]
    forward_prev = start
    backward = neighbors[1]
    backward_prev = start
    distance = 1
    while forward != backward:
        next_forward = next_node(forward_prev, forward, values[1][forward[0]][forward[1]])
        forward_prev = forward
        forward = next_forward
        next_backward = next_node(backward_prev, backward, values[1][backward[0]][backward[1]])
        backward_prev = backward
        backward = next_backward
        distance += 1
    return distance


def part_2(values: tuple) -> int:
    return 0


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 8
    assert part_2(read_input("test_input.txt")) == 0

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

import numpy as np


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        actions = {"R": np.array([1, 0]), "L": np.array([-1, 0]), "U": np.array([0, 1]), "D": np.array([0, -1])}
        moves = []
        for value in [i.split(" ") for i in f.read().splitlines()]:
            for _ in range(int(value[1])):
                moves.append(actions[value[0]])
        return moves


def part_1(values: list) -> int:
    head = np.array([0, 0])
    tail = np.array([0, 0])
    positions = {(0, 0)}
    for move in values:
        head += move
        if np.linalg.norm(head - tail) > 1.5:
            change = (head - move) - tail
            tail += change
            positions.add(tuple(tail))
    return len(positions)


def part_2(values: list) -> int:
    head = np.array([0, 0])
    rope = [np.array([0, 0]) for _ in range(9)]
    positions = {(0, 0)}
    for move in values:
        head += move
        if np.linalg.norm(head - rope[0]) > 1.5:
            change = (head - move) - rope[0]
            rope[0] += change
            for i in range(1, 9):
                if np.linalg.norm(rope[i - 1] - rope[i]) > 1.5:
                    change = (rope[i - 1] - change) - rope[i]
                    rope[i] += change
            positions.add(tuple(rope[8]))
    print(len(positions))
    return 0


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    #assert part_1(test_input) == 13
    assert part_2(test_input) == 0

    # my_input = read_input("input.txt")
    # print_solution(lambda: part_1(my_input), lambda: part_2(my_input))



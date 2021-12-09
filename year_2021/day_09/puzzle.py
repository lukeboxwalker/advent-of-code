from timeit import timeit

import numpy as np


def read_input(filename: str) -> np.array:
    with open(filename, "r") as f:
        return np.array([np.array(list(i)).astype(int) for i in f.read().splitlines()])


def part_1(values: np.array) -> int:
    result = []
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if j + 1 < values.shape[1] and values[i, j] >= values[i, j + 1]:
                continue
            if j > 0 and values[i, j] >= values[i, j - 1]:
                continue
            if i + 1 < values.shape[0] and values[i, j] >= values[i + 1, j]:
                continue
            if i > 0 and values[i, j] >= values[i - 1, j]:
                continue
            result.append(values[i, j] + 1)
    return sum(result)


def part_2(values: np.array) -> int:
    labels, label, identical = np.zeros(values.shape).astype(int), 0, {}
    # mark regions
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if values[i, j] == 9:
                continue
            if j > 0 and values[i, j] < 9 and values[i, j - 1] < 9:
                labels[i, j] = labels[i, j - 1]
                if i > 0 and values[i, j] < 9 and values[i - 1, j] < 9 and labels[i, j] != labels[i - 1, j]:
                    identical[labels[i - 1, j]] = labels[i, j]
            elif i > 0 and values[i, j] < 9 and values[i - 1, j] < 9:
                labels[i, j] = labels[i - 1, j]
            else:
                label += 1
                labels[i, j] = label
    # combine identical regions
    for i in range(labels.shape[0]):
        for j in range(labels.shape[1]):
            if labels[i, j] in identical:
                replace = identical[labels[i, j]]
                while replace in identical:
                    replace = identical[replace]
                labels[i, j] = replace
    _, counts = np.unique(labels, return_counts=True)
    return int(np.prod(np.sort(counts)[-4:-1]))


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 15
    assert part_2(test_input) == 1134

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

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
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if values[i, j] == 9:
                values[i, j] = 1
            else:
                values[i, j] = 0
    label = 0
    label_array = np.zeros(values.shape).astype(int)
    identical = {}
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if values[i, j] == 1:
                continue
            if j > 0 and values[i, j] == values[i, j - 1]:
                label_array[i, j] = label_array[i, j - 1]
                if i > 0 and values[i, j] == values[i - 1, j] and label_array[i, j] != label_array[i - 1, j]:
                    identical[label_array[i - 1, j]] = label_array[i, j]
            elif i > 0 and values[i, j] == values[i - 1, j]:
                label_array[i, j] = label_array[i - 1, j]
            else:
                label += 1
                label_array[i, j] = label
    for i in range(label_array.shape[0]):
        for j in range(label_array.shape[1]):
            if label_array[i, j] in identical:
                replace = identical[label_array[i, j]]
                while replace in identical:
                    replace = identical[replace]
                label_array[i, j] = replace
    (unique, counts) = np.unique(label_array, return_counts=True)
    return int(np.prod(np.sort(np.asarray((unique, counts))[1][1:])[-3:]))


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    # assert part_1(test_input) == 15
    # assert part_2(test_input) == 1134

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

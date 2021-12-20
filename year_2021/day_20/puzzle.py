from functools import reduce
from timeit import timeit

import numpy as np


def read_input(filename: str) -> tuple:
    with open(filename, "r") as f:
        def to_int(i):
            return 1 if i == "#" else 0
        lines = f.read().split("\n\n")
        enhancement = np.array(list(map(to_int, list(lines[0]))))
        img = np.array(list(map(lambda x: list(map(to_int, list(x))), lines[1].split("\n"))))
        return enhancement, img

def expand_img(img: np.array, expand) -> np.array:
    supplier = np.zeros if expand == 0 else np.ones
    new = supplier((img.shape[0] + 4, img.shape[1] + 4)).astype(int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new[i + 2][j + 2] = img[i][j]
    return new

def bin_to_int(values: list):
    return reduce(lambda a, b: (a << 1) | b, [0] + values)

def enhance(enhancement, img, expand):
    img = expand_img(img, expand)
    enhanced_img = np.zeros((img.shape[0] - 2, img.shape[1] - 2)).astype(int)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            z = img[i - 1:i + 2, j - 1:j + 2].flatten()
            enhanced_img[i - 1][j - 1] = enhancement[bin_to_int(z.tolist())]
    return enhanced_img, enhancement[-expand]


def solve(values: tuple, n: int) -> int:
    enhancement, img = values
    inf_expand = 0
    for i in range(n):
        img, inf_expand = enhance(enhancement, img, inf_expand)
    return sum(sum(img))

def part_1(values: tuple) -> int:
    return solve(values, 2)


def part_2(values: tuple) -> int:
    return solve(values, 50)


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 35
    assert part_2(test_input) == 3351

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

import operator
from functools import reduce


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().splitlines()


def map_x(x: int, row_len: int) -> int:
    result = x
    while result > row_len - 1:
        result -= row_len
    return result


def count_trees(x: int, y: int, v: list):
    return sum([1 for n in range(1, len(v)) if y * n < len(v) and v[y * n][map_x(x * n, len(v[0]))] == '#'])


def part_1(values: list) -> int:
    return count_trees(3, 1, values)


def part_2(values: list) -> int:
    return reduce(operator.mul, [count_trees(x, y, values) for (x, y) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 7
    assert part_2(test_input) == 336

    my_input = read_input("input.txt")
    print("Puzzle 1:", part_1(my_input))
    print("Puzzle 2:", part_2(my_input))

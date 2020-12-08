from functools import reduce


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [line.replace("\n", " ") for line in f.read().split("\n\n")]


def part_1(values: list) -> int:
    return sum(len(reduce(set.union, map(set, val.split()))) for val in values)


def part_2(values: list) -> int:
    return sum(len(reduce(set.intersection, map(set, val.split()))) for val in values)


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 11
    assert part_2(test_input) == 6

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

from aoc.api import print_solution


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return []


def part_1(values: list) -> int:
    return 0


def part_2(values: list) -> int:
    return 0


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 0
    assert part_2(test_input) == 0

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

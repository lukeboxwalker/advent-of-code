import aoc.api as aoc


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(lambda x: list(map(int, x.split("-"))), i.split(","))) for i in f.read().splitlines()]


def part_1(values: list) -> int:
    count = 0
    for value in values:
        if value[0][0] >= value[1][0] and value[0][1] <= value[1][1]:
            count += 1
        elif value[1][0] >= value[0][0] and value[1][1] <= value[0][1]:
            count += 1
    return count


def part_2(values: list) -> int:
    count = 0
    for value in values:
        if value[1][1] >= value[0][1] >= value[1][0]:
            count += 1
        elif value[0][1] >= value[1][1] >= value[0][0]:
            count += 1
    return count


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 2
    assert part_2(test_input) == 4

    my_input = read_input("input.txt")
    aoc.print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

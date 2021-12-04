from timeit import timeit

from setup.console import console


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [(i.split()[0], int(i.split()[1])) for i in f.readlines()]


def part_1(values: list) -> int:
    horizontal = 0
    depth = 0
    for cmd in values:
        if cmd[0] == "forward":
            horizontal += cmd[1]
        elif cmd[0] == "down":
            depth += cmd[1]
        elif cmd[0] == "up":
            depth -= cmd[1]
    return horizontal * depth


def part_2(values: list) -> int:
    aim = 0
    horizontal = 0
    depth = 0
    for cmd in values:
        if cmd[0] == "forward":
            horizontal += cmd[1]
            depth += aim * cmd[1]
        elif cmd[0] == "down":
            aim += cmd[1]
        elif cmd[0] == "up":
            aim -= cmd[1]
    return horizontal * depth


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 150
    assert part_2(test_input) == 900

    my_input = read_input("input.txt")
    console.print(f"Part 1: {part_1(my_input)}, Timing: {timeit(lambda: part_1(my_input), number=1)}")
    console.print(f"Part 2: {part_2(my_input)}, Timing: {timeit(lambda: part_2(my_input), number=1)}")

from aoc.api import *


def read_input(filename: str) -> list:
    return FileStream(filename).map(lambda x: x.replace("R", "+").replace("L", "-")).map(int).list()


def part_1(values: list) -> int:
    dial = 50
    passcode = 0
    for value in values:
        dial = (dial + value) % 100
        passcode += 1 if dial == 0 else 0
    return passcode


def part_2(values: list) -> int:
    dial = 50
    passcode = 0
    for value in values:
        prev = dial
        dial += value
        rotation = value/100
        full_rotations = int(rotation)
        dial += -full_rotations * 100 # correct the dial value by ignoring full rotations

        passcode += 1 if dial == 0 and prev != 0 else 0 # rotated to 0 only if not 0 before
        passcode += 1 if dial % 100 != dial and prev != 0 else 0  # rotated over 0 only if not 0 before
        passcode += abs(full_rotations) # full rotations captured
        dial = dial % 100
    return passcode


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 3
    assert part_2(read_input("test_input.txt")) == 6

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

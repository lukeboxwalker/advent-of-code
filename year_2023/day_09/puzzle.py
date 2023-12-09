from aoc.api import *


def read_input(filename: str) -> tuple:
    with open(filename, "r") as f:
        return calc_extrapolations([list(map(int, line.split())) for line in f.read().splitlines()])

def extrapolate_last(numbers):
    extrapolation = numbers[-1]
    for i in range(len(numbers) - 2, -1, -1):
        extrapolation += numbers[i]
    return extrapolation

def extrapolate_first(numbers):
    extrapolation = numbers[-1]
    for i in range(len(numbers) - 2, -1, -1):
        extrapolation = numbers[i] - extrapolation
    return extrapolation

def calc_extrapolations(values: list) -> tuple:
    left_most_extrapolations = []
    right_most_extrapolations = []
    for numbers in values:
        last_numbers = [numbers[-1]]
        first_numbers = [numbers[0]]
        next_line = numbers
        while set(next_line) != {0}:
            new_line = []
            for i in range(len(next_line) - 1):
                new_line.append(next_line[i + 1] - next_line[i])
            next_line = new_line
            last_numbers.append(next_line[-1])
            first_numbers.append(next_line[0])
        right_most_extrapolations.append(extrapolate_last(last_numbers))
        left_most_extrapolations.append(extrapolate_first(first_numbers))
    return left_most_extrapolations, right_most_extrapolations

def part_1(values: tuple) -> int:
    return sum(values[1])


def part_2(values: tuple) -> int:
    return sum(values[0])


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 114
    assert part_2(read_input("test_input.txt")) == 2

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

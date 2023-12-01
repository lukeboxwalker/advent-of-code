from aoc.api import *


def read_input(filename: str) -> list:
    return FileStream(filename).list()


def part_1(values: list) -> int:
    result = 0
    for val in values:
        numbers = [i for i in val if str.isdigit(i)]
        result += int(numbers[0] + numbers[-1])
    return result


string_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_first_digit(val):
    for i in range(len(val)):
        if str.isdigit(val[i]):
            return val[i]
        for j in range(i, len(val)):
            sub_string = val[i:j]
            if sub_string in string_numbers:
                return str(string_numbers[sub_string])

def find_last_digit(val):
    for i in range(len(val) - 1, -1, -1):
        if str.isdigit(val[i]):
            return val[i]
        for j in range(i, -1, -1):
            sub_string = val[j + 1: i + 1]
            if sub_string in string_numbers:
                return str(string_numbers[sub_string])


def part_2(values: list) -> int:
    values_only_ints = []
    for val in values:
        values_only_ints.append(int(find_first_digit(val) + find_last_digit(val)))
    return sum(values_only_ints)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 142
    assert part_2(read_input("test_input_part2.txt")) == 281

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

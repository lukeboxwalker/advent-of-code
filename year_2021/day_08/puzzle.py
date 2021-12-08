from aoc.utils import *

easy_digits = {2: 1, 4: 4, 7: 8, 3: 7}


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(lambda x: x.split(), i.split(" | "))) for i in f.read().splitlines()]


def hamming_distance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance


def part_1(values: list) -> int:
    return sum([1 for v in values for i in v[1] if len(i) in easy_digits])


def part_2(values: list) -> int:
    num = 0
    for val in values:
        digits = val[0] + val[1]
        decoding = {}
        for digit in list(digits):
            if len(digit) in easy_digits:
                digits.remove(digit)
                decoding[easy_digits[len(digit)]] = set(digit)
        for digit in list(digits):
            if decoding[7].issubset(set(digit)) and decoding[4].issubset(set(digit)) and len(digit) == 6:
                digits.remove(digit)
                decoding[9] = set(digit)
        for digit in list(digits):
            if set(digit).issubset(decoding[9]) and not decoding[1].issubset(set(digit)) and len(digit) == 5:
                digits.remove(digit)
                decoding[5] = set(digit)
        for digit in list(digits):
            if set(digit).issubset(decoding[8]) and decoding[1].issubset(set(digit)) and len(digit) == 5:
                digits.remove(digit)
                decoding[3] = set(digit)
        for digit in list(digits):
            if decoding[5].issubset(set(digit)) and len(digit) == 6:
                digits.remove(digit)
                decoding[6] = set(digit)
        for digit in list(digits):
            if len(digit) == 6:
                digits.remove(digit)
                decoding[0] = set(digit)
            elif len(digit) == 5:
                digits.remove(digit)
                decoding[2] = set(digit)
        num += int("".join([str(k[0]) for digit in val[1] for k in decoding.items() if set(digit) == k[1]]))
    return num


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 26
    assert part_2(test_input) == 61229

    my_input = read_input("input.txt")
    log(f"Part 1: {part_1(my_input)}, {timings(lambda: part_1(my_input))}")
    log(f"Part 2: {part_2(my_input)}, {timings(lambda: part_2(my_input))}")

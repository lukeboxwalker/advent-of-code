from aoc.utils import *

easy_digits = {2: 1, 4: 4, 7: 8, 3: 7}


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(lambda x: x.split(), i.split(" | "))) for i in f.read().splitlines()]


def part_1(values: list) -> int:
    return sum([1 for v in values for i in v[1] if len(i) in easy_digits])


def part_2(values: list) -> int:
    num = 0
    for val in values:
        decoding = {}
        for digit in val[0] + val[1]:
            if len(digit) in easy_digits:
                decoding[easy_digits[len(digit)]] = set(digit)
        for digit in val[0] + val[1]:
            digit_set = set(digit)
            if len(digit_set) == 5:
                if digit_set.issubset(decoding[8]) and decoding[1].issubset(digit_set):
                    decoding[3] = digit_set
                elif decoding[8].difference(decoding[4]).issubset(digit_set):
                    decoding[2] = digit_set
                else:
                    decoding[5] = digit_set
            if len(digit_set) == 6:
                if decoding[7].issubset(digit_set) and decoding[4].issubset(digit_set):
                    decoding[9] = digit_set
                elif decoding[1].issubset(digit_set) and digit_set.issubset(decoding[8]):
                    decoding[0] = digit_set
                else:
                    decoding[6] = digit_set
        num += int("".join([str(k[0]) for digit in val[1] for k in decoding.items() if set(digit) == k[1]]))
    return num


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 26
    assert part_2(test_input) == 61229

    my_input = read_input("input.txt")
    log(f"Part 1: {part_1(my_input)}, {timings(lambda: part_1(my_input))}")
    log(f"Part 2: {part_2(my_input)}, {timings(lambda: part_2(my_input))}")

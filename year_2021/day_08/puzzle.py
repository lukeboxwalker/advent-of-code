from timeit import timeit

easy_digits = {2: 1, 4: 4, 7: 8, 3: 7}


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(lambda x: list(map(set, x.split())), i.split(" | "))) for i in f.read().splitlines()]


def part_1(values: list) -> int:
    return sum([1 for v in values for i in v[1] if len(i) in easy_digits])


def part_2(values: list) -> int:
    num = 0
    for val in values:
        decoding = {easy_digits[len(digit)]: digit for digit in val[0] if len(digit) in easy_digits}
        for digit in val[0]:
            if len(digit) == 5:
                if digit.issubset(decoding[8]) and decoding[1].issubset(digit):
                    decoding[3] = digit
                elif decoding[8].difference(decoding[4]).issubset(digit):
                    decoding[2] = digit
                else:
                    decoding[5] = digit
            elif len(digit) == 6:
                if decoding[7].issubset(digit) and decoding[4].issubset(digit):
                    decoding[9] = digit
                elif decoding[1].issubset(digit) and digit.issubset(decoding[8]):
                    decoding[0] = digit
                else:
                    decoding[6] = digit
        num += int("".join([str(k[0]) for digit in val[1] for k in decoding.items() if digit == k[1]]))
    return num


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 26
    assert part_2(test_input) == 61229

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

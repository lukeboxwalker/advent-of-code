from timeit import timeit


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [i.replace(" ", "") for i in f.read().splitlines()]


def part_1(values: list) -> int:
    points = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}
    return sum(map(lambda x: points[x], values))


def part_2(values: list) -> int:
    points = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
    return sum(map(lambda x: points[x], values))


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 15
    assert part_2(test_input) == 12

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

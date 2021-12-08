from collections import defaultdict
from timeit import timeit


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return list(map(int, f.read().splitlines()[0].split(",")))


def solve(values: list, days: int) -> int:
    born6, born8 = defaultdict(int), defaultdict(int)
    for i in values:
        born8[i - 8] = values.count(i)
    for day in range(days):
        if day - 6 in born6:
            born6[day + 1] += born6[day - 6]
            born8[day + 1] += born6[day - 6]
        if day - 8 in born8:
            born6[day + 1] += born8[day - 8]
            born8[day + 1] += born8[day - 8]
    return sum(born8.values())


def part_1(values: list) -> int:
    return solve(values, 80)


def part_2(values: list) -> int:
    return solve(values, 256)


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 5934
    assert part_2(test_input) == 26984457539

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

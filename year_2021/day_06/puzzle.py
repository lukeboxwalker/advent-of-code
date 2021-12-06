from timeit import timeit

from setup.console import console


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return list(map(int, f.read().splitlines()[0].split(",")))


def solve(values: list, days: int) -> int:
    born6, born8 = {(i - 6): values.count(i) for i in values}, {}
    for day in range(-6, days):
        if day in born6:
            born6[day + 7] = born6[day] + born6[day + 7] if (day + 7) in born6 else born6[day]
            born8[day + 7] = born6[day] + born8[day + 7] if day + 7 in born8 else born6[day]
        if day in born8:
            born6[day + 9] = born8[day] + born6[day + 9] if (day + 9) in born6 else born8[day]
            born8[day + 9] = born8[day] + born8[day + 9] if (day + 9) in born8 else born8[day]
    return sum([born8[i] for i in born8 if i <= days]) + len(values)


def part_1(values: list) -> int:
    return solve(values, 80)


def part_2(values: list) -> int:
    return solve(values, 256)


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 5934
    assert part_2(test_input) == 26984457539

    my_input = read_input("input.txt")
    console.print(f"Part 1: {part_1(my_input)}, Timing: {timeit(lambda: part_1(my_input), number=1)}")
    console.print(f"Part 2: {part_2(my_input)}, Timing: {timeit(lambda: part_2(my_input), number=1)}")

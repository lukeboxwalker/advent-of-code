from timeit import timeit


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return list(map(int, f.read().splitlines()))


def part_1(values: list) -> int:
    return sum(map(lambda x: x[0] < x[1], zip(values[:-1], values[1:])))


def part_2(values: list) -> int:
    return part_1(list(map(sum, zip(values[:-2], values[1:-1], values[2:]))))


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 7
    assert part_2(test_input) == 5

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

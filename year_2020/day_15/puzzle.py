def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [int(i) for i in f.read().splitlines()]


def solve(values: list, stop: int) -> int:
    cache = dict()
    for i in range(len(values) - 1):
        cache[values[i]] = i
    current = values[-1]
    for i in range(len(values), stop):
        if current in cache:
            next_current = i - cache[current] - 1
            cache[current] = i - 1
            current = next_current
        else:
            cache[current] = i - 1
            current = 0
    return current


def part_1(values: list) -> int:
    return solve(values, 2020)


def part_2(values: list) -> int:
    return solve(values, 30000000)


if __name__ == '__main__':
    assert part_1([0, 3, 6]) == 436

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

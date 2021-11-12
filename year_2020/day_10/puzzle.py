def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        values = sorted([int(line) for line in f.read().splitlines()])
        return [0] + values + [values[-1] + 3]


def part_1(values: list) -> int:
    result = [b - a for (a, b) in zip(values, values[1:])]
    return result.count(1) * result.count(3)


def part_2(values: list) -> int:
    poss_ways = [1] + [0] * values[-1]
    for i in values[1:]:
        poss_ways[i] = poss_ways[i - 1] + poss_ways[i - 2] + poss_ways[i - 3]
    return poss_ways[-1]


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 220
    assert part_2(test_input) == 19208

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        values = [int(line) for line in f.read().splitlines()]
        values.sort()
        return [0] + values + [values[-1] + 3]


def part_1(values: list) -> int:
    result = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    return result.count(1) * result.count(3)


def count_ways(value_set: set, current: int, possible_ways: dict):
    if current in possible_ways:
        return possible_ways[current]
    possible_ways_for_current = 0
    for next_current in range(current + 1, current + 4):
        if next_current in value_set:
            possible_ways_for_current += count_ways(value_set, next_current, possible_ways)
    possible_ways[current] = possible_ways_for_current
    return possible_ways_for_current


def part_2(values: list) -> int:
    return count_ways(set(values), 0, {values[-1]: 1})


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 220
    assert part_2(test_input) == 19208

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        values = [int(line) for line in f.read().splitlines()]
        values.sort()
        return [0] + values + [values[-1] + 3]


def part_1(values: list) -> int:
    result = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    return result.count(1) * result.count(3)


def count_ways(values: list, cur: int, cache: dict):
    if cur in cache:
        return cache[cur]
    cache[cur] = sum([count_ways(values, next, cache) for next in range(cur + 1, cur + 4) if next in values])
    return cache[cur]


def part_2(values: list) -> int:
    return count_ways(values, 0, {values[-1]: 1})


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 220
    assert part_2(test_input) == 19208

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

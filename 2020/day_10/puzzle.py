def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        values = [int(line) for line in f.read().splitlines()]
        values.sort()
        return [0] + values + [values[len(values) - 1] + 3]


def part_1(values: list) -> int:
    result = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    return result.count(1) * result.count(3)


# stupid solution...
def part_2(values: list) -> int:
    s = "".join([str(sum(j < len(values) and values[j] - 3 <= values[i] for j in range(i + 1, i + 4))) for i in
                 range(len(values))]).replace("332", "7").replace("32", "4").replace("1", "").replace("0", "")
    prod = 1
    for c in s:
        prod *= int(c)
    return prod


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 220
    assert part_2(test_input) == 19208

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

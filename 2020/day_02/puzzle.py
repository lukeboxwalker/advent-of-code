def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [(s[0].split('-'), s[1][0], s[2]) for s in [line.split() for line in f]]


def part_1(values: list) -> int:
    return sum(1 for data in values if int(data[0][0]) <= data[2].count(data[1]) <= int(data[0][1]))


def part_2(values: list) -> int:
    return sum(1 for d in values if (d[2][int(d[0][0]) - 1] == d[1]) ^ (d[2][int(d[0][1]) - 1] == d[1]))


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 2
    assert part_2(test_input) == 1

    my_input = read_input("input.txt")
    print("Puzzle 1:", part_1(my_input))
    print("Puzzle 2:", part_2(my_input))

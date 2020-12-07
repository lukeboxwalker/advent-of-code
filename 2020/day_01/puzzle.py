def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().splitlines()


def part_1(values: list) -> int:
    for i in range(len(values)):
        for j in range(i, len(values)):
            if int(values[i]) + int(values[j]) == 2020:
                return int(values[i]) * int(values[j])


def part_2(values: list) -> int:
    for i in range(len(values)):
        for j in range(i, len(values)):
            for k in range(j, len(values)):
                if int(values[i]) + int(values[j]) + int(values[k]) == 2020:
                    return int(values[i]) * int(values[j]) * int(values[k])


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 514579
    assert part_2(test_input) == 241861950

    my_input = read_input("input.txt")
    print("Puzzle 1:", part_1(my_input))
    print("Puzzle 2:", part_2(my_input))

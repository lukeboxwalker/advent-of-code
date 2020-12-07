def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [d.replace("\n", " ") for d in f.read().split("\n\n")]


def part_1(values: list) -> int:
    return sum(len(set(val.replace(" ", ""))) for val in values)


def part_2(values: list) -> int:
    result = 0
    for i in range(len(values)):
        for char in [set(val.replace(" ", "")) for val in values][i]:
            count = 0
            for c in values[i]:
                if c == char:
                    count += 1
            if count == len(values[i].split()):
                result += 1
    return result


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 11
    assert part_2(test_input) == 6

    my_input = read_input("input.txt")
    print("Puzzle 1:", part_1(my_input))
    print("Puzzle 2:", part_2(my_input))

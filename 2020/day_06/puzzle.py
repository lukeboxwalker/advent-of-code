def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [d.replace("\n", " ") for d in f.read().split("\n\n")]


def part_1(values: list) -> int:
    return sum(len(set(val.replace(" ", ""))) for val in values)


def part_2(values: list) -> int:
    val_set = [set(v.replace(" ", "")) for v in values]
    return sum(sum(1 for c in val_set[i] if values[i].count(c) == len(values[i].split())) for i in range(len(values)))


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 11
    assert part_2(test_input) == 6

    my_input = read_input("input.txt")
    print("Puzzle 1:", part_1(my_input))
    print("Puzzle 2:", part_2(my_input))

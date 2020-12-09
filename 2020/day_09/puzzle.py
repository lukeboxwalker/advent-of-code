def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [int(line) for line in f.read().splitlines()]


def is_sum_of_previous(values: list, preamble_length: int, index: int) -> bool:
    for i in range(index - preamble_length, index):
        for j in range(i + 1, index):
            if int(values[i]) + int(values[j]) == values[index]:
                return True
    return False


def part_1(values: list, preamble_length: int) -> int:
    for i in range(preamble_length, len(values)):
        if not is_sum_of_previous(values, preamble_length, i):
            return values[i]


def sum_to_invalid(values: list, invalid: int) -> list:
    val_len = len(values)
    result = []
    for i in range(val_len):
        result.append(values[i])
        for j in range(i + 1, val_len):
            result.append(values[j])
            if sum(result) == invalid:
                return result
        result = []
    return result


def part_2(values: list, invalid: int) -> int:
    numbers = sum_to_invalid(values, invalid)
    return min(numbers) + max(numbers)


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input, 5) == 127
    assert part_2(test_input, 127) == 62

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input, 25))
    print("Part 2:", part_2(my_input, 18272118))

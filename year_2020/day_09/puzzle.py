def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [int(line) for line in f.read().splitlines()]


def read_extra_input(filename: str) -> list:
    return read_input(filename)


def is_sum_of_previous(values: list, preamble_length: int, index: int) -> bool:
    for i in range(index - preamble_length, index):
        for j in range(i + 1, index):
            if int(values[i]) + int(values[j]) == values[index]:
                return True
    return False


def part_1(values: list, extra: list) -> int:
    preamble_length = extra[0]
    for i in range(preamble_length, len(values)):
        if not is_sum_of_previous(values, preamble_length, i):
            return values[i]


def sum_to_invalid(values: list, part_1_solution: int) -> list:
    for i in range(len(values)):
        result = [values[i]]
        result_sum = values[i]
        j = i + 1
        while j < len(values) - 1:
            result.append(values[j])
            result_sum += values[j]
            if result_sum > part_1_solution:
                j = len(values)
            elif result_sum == part_1_solution:
                return result
            j += 1
    return []


def part_2(values: list, extra: list) -> int:
    invalid = extra[1]
    numbers = sum_to_invalid(values, invalid)
    return min(numbers) + max(numbers)


if __name__ == '__main__':
    test_input = read_input("test.txt")
    text_extra_input = read_extra_input("extra_test.txt")
    assert part_1(test_input, text_extra_input) == 127
    assert part_2(test_input, text_extra_input) == 62

    my_input = read_input("input.txt")
    my_extra_input = read_extra_input("extra_input.txt")
    print("Part 1:", part_1(my_input, my_extra_input))
    print("Part 2:", part_2(my_input, my_extra_input))

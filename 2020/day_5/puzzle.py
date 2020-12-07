def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [line.replace("\n", "") for line in f]


def div_str(string: str, highest: int) -> int:
    lower = 0
    upper = highest
    for char in string:
        if char == 'B' or char == 'R':
            if lower + 1 == upper:
                return upper
            lower = lower + int(round((upper - lower) / 2))
        if char == 'F' or char == 'L':
            if lower + 1 == upper:
                return lower
            upper = upper - int(round((upper - lower) / 2))


def part_1(values: list) -> int:
    return max(div_str(val[0:7], 127) * 8 + div_str(val[7:10], 7) for val in values)


def part_2(values: list) -> int:
    seat_ids = [div_str(v[0:7], 127) * 8 + div_str(v[7:10], 7) for v in values if div_str(v[0:7], 127) != 127 != 0]
    for i in range(len(seat_ids)):
        for j in range(i, len(seat_ids)):
            if seat_ids[i] + 2 == seat_ids[j] and seat_ids[i] + 1 not in seat_ids:
                return seat_ids[i] + 1
            elif seat_ids[i] - 2 == seat_ids[j] and seat_ids[i] - 1 not in seat_ids:
                return seat_ids[i] - 1


if __name__ == '__main__':
    assert part_1(read_input("test.txt")) == 820

    my_input = read_input("input.txt")
    print("Puzzle 1:", part_1(my_input))
    print("Puzzle 2:", part_2(my_input))

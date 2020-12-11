import itertools

neighbors = [i for i in itertools.permutations([-1, 0, 1], 2)] + [i for i in zip([-1, 1], [-1, 1])]


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(line) for line in f.read().splitlines()]


def count_seats_part_1(seats: list, x: int, y: int, size: int):
    count = 0
    for dx, dy in neighbors:
        off_x = dx + x
        off_y = dy + y
        if size > off_x >= 0 and size > off_y >= 0 and seats[off_x][off_y] == "#":
            count += 1
    return count


def is_seat_used(seats: list, direction: tuple, position: tuple, size: int):
    dx = direction[0] + position[0]
    dy = direction[1] + position[1]
    if (size <= dy or dy < 0) or (size <= dx or dx < 0):
        return False
    elif seats[dx][dy] == "#":
        return True
    elif seats[dx][dy] == "L":
        return False
    else:
        return is_seat_used(seats, direction, (dx, dy), size)


def count_seats_part_2(seats: list, x: int, y: int, size: int):
    count = 0
    for dx, dy in neighbors:
        if is_seat_used(seats, (dx, dy), (x, y), size):
            count += 1

    return count


def seat_iteration(seats: list, size: int, max_n: int, count_seats) -> list:
    updated_seats = []
    for x in range(size):
        row = []
        for y in range(size):
            if seats[x][y] == ".":
                row.append(".")
                continue
            count = count_seats(seats, x, y, size)
            if count == 0:
                row.append("#")
            elif count >= max_n:
                row.append("L")
            else:
                row.append(seats[x][y])
        updated_seats.append(row)
    return updated_seats


def update_seats(seats: list, size: int, max_n: int, count_seats) -> list:
    updated_seats = seat_iteration(seats, size, max_n, count_seats)
    if updated_seats == seats:
        return updated_seats
    else:
        return update_seats(updated_seats, size, max_n, count_seats)


def part_1(values: list) -> int:
    stabilizes_seats = update_seats(values, len(values), 4, count_seats_part_1)
    return sum(line.count("#") for line in stabilizes_seats)


def part_2(values: list) -> int:
    stabilizes_seats = update_seats(values, len(values), 5, count_seats_part_2)
    return sum(line.count("#") for line in stabilizes_seats)


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 37
    assert part_2(test_input) == 26

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

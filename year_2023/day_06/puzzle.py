from aoc.api import *


def read_input(filename: str) -> list:
    return FileStream(filename).list()


# divide an conquer
def possible_ways_to_win(race_time, distance):
    pivot_max = race_time
    pivot_min = 0
    pivot = round(race_time / 2)
    while True:
        if pivot * (race_time - pivot) > distance:
            pivot_max = pivot
            if (pivot - 1) * (race_time - pivot + 1) <= distance:
                return race_time - 2 * pivot + 1
            pivot = pivot_min + round((pivot_max - pivot_min) / 2)
            continue
        else:
            pivot_min = pivot
            pivot = pivot_min + round((pivot_max - pivot_min) / 2)
            continue


def part_1(values: list) -> int:
    race_times = list(map(int, values[0].split()[1:]))
    race_distances = list(map(int, values[1].split()[1:]))
    return prod([possible_ways_to_win(race_times[i], race_distances[i]) for i in range(len(race_times))])


def part_2(values: list) -> int:
    race_time = int("".join(values[0].split()[1:]))
    race_distance = int("".join(values[1].split()[1:]))
    return possible_ways_to_win(race_time, race_distance)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 288
    assert part_2(read_input("test_input.txt")) == 71503

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

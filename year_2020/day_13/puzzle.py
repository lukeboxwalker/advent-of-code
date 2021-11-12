from typing import Tuple


def read_input(filename: str) -> [int, list]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        return int(lines[0]), [int(i.replace("x", "0")) for i in lines[1].split(",")]


def part_1(values: Tuple) -> int:
    depart_time, bus_ids = values
    timestamp = 0
    while True:
        timestamp += 1
        for i in range(len(bus_ids)):
            if bus_ids[i] * timestamp >= depart_time:
                return (bus_ids[i] * timestamp - depart_time) * bus_ids[i]


def part_2(values: Tuple) -> int:
    bus_ids = values[1]
    bus_map = dict((i, bus_ids[i]) for i in range(len(bus_ids)) if bus_ids[i] != 0)
    timestamp = 1
    step = 1
    for i in bus_map:
        while (timestamp + i) % bus_map[i] != 0:
            timestamp += step
        step *= bus_map[i]
    return timestamp


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 295
    assert part_2(test_input) == 1068781

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

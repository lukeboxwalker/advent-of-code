import numpy as np


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [(line[0], int(line[1:])) for line in f.read().splitlines()]


def part_1(values: list) -> int:
    rotations = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    rotation_idx = 0
    east_west = 0
    north_south = 0
    for i in values:
        if i[0] == "F":
            east_west += rotations[rotation_idx][0] * i[1]
            north_south += rotations[rotation_idx][1] * i[1]
        elif i[0] == "N":
            north_south += i[1]
        elif i[0] == "S":
            north_south -= i[1]
        elif i[0] == "E":
            east_west += i[1]
        elif i[0] == "W":
            east_west -= i[1]
        elif i[0] == "R":
            rotation_idx = (rotation_idx + int(i[1] / 90)) % 4
        elif i[0] == "L":
            idx = (rotation_idx - int(i[1] / 90))
            rotation_idx = (idx + 4) % 4 if idx < 0 else idx
    return abs(east_west) + abs(north_south)


def part_2(values: list) -> int:
    way_point = np.array([10, 1])
    ship_pos = np.array([0, 0])
    for i in values:
        if i[0] == "F":
            ship_pos = np.rint(ship_pos + i[1] * way_point)
        elif i[0] == "N":
            way_point = np.rint(way_point + np.array([0., i[1]]))
        elif i[0] == "S":
            way_point = np.rint(way_point - np.array([0., i[1]]))
        elif i[0] == "E":
            way_point = np.rint(way_point + np.array([i[1], 0.]))
        elif i[0] == "W":
            way_point = np.rint(way_point - np.array([i[1], 0.]))
        else:
            rad = 0
            if i[0] == "R":
                rad = np.deg2rad(i[1])
            elif i[0] == "L":
                rad = np.deg2rad(-i[1])
            c, s = np.cos(rad), np.sin(rad)
            r = np.array([[c, s],
                          [-s, c]])
            way_point = np.rint(np.dot(r, way_point))
    return int(abs(ship_pos[0]) + abs(ship_pos[1]))


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 25
    assert part_2(test_input) == 286

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))


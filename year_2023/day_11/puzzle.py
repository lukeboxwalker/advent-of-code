from aoc.api import *

def read_input(filename: str) -> list:
    return FileStream(filename).list()

def get_galaxies(values: list, expand):
    rows = []
    cols = []
    nodes = []
    for i in range(len(values)):
        rows.append(i)
        cols.append(i)
        for j in range(len(values[i])):
            if values[i][j] != ".":
                nodes.append([i, j])
                if i in rows:
                    rows.remove(i)
            if values[j][i] != "." and i in cols:
                cols.remove(i)
    for i in range(len(rows)):
        for node in nodes:
            if node[0] > rows[i] + i * expand:
                node[0] += expand
    for i in range(len(cols)):
        for node in nodes:
            if node[1] > cols[i] + i * expand:
                node[1] += expand
    return nodes

def sum_galaxy_distances(nodes):
    result = 0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes), 1):
            dist = abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])
            result += dist
    return result

def part_1(values: list) -> int:
    return sum_galaxy_distances(get_galaxies(values, 1))


def part_2(values: list) -> int:
    return sum_galaxy_distances(get_galaxies(values, 999_999))


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 374
    assert part_2(read_input("test_input.txt")) == 82000210

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

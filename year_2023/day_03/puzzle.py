from itertools import chain
from aoc.api import *


def read_input(filename: str) -> dict:
    return get_all_symbols_with_neighbors(FileStream(filename).list())

def get_neighbors(lines, row, j1, j2, num):
    neighbors = dict()
    for ix in range(row - 1, row + 2):
        # bounce check
        if ix < 0 or ix > len(lines) - 1:
            continue
        line = lines[ix]
        for jx in range(j1 - 1, j2 + 2):
            # skip number
            if ix == row and j1 <= jx <= j2:
                continue
            # check symbol and bounce
            if len(line) > jx > -1 and line[jx] != ".":
                neighbors[(ix, jx)] = (line[jx], [num])
    return neighbors

def get_all_symbols_with_neighbors(values: list) -> dict:
    symbols = dict()
    for row in range(len(values)):
        line = values[row]
        i_iter = Foreach(len(line))
        for i in iter(i_iter):
            j_iter = Foreach(len(line), start=i)
            for j in iter(j_iter):
                # check if new digit found in line
                if (j + 1 >= len(line) or not str.isdigit(line[j + 1])) and str.isdigit(line[i:j + 1]):
                    neighbor_symbols = get_neighbors(values, row, i, j, int(line[i:j + 1]))
                    # add symbols to dict
                    for key in neighbor_symbols:
                        if key not in symbols:
                            symbols[key] = neighbor_symbols[key]
                        else:
                            symbols[key][1].extend(neighbor_symbols[key][1])
                    i_iter.set(j + 1)
                    j_iter.break_iteration()
    return symbols

def part_1(values: dict) -> int:
    return sum(chain.from_iterable([values[s][1] for s in values]))


def part_2(values: dict) -> int:
    return sum([prod(values[s][1]) for s in values if values[s][0] == "*" and len(values[s][1]) == 2])


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 4361
    assert part_2(test_input) == 467835

    my_input = read_input("input.txt")
    print("Part 1:", format_solution(lambda: part_1(my_input)))
    print("Part 2:", format_solution(lambda: part_2(my_input)))

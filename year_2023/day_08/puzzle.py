import math

from aoc.api import *


def read_input(filename: str) -> tuple:
    lines = FileStream(filename).list()
    left_right = lines[0]
    graph = dict()
    for line in lines[2:]:
        node = line.split(" = ")
        children = node[1].split(", ")
        graph[node[0]] = children[0][1:], children[1][:-1],
    return list(left_right), graph

def make_step(values, current):
    direction = values[0].pop(0)
    values[0].append(direction)
    if direction == "L":
        return values[1][current][0]
    else:
        return values[1][current][1]


def count_steps(values: tuple, start, ends) -> tuple:
    current = make_step(values, start)
    steps = 1
    while current not in ends:
        current = make_step(values, current)
        steps += 1
    return steps, current

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0

def n_lcm(numbers):
    lcm_result = lcm(numbers[0], numbers[1])
    for num in numbers[2:]:
        lcm_result = lcm(lcm_result, num)
    return lcm_result

def part_1(values: tuple) -> int:
    return count_steps(values, "AAA", {"ZZZ"})[0]

def part_2(values: tuple) -> int:
    ends = {i for i in values[1] if i.endswith("Z")}
    start_pos = [i for i in values[1] if i.endswith("A")]
    steps = []
    for start in start_pos:
        steps.append(count_steps(values, start, ends)[0])
    return n_lcm(steps)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 2
    assert part_2(read_input("test_input_part2.txt")) == 6

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

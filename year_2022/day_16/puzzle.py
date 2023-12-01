import itertools
from collections import defaultdict

import numpy as np

from aoc.api import *
import re

class Valve:

    def __init__(self, name, rate, neighbors):
        self.name = name
        self.rate = rate
        self.idx = 0
        self.neighbors = neighbors
        self.connections = {name: 0}

    def __str__(self) -> str:
        return f"{self.name}, {self.rate}, {self.idx}, {self.connections}"


def read_input(filename: str) -> dict:
    valves = dict()
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            name = line.split("Valve ")[1][:2]
            rate = int(line.split("=")[1].split(";")[0])
            neighbors = re.split("valve |valves ", line)[1].split(", ")
            valves[name] = Valve(name, rate, neighbors)
    for name in valves:
        min_distance_valve(valves[name].connections, valves, valves[name].neighbors, 1)
    for name in list(valves.keys()):
        for connection in list(valves[name].connections.keys()):
            if connection not in valves or valves[connection].rate == 0 or valves[name].connections[connection] == 0:
                valves[name].connections.pop(connection)
        if valves[name].rate == 0 and name != "AA":
            valves.pop(name)
    keys = list(valves.keys())
    for i in range(len(keys)):
        valves[keys[i]].idx = 0x1 << i
    return valves

def min_distance_valve(connections, valves, neighbors, distance):
    for neighbor in neighbors:
        if neighbor not in connections or connections[neighbor] > distance:
            connections[neighbor] = distance
            min_distance_valve(connections, valves, valves[neighbor].neighbors, distance + 1)

def part_1(valves: dict) -> int:
    return depth_search(valves, "AA", 0, 30, dict())

def part_2(valves: dict) -> int:
    depth_cache = dict()
    max_release = 0
    size = len(valves)
    for closed_valves in range(2**size // 2):
        closed_valves_elephant = closed_valves ^ (2 ** size - 1)
        combination_release = depth_search(valves, "AA", closed_valves, 26, depth_cache) + depth_search(valves, "AA", closed_valves_elephant, 26, depth_cache)
        if combination_release > max_release:
            max_release = combination_release
            continue
    return max_release

def depth_search(valves: dict, current_valve: str, closed_valves: int, minute: int, cache: dict):
    if minute <= 0:
        return 0
    cache_key = (current_valve, closed_valves, minute)
    if cache_key in cache:
        return cache[cache_key]
    release_over_time = valves[current_valve].rate * minute
    release_over_time_from_neighbor = 0
    for neighbor_valve, distance in valves[current_valve].connections.items():
        if valves[neighbor_valve].idx & closed_valves != 0:
            continue
        if distance > minute:
            continue
        minute_at_neighbor = minute - distance - 1
        release_over_time_from_current_neighbor = depth_search(valves, neighbor_valve, closed_valves | valves[current_valve].idx, minute_at_neighbor, cache)
        if release_over_time_from_current_neighbor > release_over_time_from_neighbor:
            release_over_time_from_neighbor = release_over_time_from_current_neighbor
    cache[cache_key] = release_over_time + release_over_time_from_neighbor
    return cache[cache_key]


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 1651
    assert part_2(read_input("test_input.txt")) == 1707

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

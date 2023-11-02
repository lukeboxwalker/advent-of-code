import itertools
from collections import defaultdict

import numpy as np

from aoc.api import *
import re

class Valve:

    def __init__(self, name, rate, neighbors):
        self.name = name
        self.rate = rate
        self.neighbors = neighbors
        self.connections = {name: 0}

    def __str__(self) -> str:
        return f"{self.name}, {self.rate}, {self.connections}"


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
    return valves

def min_distance_valve(connections, valves, neighbors, distance):
    for neighbor in neighbors:
        if neighbor not in connections or connections[neighbor] > distance:
            connections[neighbor] = distance
            min_distance_valve(connections, valves, valves[neighbor].neighbors, distance + 1)

def part_1(valves: dict) -> int:
    return depth_search(valves, "AA", set(), 30, dict())

def part_2(valves: dict) -> int:
    combination_cache = dict()
    depth_cache = dict()
    max_release = 0
    for subset in itertools.chain.from_iterable(itertools.combinations(valves.keys(), r) for r in range(len(valves) + 1)):
        valves_elephant = set(subset)
        valves_me = set(valves.keys()) - valves_elephant
        combination_key = (tuple(sorted(list(valves_elephant))), tuple(sorted(list(valves_me))))
        if len(valves_me) > len(valves_elephant):
            combination_key = (tuple(sorted(list(valves_me))), tuple(sorted(list(valves_elephant))))
        if combination_key in combination_cache:
            if combination_cache[combination_key] > max_release:
                max_release = combination_cache[combination_key]
            continue
        combination_release = depth_search(valves, "AA", valves_elephant, 26, depth_cache) + depth_search(valves, "AA", valves_me, 26, depth_cache)
        if combination_release > max_release:
            combination_cache[combination_key] = combination_release
            max_release = combination_release
            continue
    return max_release


def depth_search(valves: dict, current_valve: str, closed_valves: set, minute: int, cache: dict):
    if minute <= 0:
        return 0
    cache_key = (current_valve, tuple(sorted(list(closed_valves))), minute)
    if cache_key in cache:
        return cache[cache_key]
    release_over_time = valves[current_valve].rate * minute
    release_over_time_from_neighbor = 0
    for neighbor_valve, distance in valves[current_valve].connections.items():
        if neighbor_valve in closed_valves:
            continue
        if distance > minute:
            continue
        closed_valves_at_neighbor = set(closed_valves)
        closed_valves_at_neighbor.add(current_valve)
        minute_at_neighbor = minute - distance - 1
        release_over_time_from_current_neighbor = depth_search(valves, neighbor_valve, closed_valves_at_neighbor, minute_at_neighbor, cache)
        if release_over_time_from_current_neighbor > release_over_time_from_neighbor:
            release_over_time_from_neighbor = release_over_time_from_current_neighbor
    cache[cache_key] = release_over_time + release_over_time_from_neighbor
    return cache[cache_key]


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 1651
    assert part_2(read_input("test_input.txt")) == 1707

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

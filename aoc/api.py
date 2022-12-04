from __future__ import annotations

import sys
from collections import Callable
from timeit import timeit
from typing import List


def print_solution(part_1, part_2):
    print(str(sys.argv[0].split("puzzle.py")[0]) + "solution.txt")
    solution_1 = part_1()
    solution_2 = part_2()
    with open(str(sys.argv[0].split("puzzle.py")[0]) + "solution.txt", "w") as f:
        f.write("Part 1: " + str(solution_1) + "\nPart 2: " + str(solution_2))
    print(f"Part 1: {solution_1}, Timing: %.2f ms" % (1000 * timeit(part_1, number=1)))
    print(f"Part 2: {solution_2}, Timing: %.2f ms" % (1000 * timeit(part_2, number=1)))

class String:

    @staticmethod
    def split(separator: str):
        return lambda x: x.split(separator)


class Stream:

    def __init__(self, array: List):
        self.array = array

    def map_in_stream(self):
        return self.map(lambda x: Stream(x))

    def map(self, mapper: Callable | MapStream):
        if isinstance(mapper, MapStream):
            return Stream(list(map(mapper.callable(), self.array)))
        return Stream(list(map(mapper, self.array)))

    def list(self):
        return self.array

    def sum(self):
        return sum(self.list())

class MapStream(Stream):

    def __init__(self, mapper: Callable):
        super().__init__([])
        self.mapper = mapper

    @staticmethod
    def split(separator):
        return MapStream(String.split(separator))

    def map(self, mapper: Callable | MapStream):
        if isinstance(mapper, MapStream):
            return MapStream(lambda x: list(map(mapper.callable(), self.mapper(x))))
        return MapStream(lambda x: list(map(mapper, self.mapper(x))))

    def list(self):
        raise NotImplemented

    def callable(self):
        return self.mapper


class FileStream(Stream):

    def __init__(self, filename: str):
        with open(filename, "r") as f:
            super().__init__(f.read().splitlines())




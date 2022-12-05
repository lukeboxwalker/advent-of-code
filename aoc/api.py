from __future__ import annotations

import sys
from functools import reduce
from timeit import timeit
from typing import List, Callable


def print_solution(part_1, part_2):
    print(str(sys.argv[0].split("puzzle.py")[0]) + "solution.txt")
    solution_1 = part_1()
    solution_2 = part_2()
    with open(str(sys.argv[0].split("puzzle.py")[0]) + "solution.txt", "w") as f:
        f.write("Part 1: " + str(solution_1) + "\nPart 2: " + str(solution_2))
    print(f"Part 1: {solution_1}, Timing: %.2f ms" % (1000 * timeit(part_1, number=1)))
    print(f"Part 2: {solution_2}, Timing: %.2f ms" % (1000 * timeit(part_2, number=1)))

class Set:

    @staticmethod
    def union(a: set, b: set):
        return a | b

    @staticmethod
    def intersection(a: set, b: set):
        return a & b

    @staticmethod
    def pop(a: set):
        return a.pop()

class String:

    @staticmethod
    def isdigit(string: str):
        return string.isdigit()

    @staticmethod
    def split(separator: str):
        return lambda x: x.split(separator)

    @staticmethod
    def replace(sequence: str, replace: str):
        return lambda x: x.replace(sequence, replace)

    @staticmethod
    def divide(string: str):
        return [string[:len(string) // 2], string[len(string) // 2:]]

class Tuple:

    def __init__(self, array):
        self.x = array[0]
        self.y = array[1]

    def __repr__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class IntTuple(Tuple):

    def __init__(self, array):
        super().__init__(array)

    @staticmethod
    def overlap_other(tuple: Tuple):
        return tuple.x.overlap(tuple.y) or tuple.y.overlap(tuple.x)

    @staticmethod
    def include_other(tuple: Tuple):
        return tuple.x.include(tuple.y) or tuple.y.include(tuple.x)

    def overlap(self, int_tuple: IntTuple):
        return int_tuple.y >= self.y >= int_tuple.x

    def include(self, int_tuple: IntTuple):
        return int_tuple.x >= self.x and int_tuple.y <= self.y

class Stream:

    def __init__(self, array: List):
        self.array = array

    def map(self, mapper: Callable | MapStream):
        if isinstance(mapper, MapStream):
            return Stream(list(map(mapper.callable(), self.array)))
        return Stream(list(map(mapper, self.array)))

    def list(self):
        return self.array

    def sum(self):
        return sum(self.list())

    def reduce(self, reducer: Callable):
        return reduce(reducer, self.list())

    def group(self, size: int):
        return Stream([self.array[i:i + size] for i in range(0, len(self.array), size)])

    def max(self):
        return max(self.list())

    def sorted(self):
        return Stream(sorted(self.array))

    def last(self, amount: int):
        return Stream(self.array[-amount:])

    def first(self, amount: int):
        return Stream(self.array[:amount])

    def filter(self, predicate: Callable):
        return Stream(list(filter(predicate, self.array)))

class MapStream(Stream):

    def __init__(self, mapper=lambda x: x):
        super().__init__([])
        self.mapper = mapper

    @staticmethod
    def split(separator):
        return MapStream(String.split(separator))

    def to(self, factory: Callable):
        return MapStream(lambda x: factory(self.mapper(x)))

    def map(self, mapper: Callable | MapStream):
        if isinstance(mapper, MapStream):
            return MapStream(lambda x: list(map(mapper.callable(), self.mapper(x))))
        return MapStream(lambda x: list(map(mapper, self.mapper(x))))

    def list(self):
        raise NotImplemented

    def callable(self):
        return self.mapper

    def reduce(self, reducer: Callable):
        return lambda x: reduce(reducer, self.mapper(x))

    def max(self):
        return MapStream(lambda x: max(self.mapper(x)))

    def sorted(self):
        return MapStream(lambda x: sorted(self.mapper(x)))

    def last(self, amount: int):
        return MapStream(lambda x: self.mapper(x)[-amount:])

    def first(self, amount: int):
        return MapStream(lambda x: self.mapper(x)[:amount])

    def filter(self, predicate: Callable):
        return MapStream(lambda x: (list(filter(predicate, self.mapper(x)))))

class FileStream(Stream):

    def __init__(self, filename: str, separator=None):
        with open(filename, "r") as f:
            if separator is None:
                super().__init__(f.read().splitlines())
            else:
                super().__init__(f.read().split(separator))

import time
from functools import reduce
from typing import Callable


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

    @staticmethod
    def concat(separator=""):
        return lambda a, b: a + separator + b

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

    def overlap(self, int_tuple):
        return int_tuple.y >= self.y >= int_tuple.x

    def include(self, int_tuple):
        return int_tuple.x >= self.x and int_tuple.y <= self.y

class Stream:

    def __init__(self, array):
        self.array = array

    @staticmethod
    def split(separator):
        return MapStream(String.split(separator))

    def map(self, mapper):
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

    def min(self):
        return min(self.list())

    def sorted(self):
        return Stream(sorted(self.array))

    def reversed(self):
        return Stream(list(reversed(self.array)))

    def last(self, amount: int):
        return Stream(self.array[-amount:])

    def first(self, amount: int):
        return Stream(self.array[:amount])

    def filter(self, predicate: Callable):
        return Stream(list(filter(predicate, self.array)))

    def count(self):
        return len(self.list())

    def foreach(self, consumer: Callable):
        for i in self.list():
            consumer(i)

class MapStream(Stream):

    def __init__(self, mapper=lambda x: x):
        super().__init__([])
        self.mapper = mapper

    def to(self, factory: Callable):
        return MapStream(lambda x: factory(self.mapper(x)))

    def map(self, mapper):
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

    def reversed(self):
        return MapStream(lambda x: list(reversed(self.mapper(x))))

    def last(self, amount: int):
        return MapStream(lambda x: self.mapper(x)[-amount:])

    def first(self, amount: int):
        return MapStream(lambda x: self.mapper(x)[:amount])

    def filter(self, predicate: Callable):
        return MapStream(lambda x: (list(filter(predicate, self.mapper(x)))))

class IntStream(Stream):

    def __init__(self, stop, start=0, step=1):
        super().__init__(range(start, stop, step))

class FileStream(Stream):

    def __init__(self, filename: str, separator=None):
        with open(filename, "r") as f:
            if separator is None:
                super().__init__(f.read().splitlines())
            else:
                super().__init__(f.read().split(separator))


def format_solution(func: Callable):
    start = time.time()
    res = func()
    end = time.time()
    return f"{res}, Timing: %.2f ms" % (1000 * (end - start))

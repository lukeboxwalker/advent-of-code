import timeit

from rich.console import Console
from rich.theme import Theme

__console = Console(color_system="windows", theme=Theme({"repr.number": "bold green"}))


def log(msg):
    __console.print(msg)


def timings(func):
    return "Timing: %.2f ms" % (1000 * timeit.timeit(func, number=1))

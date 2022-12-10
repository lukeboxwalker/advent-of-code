from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().splitlines()


def part_1(values: list) -> int:
    cycle = 0
    rax = 1
    result = 0
    for value in values:
        if value.startswith("noop"):
            do_cycles = 1
            add_x = 0
        else:
            do_cycles = 2
            add_x = int(value.split(" ")[1])
        for _ in range(do_cycles):
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                result += rax * cycle
        rax += add_x
    return result


def part_2(values: list) -> str:
    cycle = 0
    rax = 1
    result = list("." * 240)
    for value in values:
        if value.startswith("noop"):
            do_cycles = 1
            add_x = 0
        else:
            do_cycles = 2
            add_x = int(value.split(" ")[1])
        for i in range(do_cycles):
            if rax + 2 > cycle % 40 > rax - 2:
                result[cycle] = "#"
            cycle += 1
        rax += add_x
    return "\n" + Stream(result).group(40).map(
        lambda x: Stream(x).reduce(String.concat(""))
    ).reduce(String.concat("\n")) + "\n"


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 13140
    assert part_2(test_input) == "\n##..##..##..##..##..##..##..##..##..##..\n" \
           + "###...###...###...###...###...###...###.\n" \
           + "####....####....####....####....####....\n" \
           + "#####.....#####.....#####.....#####.....\n" \
           + "######......######......######......####\n" \
           + "#######.......#######.......#######.....\n"

my_input = read_input("input.txt")
print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

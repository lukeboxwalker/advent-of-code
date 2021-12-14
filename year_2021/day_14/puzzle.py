from timeit import timeit
import re


def read_input(filename: str) -> tuple:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        pairs = {}
        for pair in map(lambda x: x.split(" -> "), lines[2:]):
            pairs[pair[0]] = pair[1]
        return lines[0], pairs


def solve(values: tuple, n: int):
    pair_count = {pair: len(re.findall(pair, values[0])) for pair in values[1]}
    letter_count = {pair: len(re.findall(pair, values[0])) for pair in values[1].values()}
    for i in range(n):
        new_pair_count = {pair: 0 for pair in values[1]}
        for pair in pair_count:
            if pair_count[pair] > 0:
                letter_count[values[1][pair]] += pair_count[pair]
                first = pair[0] + values[1][pair]
                if first in new_pair_count:
                    new_pair_count[first] += pair_count[pair]
                second = values[1][pair] + pair[1]
                if second in new_pair_count:
                    new_pair_count[second] += pair_count[pair]
        pair_count = new_pair_count
    return max(letter_count.values()) - min(letter_count.values())


def part_1(values: tuple) -> int:
    return solve(values, 10)


def part_2(values: tuple) -> int:
    return solve(values, 40)


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 1588
    assert part_2(test_input) == 2188189693529

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

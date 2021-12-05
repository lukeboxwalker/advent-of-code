from timeit import timeit

from setup.console import console


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [list(map(lambda x: list(map(int, x.split(","))), i.split(" -> "))) for i in f.read().splitlines()]


def part_1(values: list) -> int:
    values = [i for i in values if i[0][0] == i[1][0] or i[0][1] == i[1][1]]
    return part_2(values)


def part_2(values: list) -> int:
    count = {}
    for i in values:
        dx = (i[1][0] - i[0][0]) // max(abs(i[1][0] - i[0][0]), abs(i[1][1] - i[0][1]))
        dy = (i[1][1] - i[0][1]) // max(abs(i[1][0] - i[0][0]), abs(i[1][1] - i[0][1]))
        vec = (i[0][0], i[0][1])
        while not (vec[0] == i[1][0] + dx and vec[1] == i[1][1] + dy):
            if vec in count:
                count[vec] += 1
            else:
                count[vec] = 1
            vec = (vec[0] + dx, vec[1] + dy)
    return sum([1 for i in count if count[i] > 1])


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 5
    assert part_2(test_input) == 12

    my_input = read_input("input.txt")
    console.print(f"Part 1: {part_1(my_input)}, Timing: {timeit(lambda: part_1(my_input), number=1)}")
    console.print(f"Part 2: {part_2(my_input)}, Timing: {timeit(lambda: part_2(my_input), number=1)}")

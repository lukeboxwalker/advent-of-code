import re
from timeit import timeit


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return list(map(int, re.findall("-?[0-9][0-9]*", f.read().splitlines()[0])))


def shoot(values: list, dx: int, dy: int) -> list:
    x, y = 0, 0
    result = [y]
    while True:
        if not (x + dx <= values[1] and y + dy >= values[2]):
            if x >= values[0] and y <= values[3]:
                return result
            else:
                return [0]
        x += dx
        y += dy
        result += [y]
        dx += -1 if dx > 0 else 0 if dx == 0 else 1
        dy -= 1

def shoot2(values: list, dx: int, dy: int) -> list:
    x, y = 0, 0
    result = [y]
    while True:
        if not (x + dx <= values[1] and y + dy >= values[2]):
            return x >= values[0] and y <= values[3]
        x += dx
        y += dy
        result += [y]
        dx += -1 if dx > 0 else 0 if dx == 0 else 1
        dy -= 1


def part_1(values: list) -> int:
    res = []
    for i in range(500):
        for j in range(1, 500):
            m = max(shoot(values, i, j))
            if m == 0 and j == 1:
                break
            res.append(m)
    return max(res)


def part_2(values: list) -> int:
    res = 0
    for i in range(500):
        for j in range(-2000, 2000):
            if shoot2(values, i, j):
                res += 1
    return res


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 45
    assert part_2(test_input) == 112

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

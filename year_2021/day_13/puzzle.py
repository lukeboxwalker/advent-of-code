from timeit import timeit

letters = {
    "52225": "O",
    "4222": "C",
    "6222": "P",
    "3333": "Z",
    "6111": "L",
    "6221": "F"
}


def read_input(filename: str) -> (list, list):
    with open(filename, "r") as f:
        lines = f.read().replace("\n", " ").replace("fold along ", "").split("  ")
        points = set(map(lambda x: tuple(map(int, x.split(","))), lines[0].split()))
        folds = list(map(lambda x: (x.split("=")[0], int(x.split("=")[1])), lines[1].split()))
        return points, folds


def fold(points: set, folding):
    for point in points.copy():
        if folding[0] == "y" and point[1] > folding[1]:
            points.remove(point)
            points.add((point[0], 2 * folding[1] - point[1]))
        elif folding[0] == "x" and point[0] > folding[1]:
            points.remove(point)
            points.add((2 * folding[1] - point[0], point[1]))
    return points


def part_1(values: tuple) -> int:
    return len(fold(values[0].copy(), values[1][0]))


def part_2(values: tuple) -> str:
    points = values[0].copy()
    for folding in values[1]:
        points = fold(points, folding)
    shape = max(points)
    nums = "".join([str(sum([1 if (i, j) in points else 0 for j in range(shape[1] + 1)])) for i in range(shape[0] + 1)])
    return "".join(map(lambda x: letters[x], nums.split("0")))


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 17
    assert part_2(test_input) == "O"

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 1: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

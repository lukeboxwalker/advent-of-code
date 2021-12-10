from timeit import timeit


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().splitlines()


def part_1(values: list) -> int:
    points = {"]": 57, ")": 3, "}": 1197, ">": 25137}
    brackets = {"]": "[", ")": "(", "}": "{", ">": "<"}
    result = 0
    for line in values:
        stack = []
        for i in line:
            if i in brackets.values():
                stack.append(i)
            elif brackets[i] != stack.pop():
                result += points[i]
                break
    return result


def part_2(values: list) -> int:
    points = {"[": 2, "(": 1, "{": 3, "<": 4}
    brackets = {"]": "[", ")": "(", "}": "{", ">": "<"}
    result = []
    for line in values:
        stack = []
        corrupted = False
        line_result = 0
        for i in line:
            if i in brackets.values():
                stack.append(i)
            elif brackets[i] != stack.pop():
                corrupted = True
                break
        if not corrupted:
            for i in stack[::-1]:
                line_result = line_result * 5 + points[i]
            result.append(line_result)
    return sorted(result)[len(result) // 2]


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 26397
    assert part_2(test_input) == 288957

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

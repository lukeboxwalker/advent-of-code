from timeit import timeit

from setup.console import console


def read_input(filename: str) -> tuple:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        numbers = list(map(int, lines[0].split(",")))
        boards = [[list(map(int, lines[j].split())) for j in range(i, i + 5)] for i in range(2, len(lines), 6)]
        return numbers, boards


def part_1(values: tuple) -> int:
    marked = [[[] for _ in range(10)] for _ in range(len(values[1]))]
    for number in values[0]:
        for idx, board in enumerate(values[1]):
            for i in range(len(board[0])):
                for j in range(len(board[0])):
                    if board[i][j] == number:
                        marked[idx][i].append(j)
                        marked[idx][j + 5].append(i)
                        if len(marked[idx][i]) == 5 or len(marked[idx][j + 5]) == 5:
                            nums = [board[i][j] for i in range(5) for j in range(5) if j not in marked[idx][i]]
                            return sum(nums) * number


def part_2(values: tuple) -> int:
    not_won = {i for i in range(len(values[1]))}
    marked = [[[] for _ in range(10)] for _ in range(len(values[1]))]
    last = None
    for number in values[0]:
        if len(not_won) == 1:
            last = next(iter(not_won))
        for idx, board in enumerate(values[1]):
            for i in range(len(board[0])):
                for j in range(len(board[0])):
                    if board[i][j] == number:
                        marked[idx][i].append(j)
                        marked[idx][j + 5].append(i)
                        if len(marked[idx][i]) == 5 or len(marked[idx][j + 5]) == 5:
                            if not_won.__contains__(idx):
                                not_won.remove(idx)
        if len(not_won) == 0:
            nums = [values[1][last][i][j] for i in range(5) for j in range(5) if j not in marked[last][i]]
            return sum(nums) * number


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 4512
    assert part_2(test_input) == 1924

    my_input = read_input("input.txt")
    console.print(f"Part 1: {part_1(my_input)}, Timing: {timeit(lambda: part_1(my_input), number=1)}")
    console.print(f"Part 2: {part_2(my_input)}, Timing: {timeit(lambda: part_2(my_input), number=1)}")

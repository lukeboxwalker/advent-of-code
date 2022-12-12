import copy

import numpy as np


class Monkey:

    def __int__(self):
        self.operation = None
        self.items = None
        self.move_true = None
        self.move_false = None
        self.test = None


operations = {
    "*": lambda a, b: a * b,
    "+": lambda a, b: a + b
}


def read_input(filename: str) -> list:
    monkeys = []
    with open(filename, "r") as f:
        strings = f.read().split("\n\n")
        for string in strings:
            split = string.split("\n")
            monkey = Monkey()
            monkey.items = list(map(int, split[1][18:].split(", ")))
            operation = split[2][23:].split(" ")
            monkey.operation = operation[0]
            monkey.operand = operation[1]
            monkey.move_true = int(split[4][29:])
            monkey.move_false = int(split[5][29:])
            monkey.test = int(split[3][21:])
            monkeys.append(monkey)
        return monkeys


def part_1(monkeys: list) -> int:
    monkeys = [copy.deepcopy(monkey) for monkey in monkeys]
    inspections = np.zeros(len(monkeys))
    for _ in range(20):
        for k, monkey in enumerate(monkeys):
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                inspections[k] += 1
                if monkey.operand == "old":
                    item = operations[monkey.operation](item, item)
                else:
                    item = operations[monkey.operation](item, int(monkey.operand))
                item = int(item / 3)
                if item % monkey.test == 0:
                    monkeys[monkey.move_true].items.append(item)
                else:
                    monkeys[monkey.move_false].items.append(item)
    nums = sorted(inspections)
    return int(nums[-1] * nums[-2])


def part_2(monkeys: list) -> int:
    monkeys = [copy.deepcopy(monkey) for monkey in monkeys]
    inspections = np.zeros(len(monkeys))
    for _ in range(10_000):
        for k, monkey in enumerate(monkeys):
            print(monkey.items)
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                inspections[k] += 1
                if monkey.operand == "old":
                    item = operations[monkey.operation](item, item)
                else:
                    item = operations[monkey.operation](item, int(monkey.operand))
                if item % monkey.test == 0:
                    monkeys[monkey.move_true].items.append(item)
                else:
                    monkeys[monkey.move_false].items.append(item)
    nums = sorted(inspections)
    return int(nums[-1] * nums[-2])


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 10605
    #assert part_2(test_input) == 0

    for i in range(100):
        print((i + 3) % 23, ((i % 23) + 3) % 23)
    #my_input = read_input("input.txt")
    #print_solution(lambda: part_1(my_input), lambda: part_1(my_input))

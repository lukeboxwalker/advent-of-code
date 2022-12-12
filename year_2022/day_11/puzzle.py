from aoc.api import format_solution


class Leaf:

    def __init__(self, value):
        self.value = value

    def modulo(self, m: int):
        return self.value % m


class Node:

    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator
        self.cache = dict()

    def modulo(self, m: int):
        if m in self.cache:
            return self.cache[m]

        left = self.left.modulo(m)
        right = self.right.modulo(m)

        value = operation(left, right, self.operator) % m
        self.cache[m] = value
        return value

def operation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "*":
        return a * b
    else:
        raise ValueError()

class Monkey:

    def __init__(self, **kwargs):
        self.items = kwargs["items"]
        self.operator = kwargs["operator"]
        self.operand = kwargs["operand"]
        self.divisor = kwargs["divisor"]
        self.throw_true = kwargs["throw_true"]
        self.throw_false = kwargs["throw_false"]
        self.inspections = 0


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        monkeys = []
        strings = f.read().split("\n\n")
        for string in strings:
            split = string.split("\n")
            operation_split = split[2][23:].split(" ")
            monkey = Monkey(
                items=list(map(lambda x: Leaf(int(x)), split[1][18:].split(", "))),
                operator=operation_split[0],
                operand=operation_split[1],
                divisor=int(split[3][21:]),
                throw_true=int(split[4][29:]),
                throw_false=int(split[5][29:])
            )
            monkeys.append(monkey)
        return monkeys


def part_1(monkeys: list) -> int:
    for _ in range(20):
        for k, monkey in enumerate(monkeys):
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.inspections += 1
                if monkey.operand == "old":
                    item = Leaf(operation(item.value, item.value, monkey.operator))
                else:
                    item = Leaf(operation(item.value, int(monkey.operand), monkey.operator))
                item = Leaf(int(item.value / 3))
                if item.value % monkey.divisor == 0:
                    monkeys[monkey.throw_true].items.append(item)
                else:
                    monkeys[monkey.throw_false].items.append(item)
    nums = sorted(monkeys, key=lambda x: x.inspections)
    return int(nums[-1].inspections * nums[-2].inspections)


def part_2(monkeys: list) -> int:
    for _ in range(10_000):
        for k, monkey in enumerate(monkeys):
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.inspections += 1
                if monkey.operand == "old":
                    item = Node(left=item, right=item, operator=monkey.operator)
                else:
                    item = Node(left=item, right=Leaf(int(monkey.operand)), operator=monkey.operator)

                if item.modulo(monkey.divisor) == 0:
                    monkeys[monkey.throw_true].items.append(item)
                else:
                    monkeys[monkey.throw_false].items.append(item)
    nums = sorted(monkeys, key=lambda x: x.inspections)
    return int(nums[-1].inspections * nums[-2].inspections)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 10605
    assert part_2(read_input("test_input.txt")) == 2713310158

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

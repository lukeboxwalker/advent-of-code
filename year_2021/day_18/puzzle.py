import itertools
from timeit import timeit

import numpy as np


class Node:

    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

    def is_leaf(self):
        return self.value is not None

    def __add__(self, other):
        return Node(left=self, right=other)

    def get_leaves(self, leaves=None) -> list:
        if leaves is None:
            leaves = []
        if self.is_leaf():
            leaves.append(self)
            return leaves
        else:
            leaves = self.left.get_leaves(leaves)
            leaves = self.right.get_leaves(leaves)
            return leaves

    def magnitude(self):
        if self.is_leaf():
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().splitlines()


def reduce(tree: Node):
    while True:
        v = explode(tree, tree.get_leaves())
        if v == 1:
            continue
        v = split(tree)
        if v == 0:
            break


def split_replace(node: Node):
    left = Node(value=int(np.floor(node.value / 2)))
    right = Node(value=int(np.ceil(node.value / 2)))
    return Node(left=left, right=right)


def split(node: Node):
    if node.is_leaf():
        if node.value >= 10:
            return 2
        else:
            return 0
    else:
        left = split(node.left)
        if left == 2:
            node.left = split_replace(node.left)
            return 1
        elif left == 1:
            return 1
        right = split(node.right)
        if right == 2:
            node.right = split_replace(node.right)
            return 1
        elif right == 1:
            return 1
    return 0


def explode(node: Node, leaves: list, depth=0):
    if node.is_leaf():
        return 0
    elif depth == 4:
        l_idx = leaves.index(node.left)
        r_idx = leaves.index(node.right)
        if 0 < l_idx:
            leaves[l_idx - 1].value += node.left.value
        if r_idx + 1 < len(leaves):
            leaves[r_idx + 1].value += node.right.value
        return 2
    else:
        left = explode(node.left, leaves, depth + 1)
        if left == 2:
            node.left = Node(value=0)
            return 1
        elif left == 1:
            return 1
        right = explode(node.right, leaves, depth + 1)
        if right == 2:
            node.right = Node(value=0)
            return 1
        elif right == 1:
            return 1
    return 0


def create_tree(string_tree):
    if string_tree.isdigit():
        return Node(value=int(string_tree))
    stack = []
    for i in range(len(string_tree)):
        if string_tree[i] == "[":
            stack.append(string_tree[i])
        elif string_tree[i] == "]":
            stack.pop()
        if i > 0 and len(stack) == 1:
            left_node = create_tree(string_tree[1:i + 1])
            right_node = create_tree(string_tree[i + 2:-1])
            return Node(left=left_node, right=right_node)


def part_1(values: list) -> int:
    values = list(map(create_tree, values))
    tree = values[0]
    for next_tree in values[1:]:
        tree += next_tree
        reduce(tree)
    return tree.magnitude()


def calc_combinations(values: list, i: tuple):
    return max(part_1([values[i[0]], values[i[1]]]), part_1([values[i[1]], values[i[0]]]))

def part_2(values: list) -> int:
    return max([calc_combinations(values, i) for i in itertools.combinations(range(len(values)), r=2)])


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 4140
    assert part_2(test_input) == 3993

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

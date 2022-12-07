from aoc.api import *

class Leaf:

    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size

class Node:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = dict()

    def add_child(self, node):
        self.children[node.name] = node

    @property
    def size(self):
        return sum([child.size for child in self.children.values()])


def read_input(filename: str) -> Node:
    root = Node("root", None)
    root.add_child(Node("/", root))
    current = root
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            if line.startswith("$ cd"):
                if line.split(" ")[-1] == "..":
                    current = current.parent
                else:
                    current = current.children[line.split(" ")[-1]]
            elif line.startswith("$ ls"):
                continue
            elif line.startswith("dir"):
                current.add_child(Node(line.split(" ")[1], current))
            else:
                data = line.split(" ")
                current.add_child(Leaf(data[1], current, int(data[0])))
    return root.children["/"]

def collect_sizes(node, sizes=None):
    if sizes is None:
        sizes = []
    if hasattr(node, "children"):
        sizes.append(node.size)
        for child in node.children.values():
            collect_sizes(child, sizes)
        return sizes


def part_1(node: Node) -> int:
    return Stream(collect_sizes(node)).filter(lambda x: x < 100_000).sum()

def part_2(node: Node) -> int:
    return Stream(collect_sizes(node)).filter(lambda x: x > node.size - 40_000_000).min()


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 95437
    assert part_2(test_input) == 24933642

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

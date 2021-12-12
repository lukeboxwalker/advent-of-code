from collections import defaultdict
from timeit import timeit


def read_input(filename: str) -> dict:
    with open(filename, "r") as f:
        graph = defaultdict(set)
        for line in f.read().splitlines():
            nodes = line.split("-")
            graph[nodes[0]].add(nodes[1])
            graph[nodes[1]].add(nodes[0])
        return graph


def paths_path_1(graph: dict, current_path: list, node_name: str):
    if node_name == "end":
        return 1
    if node_name[0].islower() and node_name in current_path:
        return 0
    current_path = current_path.copy()
    current_path.append(node_name)
    return sum(paths_path_1(graph, current_path, node) for node in graph[node_name])


def paths_path_2(graph: dict, current_path: dict, node_name: str):
    if node_name == "end":
        current_path["nodes"].append(node_name)
        return 1
    if node_name == "start" and node_name in current_path["nodes"]:
        return 0
    current_path = {"small_twice": current_path["small_twice"], "nodes": current_path["nodes"].copy()}
    if node_name[0].islower() and node_name in current_path["nodes"]:
        if current_path["small_twice"]:
            return 0
        else:
            current_path["small_twice"] = True
    current_path["nodes"].append(node_name)
    return sum(paths_path_2(graph, current_path, node) for node in graph[node_name])


def part_1(values: dict) -> int:
    return paths_path_1(values, [], "start")


def part_2(values: dict) -> int:
    return paths_path_2(values, {"small_twice": False, "nodes": []}, "start")


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 10
    assert part_2(test_input) == 36

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

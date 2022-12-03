import sys
from timeit import timeit


def print_solution(part_1, part_2):
    print(str(sys.argv[0].split("puzzle.py")[0]) + "solution.txt")
    solution_1 = part_1()
    solution_2 = part_2()
    with open(str(sys.argv[0].split("puzzle.py")[0]) + "solution.txt", "w") as f:
        f.write("Part 1: " + str(solution_1) + "\nPart 2: " + str(solution_2))
    print(f"Part 1: {solution_1}, Timing: %.2f ms" % (1000 * timeit(part_1, number=1)))
    print(f"Part 2: {solution_2}, Timing: %.2f ms" % (1000 * timeit(part_2, number=1)))

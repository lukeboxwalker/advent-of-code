import os
import time
import unittest

from parameterized import parameterized

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))


def build_params():
    params = []
    years = [i for i in os.listdir(ROOT) if i.startswith("year")]
    for year_path in years:
        year_dir = os.path.join(ROOT, year_path)
        days = sorted([i for i in os.listdir(year_dir) if i.startswith("day")])
        params += list(zip([year_path] * len(days), days))
    return params


class PuzzleTest(unittest.TestCase):

    @parameterized.expand([
        (f"{year}_{day}", year, day) for year, day in build_params()
    ])
    def test_puzzle_parts(self, name: str, year_path: str, day_path: str):
        module = __import__(year_path + "." + day_path + ".puzzle", globals(), locals(), [], 0)

        path = "../" + year_path + "/" + day_path
        print("Testing: " + year_path + " " + day_path)
        params_1 = []
        params_2 = []

        part_1 = module.__dict__[day_path].puzzle.part_1
        part_2 = module.__dict__[day_path].puzzle.part_2

        read_input = module.__dict__[day_path].puzzle.read_input
        params_1.append(read_input(path + "/input.txt"))
        params_2.append(read_input(path + "/input.txt"))

        if module.__dict__[day_path].puzzle.__dict__.__contains__("read_extra_input"):
            read_extra_input = module.__dict__[day_path].puzzle.read_extra_input
            params_1.append(read_extra_input(path + "/extra_input.txt"))
            params_2.append(read_extra_input(path + "/extra_input.txt"))

        solution1, solution2 = 0, 0
        with open(path + "/solution.txt") as file:
            solution1, solution2 = [i.split(": ")[1] for i in file.read().splitlines()]
            if solution1.isdigit():
                solution1 = int(solution1)
            if solution2.isdigit():
                solution2 = int(solution2)
        start = time.time()
        part1 = part_1(*params_1)
        elapsed = time.time() - start
        print(f"\t- part_1 took: {elapsed:.3f}s")

        start = time.time()
        part2 = part_2(*params_2)
        elapsed = time.time() - start
        print(f"\t- part_2 took: {elapsed:.3f}s")

        self.assertEqual(solution1, part1, day_path + " part1")
        self.assertEqual(solution2, part2, day_path + " part2")

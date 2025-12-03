import os
import unittest

from parameterized import parameterized


def build_params():
    params = []
    years = [i for i in os.listdir(os.getcwd() + "/..") if i.startswith("year")]
    for year_path in years:
        days = sorted(
            [i for i in os.listdir(os.getcwd() + "/../" + year_path) if i.startswith("day")])
        params += list(zip([year_path] * len(days), days))
    return params


class PuzzleTest(unittest.TestCase):

    @parameterized.expand(build_params())
    def test_puzzle_parts(self, year_path: str, day_path: str):
        module = __import__(year_path + "." + day_path + ".puzzle", globals(), locals(), [], 0)

        path = "../" + year_path + "/" + day_path
        print("Testing: " + path)
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
        self.assertEqual(part_1(*params_1), solution1, day_path + " part1")
        self.assertEqual(part_2(*params_2), solution2, day_path + " part2")

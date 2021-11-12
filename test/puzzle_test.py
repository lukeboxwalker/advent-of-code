import os
import unittest

from parameterized import parameterized


def build_params():
    params = []
    years = [i for i in os.listdir(os.getcwd() + "/..") if i.startswith("year")]
    for year_path in years:
        days = sorted([i for i in os.listdir(os.getcwd() + "/../" + year_path) if i.startswith("day")])
        params += list(zip([year_path] * len(days), days))
    return params


if __name__ == '__main__':
    print(build_params())


class PuzzleTest(unittest.TestCase):

    @parameterized.expand(build_params())
    def test_all(self, year_path: str, day_path: str):

        module = __import__(year_path + "." + day_path + ".puzzle", globals(), locals(), [], 0)

        read_input = module.__dict__[day_path].puzzle.read_input
        part_1 = module.__dict__[day_path].puzzle.part_1
        part_2 = module.__dict__[day_path].puzzle.part_2

        path = "../" + year_path + "/" + day_path
        solution1, solution2 = 0, 0
        with open(path + "/solution.txt") as file:
            solution1, solution2 = [int(i.split(": ")[1]) for i in file.read().splitlines()]

        self.assertEqual(part_1(read_input(path + "/input.txt")), solution1)
        self.assertEqual(part_2(read_input(path + "/input.txt")), solution2)

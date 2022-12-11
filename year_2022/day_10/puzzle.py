import numpy as np
import pytesseract as pytesseract
from PIL import Image
import cv2 as cv

from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        content = f.read().replace("noop", "1 0").replace("addx", "2")
        return [list(map(int, i.split(" "))) for i in content.split("\n")]


def part_1(values: list) -> int:
    cycle, rax, result = 0, 1, 0
    for value in values:
        for _ in range(value[0]):
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                result += rax * cycle
        rax += value[1]
    return result


def part_2(values: list) -> str:
    cycle = 0
    rax = 1
    img = np.full((10, 42), 255, np.uint8)
    for value in values:
        for i in range(value[0]):
            if rax + 2 > cycle % 40 > rax - 2:
                img[cycle // 40 + 2, cycle % 40 + 2] = 0
            cycle += 1
        rax += value[1]
    img = cv.resize(img, (420, 80))
    img = cv.threshold(img, 180, 255, cv.THRESH_BINARY)[1]
    img = Image.fromarray(img)
    text = pytesseract.image_to_string(img)
    return "".join(list(filter(lambda c: c.isalpha(), text)))


if __name__ == '__main__':
    test_input = read_input("test_input.txt")
    assert part_1(test_input) == 13140
    assert part_2(test_input) == ""

    my_input = read_input("input.txt")
    print_solution(lambda: part_1(my_input), lambda: part_2(my_input))

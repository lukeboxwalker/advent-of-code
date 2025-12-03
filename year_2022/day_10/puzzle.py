import base64

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
    cycle, rax, img = 0, 1, np.full((10, 42), 255, np.uint8)
    for value in values:
        for i in range(value[0]):
            if rax + 2 > cycle % 40 > rax - 2:
                img[cycle // 40 + 2, cycle % 40 + 2] = 0
            cycle += 1
        rax += value[1]
    img = cv.resize(img, (420, 80))
    img = cv.threshold(img, 180, 255, cv.THRESH_BINARY)[1]
    retval, buffer = cv.imencode('.png', img)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    return jpg_as_text


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 13140
    assert part_2(read_input("test_input.txt")) == "iVBORw0KGgoAAAANSUhEUgAAAaQAAABQCAAAAABzU15SAAAEYElEQVR4Ae3BS5akOAAEQff7Hzpm0T2PREipH1XNAjPD6+kMr6czvJ7O8Ho6w+vpDK+nM7yezvB6OsPr6QyvpzO8ns7wejrD6+kMr6cz1MkhtMkhtMkhtMkhtMkhtMkhtMkhtMkhtMkhtMkh1Blq5CzUyVmok7NQJ2ehTs5CnZyFOjkLdXIW6uQs1MlZqDFcyVW4kqtwJVfhSq7ClVyFK7kKV3IVruQqXMlVuJKrcGW4kJpQkppQkppQkppQkppQkppQkppQkppQkppQkppwYbiQmlCSmlCSmlCSmlCSmlCSmlCSmlCSmlCSmlCSmnBhKEldOJO6cCZ14UzqwpnUhTOpC2dSF86kLpxJXTiTulAylKQhnEhdOJGGcCYN4UTqwok0hDNpCCdSF06kIZxJQygYStISTqQufJCGUJCWcCJ14YM0hIK0hBOpCx+kIRSkJZwZStIWPsiOUJC28EF2hIK0hQ+yIxSkLXwylOSbcJB1oSTfhIOsCyX5JhxkXSjJN+FgKMl34SBrwpV8Fw6yJlzJd+Ega8KVfBf+ZyhJR/gg80KNdIQPMi/USEf4IPNCjXSEvwwl6QgtMiDUSUdokQGhTjpCiwwIddIR/jKUpCe0SFdokJ7QIl2hQXpCi3SFBukJfxhK0hUapCs0SE9okK7QIl2hQbpCg/SEPwwl6QsN0hWqpCc0SFdokr7QIF2hSnrCX4aSjAhV8nPCB5kSmmREqJKfE/4ylGRMqJGfEg4yJ7TJmFAjPyX8z1CSUaFGfkI4yJzwjYwKNfITwsFQkmGhSu4WPsiU8J0MC1Vyt/DJUJJhoUumhD6ZEHpkWOiSKWGAoSTjQpdMCH0yIXTJuNAlE8IIQ0kmhC6ZELpkXOiSCaFLJoQRhpLMCF0yIXTJuNAhE0KXTAhDDCWZEzpkW/gg/0qokkVhiKEks8J3si8c5N8INbIqjDGUZF74TvaFg/y+UCOrwihDSRaEDtkWPsjvClWyKIwzlGRBmCBLwgxZFCbIkjDDUJIVYYIsCTNkSZggS8IUQ0mWhAmyJEyQJWGCrAhzDCVZEybIkjBBloRhsiJMMpRkVRgmNwpV8kzhg/QZSrIujJI7hRp5onCQEYaS7Aij5E6hRp4mHGSMoSRbwjC5UaiSJwkfZJChJFvCEtkUlsi2sEYGGUqyJyyRTWGJbAprZJShJJvCEtkUlsimsERGGUqyKyyRTWGJbApLZJChJPvCAvkRoUN+TfgggwwluUOYJz8jfCe/JxxkjKEk9wjz5GeE7+T3hIOMMJTkJmGB/IjQIb8mfJA+Q0luEjbJbcImuU2YZCjJXcImuU3YJLcJcwwluUvYJXcJu+QuYY7hQu4R9sk9wj65R5hkuJB7hH1yj7BP7hEmGa7kDuEOcodwB7lDmGWokV3hLrIr3EV2hXmGOtkR7iQ7wp1kR1hheD2d4fV0htfTGV5PZ3g9neH1dIbX0xleT2d4PZ3h9XSG19MZXk9neD2d4fV0/wFTK1wcKVbE7gAAAABJRU5ErkJggg=="

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

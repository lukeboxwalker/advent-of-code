from enum import Enum

from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        games = []
        for line in f.read().splitlines():
            game = line.split(":")
            game_nr = int(game[0].split("Game ")[1])
            sets_shown = game[1].split(";")
            game_sets = []
            for sets_shown in sets_shown:
                shown = []
                for color in sets_shown.split(","):
                    color_amount = color.split(" ")
                    shown.append((int(color_amount[1]), color_amount[2]))
                game_sets.append(shown)
            games.append((game_nr, game_sets))
        return games

def game_possible_value(game):
    for sets in game[1]:
        for color in sets:
            if color[1] == "red" and color[0] > 12:
                return 0
            if color[1] == "green" and color[0] > 13:
                return 0
            if color[1] == "blue" and color[0] > 14:
                return 0
    return game[0]

def part_1(values: list) -> int:
    return sum([game_possible_value(game) for game in values])

def game_power_value(game):
    red = 0
    green = 0
    blue = 0
    for sets in game[1]:
        for color in sets:
            if color[1] == "red":
                red = max(red, color[0])
            if color[1] == "green":
                green = max(green, color[0])
            if color[1] == "blue":
                blue = max(blue, color[0])
    return red * green * blue

def part_2(values: list) -> int:
    return sum([game_power_value(game) for game in values])


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 8
    assert part_2(read_input("test_input.txt")) == 2286

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

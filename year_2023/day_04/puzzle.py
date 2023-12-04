from aoc.api import *


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        cards = []
        for line in f.read().splitlines():
            numbers = line.split(": ")[1].split(" | ")
            winning_numbers = set()
            my_numbers = set()
            for winning in numbers[0].split(" "):
                if winning == "":
                    continue
                winning_numbers.add(int(winning))
            for my in numbers[1].split(" "):
                if my == "":
                    continue
                my_numbers.add(int(my))
            cards.append((winning_numbers, my_numbers))
    return cards


def part_1(values: list) -> int:
    result = 0
    for card in values:
        power = -1
        for my_number in card[1]:
            if my_number in card[0]:
                power += 1
        if power > -1:
            result += 2**power
    return result


def part_2(values: list) -> int:
    number_mul = [1 for _ in range(len(values))]
    for card_nr, card in enumerate(values):
        power = -1
        for my_number in card[1]:
            if my_number in card[0]:
                power += 1
        if power > -1:
            for i in range(card_nr + 1, card_nr + power + 2):
                number_mul[i] += 1 * number_mul[card_nr]
    return sum(number_mul)


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 13
    assert part_2(read_input("test_input.txt")) == 30

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

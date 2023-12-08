from collections import defaultdict

from aoc.api import *


def read_input(filename: str) -> list:
    hands = []
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            hand = line.split()
            hands.append((hand[0], int(hand[1])))
    return hands


global_digit_map = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
}

def map_card(c, digit_map):
    if c in digit_map:
        return digit_map[c]
    return c


def count_hand(hand, digit_map):
    count = defaultdict(lambda: 0)
    for c in hand:
        count[map_card(c, digit_map)] += 1
    return count, [(map_card(c, digit_map), n) for c, n in count.items()]


def joker_count(x, count, with_joker):
    if not with_joker:
        return 0
    return 0 if x[0] == "01" else count["01"]

def insert_and_get(rank, value):
    rank.insert(0, value)
    return int("".join(rank))

def is_5_pair(count, count_list, with_joker):
    return any(map(lambda x: x[1] + joker_count(x, count, with_joker) == 5, count_list))

def is_4_pair(count, count_list, with_joker):
    return any(map(lambda x: x[1] + joker_count(x, count, with_joker) == 4, count_list))

def is_3_pair(count, count_list, with_joker):
    return any(map(lambda x: x[1] + joker_count(x, count, with_joker) == 3, count_list))

def is_2_pair(count, count_list, with_joker):
    return any(map(lambda x: x[1] + joker_count(x, count, with_joker) == 2, count_list))

def is_2x2_pair(count_list, with_joker):
    def no_joker_pair(x):
        return not with_joker or x[0] != "01"
    return len(list(i for i in map(lambda x: x[1] == 2 and no_joker_pair(x), count_list) if i)) == 2

def is_full_house(count, count_list, with_joker):
    is_classic_full_house = (is_3_pair(count, count_list, False) and is_2_pair(count, count_list, False))
    if not with_joker:
        return is_classic_full_house
    return is_classic_full_house or (is_2x2_pair(count_list, True) and count["01"] == 1)

def get_deck_rank(hand, digit_map, with_joker=False):

    rank = list(map(lambda x: map_card(x, digit_map), hand))
    count, count_list = count_hand(hand, digit_map)

    if is_5_pair(count, count_list, with_joker):
        return insert_and_get(rank, "7")
    if is_4_pair(count, count_list, with_joker):
        return insert_and_get(rank, "6")
    if is_full_house(count, count_list, with_joker):
        return insert_and_get(rank, "5")
    if is_3_pair(count, count_list, with_joker):
        return insert_and_get(rank, "4")
    if is_2x2_pair(count_list, with_joker):
        return insert_and_get(rank, "3")
    if is_2_pair(count, count_list, with_joker):
        return insert_and_get(rank, "2")
    return insert_and_get(rank, "1")


def part_1(values: list) -> int:
    return sum([val[1] * (i + 1) for i, val in enumerate(sorted(values, key=lambda x: get_deck_rank(x[0], global_digit_map, with_joker=False)))])


def part_2(values: list) -> int:
    digit_map = global_digit_map.copy()
    digit_map["J"] = "01"
    return sum([val[1] * (i + 1) for i, val in enumerate(sorted(values, key=lambda x: get_deck_rank(x[0], digit_map, with_joker=True)))])


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 6440
    assert part_2(read_input("test_input.txt")) == 5905

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

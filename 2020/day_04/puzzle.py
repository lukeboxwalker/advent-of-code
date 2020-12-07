import re


def data_to_pass_map(data: str) -> map:
    pass_map = {}
    for key_val in data.split():
        key, val = key_val.split(":")
        if key != "cid":
            pass_map[key] = val
    return pass_map


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [data_to_pass_map(d.replace("\n", " ")) for d in f.read().split("\n\n")]


def part_1(values: list) -> int:
    return sum(len(pass_map) == 7 for pass_map in values)


def part_2(values: list) -> int:
    patterns = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}"
    }
    return sum(all(re.fullmatch(patterns[k], p[k]) for k in p) and len(p) == 7 for p in values)


if __name__ == '__main__':
    assert part_1(read_input("test.txt")) == 2

    assert part_2(read_input("test_invalid.txt")) == 0
    assert part_2(read_input("test_valid.txt")) == 4

    input_map = read_input("input.txt")
    print("Puzzle 1:", part_1(input_map))
    print("Puzzle 2:", part_2(input_map))

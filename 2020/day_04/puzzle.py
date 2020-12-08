import re


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        return [dict(map(lambda x: (x.split(":")[0], x.split(":")[1]), data.replace("\n", " ").split())) for data in
                f.read().split("\n\n") if all(key in data for key in required)]


def part_1(values: list) -> int:
    return len(values)


def part_2(values: list) -> int:
    patterns = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
        "cid": ".*"
    }
    return sum(all(re.fullmatch(patterns[key], val[key]) for key in val) for val in values)


if __name__ == '__main__':
    assert part_1(read_input("test.txt")) == 2
    assert part_2(read_input("test_invalid.txt")) == 0
    assert part_2(read_input("test_valid.txt")) == 4

    input_map = read_input("input.txt")
    print("Part 1:", part_1(input_map))
    print("Part 2:", part_2(input_map))

import re


def read_input(filename: str) -> map:
    regex = re.compile(r" bags?")
    result = {}
    with open(filename, "r") as f:
        for bag in f.read().splitlines():
            key, value_data = bag[:-1].split(" bags contain ")
            values = {}
            if value_data != "no other bags":
                for val in [re.sub(regex, "", val) for val in value_data.split(", ")]:
                    values[val[2:]] = int(val[0])
            result[key] = values
    return result


def find_bags(bags: map, search_bag: str, result: set) -> set:
    for bag in bags:
        if bag != search_bag and search_bag in bags.get(bag):
            result.add(bag)
            find_bags(bags, bag, result)
    return result


def part_1(bags: map) -> int:
    return len(find_bags(bags, "shiny gold", set()))


def count_bags(bags: map, count_bag: str) -> int:
    count = 1
    for bag in bags.get(count_bag):
        count += bags.get(count_bag).get(bag) * count_bags(bags, bag)
    return count


def part_2(bags: map) -> int:
    return count_bags(bags, "shiny gold") - 1


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 4
    assert part_2(test_input) == 32
    assert part_2(read_input("test_nested_bags.txt")) == 126

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

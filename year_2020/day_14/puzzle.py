import itertools


class Data:

    def __init__(self, mask: str, operations: list):
        self.mask = mask
        self.operations = operations

    def __str__(self):
        return "mask: " + self.mask + "operations: " + self.operations.__str__()


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        result = []
        operations = []
        mask = None
        for line in f.read().splitlines():
            if line.startswith("mask"):
                if mask is not None:
                    result.append(Data(mask, operations))
                    operations = []
                mask = line.split(" = ")[1]
            else:
                mem_split = line.replace("mem[", "").split("] = ")
                operations.append((int(mem_split[0]), int(mem_split[1])))
        result.append(Data(mask, operations))
        return result


def part_1(values: list) -> int:
    mem = dict()
    for val in values:
        and_mask = int(val.mask.replace("X", "1"), 2)
        or_mask = int(val.mask.replace("X", "0"), 2)
        for i in val.operations:
            mem[i[0]] = (i[1] & and_mask) | or_mask
    return sum(mem.values())


def part_2(values: list) -> int:
    mem = dict()
    combination_cache = {}
    for val in values:
        x_count = val.mask.count("X")
        if x_count not in combination_cache:
            combination_cache[x_count] = [i for i in itertools.product([1, 0], repeat=x_count)]
        combinations = combination_cache[x_count]
        and_mask = val.mask.replace("0", "1").replace("X", "0")
        comb_or_masks = []
        for combination in combinations:
            or_mask = val.mask
            for x in combination:
                or_mask = or_mask.replace("X", str(x), 1)
            comb_or_masks.append(or_mask)

        for i in val.operations:
            for or_mask in comb_or_masks:
                mem[(i[0] & int(and_mask, 2)) | int(or_mask, 2)] = i[1]
    return sum(mem.values())


if __name__ == '__main__':
    assert part_1(read_input("test_part_1.txt")) == 165
    assert part_2(read_input("test.txt")) == 208

    my_input = read_input("input.txt")
    print("Part 1:", part_1(my_input))
    print("Part 2:", part_2(my_input))

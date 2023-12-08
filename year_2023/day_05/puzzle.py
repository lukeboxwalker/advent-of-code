from aoc.api import *


def read_input(filename: str) -> tuple:
    maps = dict()
    with open(filename, "r") as f:
        lines = f.read().split("\n\n")
        seeds = list(map(int, lines[0].split(":")[1].split()))
        for line in lines[1:]:
            map_info = []
            parts = line.split("\n")
            for part in parts[1:]:
                map_info.append(list(map(int, part.split())))
            maps[parts[0].split()[0]] = map_info
    return seeds, maps

def get_mapped_value(val, dest_start, source_start, range_len):
    if source_start <= val <= source_start + range_len - 1:
        return dest_start + val - source_start
    return None

def part_1(values: tuple) -> int:
    locations = []
    for seed in values[0]:
        val = seed
        for mapper in values[1]:
            for map_info in values[1][mapper]:
                mapped_val = get_mapped_value(val, map_info[0], map_info[1], map_info[2])
                if mapped_val is not None:
                    val = mapped_val
                    break
        locations.append(val)
    return min(locations)

def get_mapped_range(val_start, val_len, dest_start, source_start, range_len):
    left_over_val = []
    if val_start < source_start:  # sub range before the mapping part
        if val_start + val_len - 1 < source_start:  # range is out of mapping part
            return None, [(val_start, val_len)]
        left_over_val.append((val_start, source_start - val_start))
    if val_start + val_len - 1 > source_start + range_len - 1:  # sub range after the mapping part
        if val_start > source_start + range_len - 1:  # range is out of mapping part
            return None, [(val_start, val_len)]
        left_over_val.append((source_start + range_len, val_start + val_len - source_start - range_len))
    if source_start <= val_start <= source_start + range_len - 1:  # range starts inside mapping part
        if val_start + val_len - 1 > source_start + range_len - 1:  # range is longer then mapping part
            return (dest_start + val_start - source_start, source_start + range_len - val_start), left_over_val
        return (dest_start + val_start - source_start, val_len), left_over_val  # range ends inside mapping part
    if val_start + val_len - 1 >= source_start > val_start:  # range ends inside mapping part or is longer while starting before mapping part
        if source_start + range_len - 1 < val_start + val_len - 1:  # range is longer than mapping part
            return (dest_start, range_len), left_over_val
        else:  # range ends inside mapping part
            return (dest_start, val_start + val_len - source_start), left_over_val
    return None, left_over_val

def part_2(values: tuple) -> int:
    ranges: list = Stream(values[0]).group(2).list()
    for mapper in values[1]:
        mapped_ranges = []
        all_left_over_ranges = []
        for map_info in values[1][mapper]:
            all_left_over_ranges = []
            while ranges:
                current_range = ranges.pop(0)
                mapped_range, left_over_ranges = get_mapped_range(current_range[0], current_range[1], map_info[0], map_info[1], map_info[2])
                if mapped_range is not None:
                    mapped_ranges.append(mapped_range)
                all_left_over_ranges.extend(left_over_ranges)
            ranges = all_left_over_ranges
        ranges = mapped_ranges
        if all_left_over_ranges:
            ranges.extend(all_left_over_ranges)
    return min(map(lambda x: x[0], ranges))


if __name__ == '__main__':
    assert part_1(read_input("test_input.txt")) == 35
    assert part_2(read_input("test_input.txt")) == 46

    print("Part 1:", format_solution(lambda: part_1(read_input("input.txt"))))
    print("Part 2:", format_solution(lambda: part_2(read_input("input.txt"))))

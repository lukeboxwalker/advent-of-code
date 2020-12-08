def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [(line.split()[0], int(line.split()[1])) for line in f.read().splitlines()]


def run_program(values: list) -> (int, bool):
    visited = set()
    acc = 0
    cmd_count = 0
    while True:
        if cmd_count in visited:
            return acc, True
        if cmd_count >= len(values):
            return acc, False
        visited.add(cmd_count)
        cmd = values[cmd_count]
        if "nop" == cmd[0]:
            cmd_count += 1
        if "acc" == cmd[0]:
            acc += cmd[1]
            cmd_count += 1
        if "jmp" == cmd[0]:
            cmd_count += cmd[1]


def part_1(values: list) -> int:
    acc, loop = run_program(values)
    if loop:
        return acc
    else:
        return -1


def replace_and_run(index: int, replace: str, v_copy: list) -> (int, bool):
    v_copy[index] = (replace, v_copy[index][1])
    return run_program(v_copy)


def part_2(values: list) -> int:
    for i in range(len(values)):
        if values[i][0] == "nop":
            acc, loop = replace_and_run(i, "jmp", values[:])
            if not loop:
                return acc
        if values[i][0] == "jmp":
            acc, loop = replace_and_run(i, "nop", values[:])
            if not loop:
                return acc


if __name__ == '__main__':
    test_input = read_input("test.txt")
    assert part_1(test_input) == 5
    assert part_2(test_input) == 8

    my_input = read_input("input.txt")
    print("Puzzle 1:", part_1(my_input))
    print("Puzzle 2:", part_2(my_input))

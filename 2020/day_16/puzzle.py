class Rule:

    def __init__(self, name: str, rules: str):
        self.name = name
        rules_split = rules.split(" or ")
        first = rules_split[0].split("-")
        second = rules_split[1].split("-")
        self.first_lower = int(first[0])
        self.first_upper = int(first[1])
        self.second_lower = int(second[0])
        self.second_upper = int(second[1])

    def is_fitting(self, number: int) -> bool:
        return self.first_lower <= number <= self.first_upper or self.second_lower <= number <= self.second_upper


def read_input(filename: str) -> [list, list, list]:
    with open(filename, "r") as f:
        index = 0
        rules = []
        my_ticket = []
        nearby_tickets = []
        lines = f.read().splitlines()
        while index < len(lines):
            if lines[index] == "your ticket:":
                my_ticket = [int(i) for i in lines[index + 1].split(",")]
                index += 2
                continue
            if lines[index] == "nearby tickets:":
                index += 1
                while index < len(lines):
                    nearby_tickets.append([int(i) for i in lines[index].split(",")])
                    index += 1
                break
            if lines[index] != "":
                split = lines[index].split(": ")
                rules.append(Rule(split[0], split[1]))
            index += 1
    return rules, my_ticket, nearby_tickets


def part_1(rules: list, nearby_tickets: list) -> int:
    result = []
    for ticket in nearby_tickets:
        for num in ticket:
            valid = False
            for rule in rules:
                if rule.is_fitting(num):
                    valid = True
            if not valid:
                result.append(num)
    return sum(result)


def collect_valid_tickets(rules: list, nearby_tickets: list) -> list:
    valid_nearby_tickets = []
    for ticket in nearby_tickets:
        ticket_valid = True
        for num in ticket:
            valid = False
            for rule in rules:
                if rule.is_fitting(num):
                    valid = True
            if not valid:
                ticket_valid = False
        if ticket_valid:
            valid_nearby_tickets.append(ticket)
    return valid_nearby_tickets


def part_2(rules: list, my_tickets: list, nearby_tickets: list) -> int:
    valid_nearby_tickets = collect_valid_tickets(rules, nearby_tickets)
    rule_map = {}
    found_index = set()
    for rule in rules:
        for j in range(len(my_tickets)):
            if j not in found_index and rule.name not in rule_map:
                is_fitting = True
                for ticket in valid_nearby_tickets:
                    if not rule.is_fitting(ticket[j]):
                        is_fitting = False
                if is_fitting:
                    rule_map[rule.name] = j
                    found_index.add(j)
    result = 1
    for key in rule_map:
        if key.startswith("departure"):
            result *= my_tickets[rule_map[key]]
    return result


if __name__ == '__main__':
    rules, my_ticket, nearby_tickets = read_input("test.txt")
    #assert part_1(rules, nearby_tickets) == 71
    #assert part_2(rules, my_ticket, nearby_tickets) == -1

    rules, my_ticket, nearby_tickets = read_input("input.txt")
    print("Part 1:", part_1(rules, nearby_tickets))
    print("Part 2:", part_2(rules, my_ticket, nearby_tickets))

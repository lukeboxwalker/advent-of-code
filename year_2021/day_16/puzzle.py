from abc import abstractmethod
from functools import reduce
from timeit import timeit


class Packet:

    def __init__(self, version: int, type_id: int):
        self.type_id = type_id
        self.version = version

    def __str__(self) -> str:
        return f"version={self.version}, type_id={self.type_id}"

    @abstractmethod
    def get_version_sum(self):
        pass

    @abstractmethod
    def calc(self):
        pass


class OperatorPacket(Packet):

    def __init__(self, version: int, type_id: int, packets: list):
        super().__init__(version, type_id)
        self.packets = packets

    def __str__(self) -> str:
        packets_str = ["["]
        for i in self.packets:
            packets_str += [str(i)]
            packets_str += [","]
        packets_str = packets_str[:-1]
        packets_str += ["]"]
        return "Operator:{" + super().__str__() + f", packets={''.join(packets_str)}" + "}"

    def get_version_sum(self) -> int:
        version_sum = self.version
        for packet in self.packets:
            version_sum += packet.get_version_sum()
        return version_sum

    def calc(self) -> int:
        sub_calc = list(map(lambda x: x.calc(), self.packets))
        if self.type_id == 0:
            return sum(sub_calc)
        if self.type_id == 1:
            return reduce(lambda a, b: a * b, [1] + sub_calc)
        if self.type_id == 2:
            return min(sub_calc)
        if self.type_id == 3:
            return max(sub_calc)
        if self.type_id == 5:
            return 1 if sub_calc[0] > sub_calc[1] else 0
        if self.type_id == 6:
            return 1 if sub_calc[0] < sub_calc[1] else 0
        if self.type_id == 7:
            return 1 if sub_calc[0] == sub_calc[1] else 0


class LiteralPacket(Packet):

    def __init__(self, version: int, type_id: int, literal_value: int):
        super().__init__(version, type_id)
        self.literal_value = literal_value

    def __str__(self) -> str:
        return "Literal:{" + super().__str__() + f", value={self.literal_value}" + "}"

    def get_version_sum(self):
        return self.version

    def calc(self):
        return self.literal_value

def bin_to_int(values: list):
    return reduce(lambda a, b: (a << 1) | b, [0] + values)


def parse(hex_num: str) -> Packet:
    return read_packet(list(map(int, bin(int(hex_num, 16))[2:].zfill(len(hex_num) * 4))))[0][0]


def read_input(filename: str) -> Packet:
    with open(filename, "r") as f:
        return parse(f.read().splitlines()[0])


def read_packet(values: list, max_packets=0) -> tuple:
    packets, idx = [], 0
    while sum(values[idx:]) != 0:
        if 0 < max_packets == len(packets):
            return packets, idx
        packet_version = bin_to_int(values[idx: idx + 3])
        type_id = bin_to_int(values[idx + 3: idx + 6])
        if type_id == 4:
            literal_value, labels = [], 0
            while values[idx + 6 + labels] == 1:
                literal_value += values[idx + 7 + labels: idx + 11 + labels]
                labels += 5
            literal_value += values[idx + 7 + labels: idx + 11 + labels]
            packets.append(LiteralPacket(packet_version, type_id, bin_to_int(literal_value)))
            idx = idx + 11 + labels
        elif values[idx + 6] == 0:
            length = bin_to_int(values[idx + 7: idx + 22])
            read, _ = read_packet(values[idx + 22: idx + 22 + length])
            packets.append(OperatorPacket(packet_version, type_id, read))
            idx = idx + 22 + length
        elif values[idx + 6] == 1:
            packet_count = bin_to_int(values[idx + 7: idx + 18])
            read, ret_idx = read_packet(values[idx + 18:], packet_count)
            idx = ret_idx + idx + 18
            packets.append(OperatorPacket(packet_version, type_id, read))
    return packets, idx


def part_1(packet: Packet) -> int:
    return packet.get_version_sum()


def part_2(packet: Packet) -> int:
    return packet.calc()


if __name__ == '__main__':
    assert part_1(parse("8A004A801A8002F478")) == 16
    assert part_1(parse("620080001611562C8802118E34")) == 12
    assert part_1(parse("C0015000016115A2E0802F182340")) == 23
    assert part_1(parse("A0016C880162017C3686B18A3D4780")) == 31

    assert part_2(parse("C200B40A82")) == 3
    assert part_2(parse("04005AC33890")) == 54
    assert part_2(parse("880086C3E88112")) == 7
    assert part_2(parse("CE00C43D881120")) == 9
    assert part_2(parse("D8005AC2A8F0")) == 1
    assert part_2(parse("F600BC2D8F")) == 0
    assert part_2(parse("9C005AC2F8F0")) == 0
    assert part_2(parse("9C0141080250320F1802104A08")) == 1

    my_input = read_input("input.txt")
    print(f"Part 1: {part_1(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_1(my_input), number=1)))
    print(f"Part 2: {part_2(my_input)}, Timing: %.2f ms" % (1000 * timeit(lambda: part_2(my_input), number=1)))

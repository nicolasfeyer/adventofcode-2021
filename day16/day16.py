import time
from functools import reduce
from typing import List, Union, Tuple


def read_input():
    return open("data/day16.txt", "r").read().strip()


TAG_LENGTH = 3
VERSION_LENGTH = 3
OPERATOR_0_INFO_LENGTH = 16
OPERATOR_1_INFO_LENGTH = 12

hex_to_binary_d = {"0": "0000",
                   "1": "0001",
                   "2": "0010",
                   "3": "0011",
                   "4": "0100",
                   "5": "0101",
                   "6": "0110",
                   "7": "0111",
                   "8": "1000",
                   "9": "1001",
                   "A": "1010",
                   "B": "1011",
                   "C": "1100",
                   "D": "1101",
                   "E": "1110",
                   "F": "1111"}


def hex_to_binary(hex_string):
    return "".join([hex_to_binary_d[c] for c in hex_string])


class Packet:
    def __init__(self, version, tag, data, end_pos):
        self.version = version
        self.tag = tag
        self.end_pos = end_pos
        self.data = data

    def __str__(self):
        return str(self.version) + " " + str(self.tag) + " " + str(self.data) + " " + str(self.end_pos)


def analyze_packet(s) -> tuple[Packet, int]:
    version = int(s[0:3], 2)
    tag = int(s[3:6], 2)
    data = s[6:]

    packet = Packet(version, tag, None, len(data))
    if tag == 4:
        packet_length = 0
        number_b = ""
        for i in range(0, len(data), 5):
            number_b += data[i + 1:i + 5]
            packet_length += 5
            if data[i] == "0":
                break

        packet.data = int(number_b, 2)
    elif data[0] == "0":  # the next 15 bits represents the length of the rest

        subpacket_length = int(data[1:OPERATOR_0_INFO_LENGTH], 2)
        data = data[OPERATOR_0_INFO_LENGTH:]

        subpackets_list = list()
        packet_length = 0
        while packet_length < subpacket_length:
            p, leng = analyze_packet(data[packet_length:])
            packet_length += leng
            subpackets_list.append(p)

        packet_length += OPERATOR_0_INFO_LENGTH
        packet.data = subpackets_list

    else:  # = 1, all packet length of 11 bit
        number_packets = int(data[1:OPERATOR_1_INFO_LENGTH], 2)
        data = data[OPERATOR_1_INFO_LENGTH:]

        subpackets_list = list()
        packet_length = 0
        for i in range(number_packets):
            p, leng = analyze_packet(data[packet_length:])
            packet_length += leng
            subpackets_list.append(p)

        packet_length += OPERATOR_1_INFO_LENGTH
        packet.data = subpackets_list

    return packet, packet_length + TAG_LENGTH + VERSION_LENGTH


def compute_sum_version(p: Packet):
    return p.version if isinstance(p.data, int) else sum([compute_sum_version(p_) for p_ in p.data]) + p.version


def evalutate_packet_expression(p: Packet):
    if isinstance(p.data, int):
        return p.data
    elif p.tag == 0:
        return sum([evalutate_packet_expression(x) for x in p.data])
    elif p.tag == 1:
        return reduce((lambda x, y: x * y), [evalutate_packet_expression(x) for x in p.data])
    elif p.tag == 2:
        return min([evalutate_packet_expression(x) for x in p.data])
    elif p.tag == 3:
        return max([evalutate_packet_expression(x) for x in p.data])
    elif p.tag == 5:
        return 1 if evalutate_packet_expression(p.data[0]) > evalutate_packet_expression(p.data[1]) else 0
    elif p.tag == 6:
        return 1 if evalutate_packet_expression(p.data[0]) < evalutate_packet_expression(p.data[1]) else 0
    elif p.tag == 7:
        return 1 if evalutate_packet_expression(p.data[0]) == evalutate_packet_expression(p.data[1]) else 0


def part_one(input):
    assert compute_sum_version(analyze_packet(hex_to_binary("8A004A801A8002F478"))[0]) == 16
    assert compute_sum_version(analyze_packet(hex_to_binary("620080001611562C8802118E34"))[0]) == 12
    assert compute_sum_version(analyze_packet(hex_to_binary("C0015000016115A2E0802F182340"))[0]) == 23
    assert compute_sum_version(analyze_packet(hex_to_binary("A0016C880162017C3686B18A3D4780"))[0]) == 31
    print(compute_sum_version(analyze_packet(hex_to_binary(input))[0]))


def part_two(input):
    assert evalutate_packet_expression(analyze_packet(hex_to_binary("C200B40A82"))[0]) == 3
    assert evalutate_packet_expression(analyze_packet(hex_to_binary("04005AC33890"))[0]) == 54
    assert evalutate_packet_expression(analyze_packet(hex_to_binary("880086C3E88112"))[0]) == 7
    assert evalutate_packet_expression(analyze_packet(hex_to_binary("CE00C43D881120"))[0]) == 9
    assert evalutate_packet_expression(analyze_packet(hex_to_binary("D8005AC2A8F0"))[0]) == 1
    assert evalutate_packet_expression(analyze_packet(hex_to_binary("F600BC2D8F"))[0]) == 0
    assert evalutate_packet_expression(analyze_packet(hex_to_binary("9C005AC2F8F0"))[0]) == 0
    assert evalutate_packet_expression(analyze_packet(hex_to_binary("9C0141080250320F1802104A08"))[0]) == 1
    print(evalutate_packet_expression(analyze_packet(hex_to_binary(input))[0]))


if __name__ == "__main__":
    t0 = time.time()
    part_one(read_input())
    t1 = time.time()
    part_two(read_input())
    t2 = time.time()
    print("total {total}ms".format(total=t2 - t1))

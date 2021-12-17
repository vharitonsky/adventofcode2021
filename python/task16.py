input_data = "D2FE28"
input_data = open('task16_input').read().strip()


def to_binary(hexa):
    decoder = {
        "0": "0000",
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
        "F": "1111",
    }
    return ''.join(decoder[i] for i in hexa)


def from_bin(bin_str):
    d = 0
    for i, v in enumerate(reversed(bin_str)):
        d += 2 ** i * int(v)
    return d


class Packet:
    type = None
    version = None
    value = None
    children = None

    def __init__(self):
        self.children = []

    def sum_version(self):
        return self.version + sum(child.sum_version() for child in self.children)

    def execute(self):
        if self.type == 0:
            return sum(child.execute() for child in self.children)
        elif self.type == 1:
            product = 1
            for child in self.children:
                product = product * child.execute()
            return product
        elif self.type == 2:
            return min(child.execute() for child in self.children)
        elif self.type == 3:
            return max(child.execute() for child in self.children)
        elif self.type == 4:
            return self.value
        elif self.type == 5:
            return (
                1 if self.children[0].execute() > self.children[1].execute()
                else 0
            )
        elif self.type == 6:
            return (
                1 if self.children[0].execute() < self.children[1].execute()
                else 0
            )
        elif self.type == 7:
            return (
                1 if self.children[0].execute() == self.children[1].execute()
                else 0
            )


def parse_packet(packet_string):
    packet = Packet()
    version_id = packet_string[:3]
    if len(version_id) < 3:
        return None, None
    type_id = packet_string[3:6]
    if len(type_id) < 3:
        return None, None
    type = from_bin(type_id)
    packet.type = type
    version = from_bin(version_id)
    packet.version = version

    if type == 4:
        i = 0
        is_last_group = False
        start_value = i + 6
        full_value = ''
        while not is_last_group:
            value = packet_string[start_value:start_value + 5]
            if len(value) < 5:
                return None, None
            if value[0] == '0':
                is_last_group = True
            full_value += value[1:]
            start_value = start_value + 5
        i = start_value
        packet.value = from_bin(full_value)
        return packet, packet_string[i:]
    else:
        try:
            length_type_id = packet_string[6]
        except IndexError:
            return None, None
        if length_type_id == '0':
            if len(packet_string[7:7 + 15]) < 15:
                return None, None
            packets_length = from_bin(packet_string[7:7 + 15])
            subpacket_string = packet_string[7 + 15:7 + 15 + packets_length]
            while True:
                child, subpacket_string = parse_packet(subpacket_string)
                if child is not None:
                    packet.children.append(child)
                if child is None or not subpacket_string:
                    return packet, packet_string[7 + 15 + packets_length:]
        else:
            packets_number = from_bin(packet_string[7:7 + 11])
            subpacket_string = packet_string[7 + 11:]
            for _ in range(packets_number):
                child,  subpacket_string = parse_packet(subpacket_string)
                packet.children.append(child)
            return packet, subpacket_string


def part_1(transmission):
    packet, _ = parse_packet(transmission)
    return packet.sum_version()


def part_2(transmission):
    packet, _ = parse_packet(transmission)
    return packet.execute()


if __name__ == '__main__':
    print(part_1(to_binary(input_data)))
    print(part_2(to_binary(input_data)))



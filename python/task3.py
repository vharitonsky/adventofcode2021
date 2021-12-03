# data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010
# """.split()
data = [l.strip() for l in open('task3_input').readlines()]


def from_bin(bin_str):
    d = 0
    for i, v in enumerate(reversed(bin_str)):
        d += 2 ** i * int(v)
    return d


def part_1(data):
    gamma = ["0"] * len(data[0])
    epsilon = ["0"] * len(data[0])
    for i in range(0, len(data[0])):
        count_0 = 0
        for line in data:
            if line[i] == "0":
                count_0 += 1
        if count_0 >= len(data)/2:
            gamma[i] = "0"
            epsilon[i] = "1"
        else:
            gamma[i] = "1"
            epsilon[i] = "0"
    return from_bin(gamma) * from_bin(epsilon)


def part_2(data):
    oxygen = ''
    current_data = data
    for i in range(0, len(data[0])):
        if len(current_data) == 1:
            break
        count_0 = 0
        count_1 = 0
        for line in current_data:
            if line[i] == "0":
                count_0 += 1
            else:
                count_1 += 1
        if count_1 >= count_0:
            current_data = [l for l in current_data if l[i] == "1"]
        else:
            current_data = [l for l in current_data if l[i] == "0"]
    oxygen = current_data[0]
    co2 = ''
    current_data = data
    for i in range(0, len(data[0])):
        if len(current_data) == 1:
            break
        count_0 = 0
        count_1 = 0
        for line in current_data:
            if line[i] == "0":
                count_0 += 1
            else:
                count_1 += 1
        if count_1 >= count_0:
            current_data = [l for l in current_data if l[i] == "0"]
        else:
            current_data = [l for l in current_data if l[i] == "1"]
    co2 = current_data[0]
    return from_bin(oxygen) * from_bin(co2)


if __name__ == '__main__':
    print(part_1(data))
    print(part_2(data))

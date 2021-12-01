import sys

example_measurements = [int(line.strip()) for line in open(sys.argv[1]).readlines()]
# example_measurements = [
#     199,
#     200,
#     208,
#     210,
#     200,
#     207,
#     240,
#     269,
#     260,
#     263
# ]


def part_1(measurements):
    incs = 0
    last_m = measurements[0]
    for m in measurements[1:]:
        if m > last_m:
            incs += 1
        last_m = m
    return incs


def part_2(measurements):
    windows = [measurements[0] + measurements[1] + measurements[2]]
    for i, _ in enumerate(measurements[1:]):
        if i > len(measurements) - 3:
            break
        w_next = measurements[i] + measurements[i + 1] + measurements[i + 2]
        windows.append(w_next)
    return part_1(windows)


if __name__ == '__main__':
    print(part_1(example_measurements))
    print(part_2(example_measurements))

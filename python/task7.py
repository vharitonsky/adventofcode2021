# input_data = [int(p) for p in "16,1,2,0,4,2,7,1,2,14".split(',')]
input_data = [int(p) for p in open('task7_input').read().strip().split(',')]


def part_1(positions):
    fuel_consumptions = [0 for i in range(max(positions) + 1)]
    for p_possible in range(max(positions) + 1):
        for p in positions:
            fuel_consumptions[p_possible] += abs(p_possible - p)
    return min(fuel_consumptions)


def part_2(positions):
    fuel_consumptions = [0 for i in range(max(positions) + 1)]
    for p_possible in range(max(positions) + 1):
        for p in positions:
            steps = abs(p_possible - p)
            fuel = sum(i for i in range(1, steps + 1))
            fuel_consumptions[p_possible] += fuel
    return min(fuel_consumptions)


if __name__ == '__main__':
    print(part_1(input_data))
    print(part_2(input_data))

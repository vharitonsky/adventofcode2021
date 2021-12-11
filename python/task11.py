# input_data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526""".split('\n')

input_data = open('task11_input').read().split()

flash_map = {}


def inc_neighbours(rows, i, j):
    for i_n in (-1, 0, 1):
        for j_n in (-1, 0, 1):
            if i_n == 0 and j_n == 0:
                continue
            try:
                ii = i + i_n
                jj = j + j_n
                energy = rows[ii][jj]
            except IndexError:
                continue
            if ii < 0 or jj < 0:
                continue
            rows[ii][jj] = energy = energy + 1
            if energy > 9 and (ii, jj) not in flash_map:
                flash_map[(ii, jj)] = True
                inc_neighbours(rows, ii, jj)


def part_1(input_data, days):
    rows = []
    for line in input_data:
        rows.append([int(octo) for octo in line])
    flashes = 0
    for _ in range(days):
        for i, row in enumerate(rows):
            for j, energy in enumerate(row):
                rows[i][j] += 1
        for i, row in enumerate(rows):
            for j, energy in enumerate(row):
                if energy > 9 and (i, j) not in flash_map:
                    flash_map[(i, j)] = True
                    inc_neighbours(rows, i, j)
        for (i, j) in flash_map.keys():
            rows[i][j] = 0
        flashes += len(flash_map)
        flash_map.clear()
    return flashes


def part_2(input_data):
    rows = []
    total_len = 0
    for line in input_data:
        rows.append([int(octo) for octo in line])
        total_len += len(line)
    print(total_len)
    step = 0
    while True:
        step += 1
        for i, row in enumerate(rows):
            for j, energy in enumerate(row):
                rows[i][j] += 1
        for i, row in enumerate(rows):
            for j, energy in enumerate(row):
                if energy > 9 and (i, j) not in flash_map:
                    flash_map[(i, j)] = True
                    inc_neighbours(rows, i, j)

        if len(flash_map) == total_len:
            return step

        for (i, j) in flash_map.keys():
            rows[i][j] = 0
        flash_map.clear()


if __name__ == '__main__':
    print(part_1(input_data, 100))
    print(part_2(input_data))

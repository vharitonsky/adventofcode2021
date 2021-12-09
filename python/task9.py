# input_data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".split('\n')
input_data = open('task9_input').read().split('\n')


def parse(input_data):
    rows = [[-1 for j in range(len(input_data[0]) + 2)] for i in range(len(input_data) + 2)]
    for i, line in enumerate(input_data, start=1):
        for j, height in enumerate(line, 1):
            rows[i][j] = int(height)
    return rows


def part_1(height_matrix):
    low_points = []
    for i in range(1, len(height_matrix) -1):
        for j in range(1, len(height_matrix[i]) - 1):
            if (
                    (height_matrix[i][j] < height_matrix[i+1][j] or height_matrix[i+1][j] == -1) and
                    (height_matrix[i][j] < height_matrix[i-1][j] or height_matrix[i-1][j] == -1) and
                    (height_matrix[i][j] < height_matrix[i][j + 1] or height_matrix[i][j + 1] == -1) and
                    (height_matrix[i][j] < height_matrix[i][j - 1] or height_matrix[i][j - 1] == -1)
            ):
                low_points.append(height_matrix[i][j])
    return sum([p + 1 for p in low_points])


def part_2(height_matrix):
    low_points = []
    for i in range(1, len(height_matrix) -1):
        for j in range(1, len(height_matrix[i]) - 1):
            if (
                    (height_matrix[i][j] < height_matrix[i+1][j] or height_matrix[i+1][j] == -1) and
                    (height_matrix[i][j] < height_matrix[i-1][j] or height_matrix[i-1][j] == -1) and
                    (height_matrix[i][j] < height_matrix[i][j + 1] or height_matrix[i][j + 1] == -1) and
                    (height_matrix[i][j] < height_matrix[i][j - 1] or height_matrix[i][j - 1] == -1)
            ):
                low_points.append((i, j))

    basins = []
    for p in low_points:
        basin_points = set([p])
        new_basin_points = set([p])
        while new_basin_points:
            next_basin_points = set()
            for bp in new_basin_points:
                points = [(bp[0] + 1, bp[1]), (bp[0] - 1, bp[1]), (bp[0], bp[1] + 1), (bp[0], bp[1] -1)]
                for pp in points:
                    if pp in basin_points:
                        continue
                    height = height_matrix[pp[0]][pp[1]]
                    if height not in (-1, 9):
                        next_basin_points.add(pp)
            basin_points.update(next_basin_points)
            new_basin_points = next_basin_points
        basins.append(basin_points)
    mul = 1
    for b in list(sorted(basins, key=lambda v: len(v), reverse=True))[:3]:
        mul *= len(b)
    return mul


if __name__ == '__main__':
    print(part_1(parse(input_data)))
    print(part_2(parse(input_data)))

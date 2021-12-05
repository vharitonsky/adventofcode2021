from typing import NamedTuple

# data = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2"""
data = open('task5_input').read()


class Point(NamedTuple):
    x: int
    y: int


def parse(input_data):
    coords = []
    max_x = 0
    max_y = 0
    for line in input_data.split('\n'):
        if not line:
            continue
        left, right = line.split(' -> ')
        pair = (
            Point(*[int(n) for n in left.split(',')]),
            Point(*[int(n) for n in right.split(',')])
        )
        for p in pair:
            if p.y > max_y:
                max_y = p.y
            if p.x > max_x:
                max_x = p.x
        coords.append(pair)
    grid = [[0] * (max_x + 1) for i in range(max_y + 1)]
    return coords, grid


def part_1(coords, grid):
    for p1, p2 in coords:
        if p1.x == p2.x:
            start, stop = [p1, p2] if p1.y < p2.y else [p2, p1]
            for i in range(start.y, stop.y + 1):
                grid[i][start.x] += 1
        elif p1.y == p2.y:
            start, stop = [p1, p2] if p1.x < p2.x else [p2, p1]
            for i in range(start.x, stop.x + 1):
                grid[start.y][i] += 1
    for row in grid:
        print(''.join(map(str, row)).replace('0', '.'))
    overlap = 0
    for row in grid:
        for value in row:
            if value > 1:
                overlap += 1
    return overlap


def part_2(coords, grid):
    for p1, p2 in coords:
        if p1.x == p2.x:
            start, stop = [p1, p2] if p1.y < p2.y else [p2, p1]
            for i in range(start.y, stop.y + 1):
                grid[i][start.x] += 1
        elif p1.y == p2.y:
            start, stop = [p1, p2] if p1.x < p2.x else [p2, p1]
            for i in range(start.x, stop.x + 1):
                grid[start.y][i] += 1
        else:
            start, stop = [p1, p2] if p1.y < p2.y else [p2, p1]
            start_x = start.x
            stop_x = stop.x
            step = 1 if start.x < stop.x else - 1
            for i, x in enumerate(range(start_x, stop_x + step, step)):
                for y in list(range(start.y, stop.y + 1))[i:]:
                    grid[y][x] += 1
                    break

    for row in grid:
        print(''.join(map(str, row)).replace('0', '.'))
    overlap = 0
    for row in grid:
        for value in row:
            if value > 1:
                overlap += 1
    return overlap


if __name__ == '__main__':
    print(part_1(*parse(data)))
    print(part_2(*parse(data)))

input_data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".split('\n')
input_data = open('task20_input').read().split('\n')[:-1]


def from_bin(bin_str):
    d = 0
    for i, v in enumerate(reversed(bin_str)):
        d += 2 ** i * int(v)
    return d


def get_neighbours(y, x, image):
    pixels = ''
    for k in (-1, 0, 1):
        for n in (-1, 0, 1):
            new_y = y + k
            new_x = x + n
            if new_x < 0 or new_y < 0:
                pixels += '.'
            else:
                try:
                    pixels += image[new_y][new_x]
                except IndexError:
                    pixels += '.'
    return pixels


def parse(input_data):
    algo = input_data[0]
    image = []
    for row in input_data[2:]:
        image.append([c for c in row])
    return image, algo


def enhance(image, algo):
    changes = []
    for _ in range(9):
        image.insert(0, ['.'] * len(image[0]))
        image.append(['.'] * len(image[0]))
        for row in image:
            row.insert(0, '.')
            row.append('.')

    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            neighbours = get_neighbours(i, j, image)
            algo_index = from_bin(
                neighbours.replace('#', '1').replace('.', '0')
            )
            changes.append((i, j, algo[algo_index]))
    for (i, j, change) in changes:
        image[i][j] = change
    return image


def crop(image):
    crop_top = None
    crop_bottom = None

    line_len = len(image[0])
    for i, line in enumerate(image):
        if line.count('.') == 2:
            crop_top = i + 1
    for i in range(len(image) - 1, 0, -1):
        if image[i].count('#') == line_len:
            continue
        else:
            crop_bottom = i - 1
            break

    crop_left = 0
    for line in image:
        print(''.join(line))

    image = image[crop_top:crop_bottom]
    image_len = len(image)

    while True:
        total = sum(1 if line[crop_left] == '.' else 0 for line in image)
        if total == image_len or total == 0:
            crop_left += 1
        else:
            break

    crop_right = len(image[0]) - 1
    while True:
        total = sum(1 if line[crop_right] == '.' else 0 for line in image)
        if total == image_len or total == 0:
            crop_right -= 1
        else:
            break
    for i, line in enumerate(image):
        image[i] = line[crop_left:crop_right + 1]
    line_len = len(image[0])
    for i, line in enumerate(image):
        if line.count('.') != line_len:
            crop_top = i
            break
    for i in range(len(image) - 1, 0, -1):
        if image[i].count('.') != line_len:
            crop_bottom = i + 1
            break
    image = image[crop_top: crop_bottom]

    for line in image:
        print(''.join(line))
    return image


def part_1(image, algo):
    image = enhance(image, algo)
    image = enhance(image, algo)
    image = crop(image)
    return sum(line.count('#') for line in image)


def part_2(image, algo):
    for i in range(1, 51):
        image = enhance(image, algo)
        if i % 2 == 0:
            image = crop(image)
    return sum(line.count('#') for line in image)


if __name__ == '__main__':
    print(part_1(*parse(input_data)))
    print(part_2(*parse(input_data)))

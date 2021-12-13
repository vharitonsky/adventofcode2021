import itertools
from itertools import permutations

input_data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split('\n')


class Cave:

    def __init__(self, name, is_start=False, is_end=False, is_big=False):
        self.name = name
        self.is_start = is_start
        self.is_end = is_end
        self.is_big = is_big
        self.connected_caves = []

    def __str__(self):
        return f'<{self.name}>'

    def __repr__(self):
        return f'<{self.name}>'


def parse_input(input_data):
    cave_map = {}
    for line in input_data:
        print(line)
        begins, ends = line.split('-')
        cave_map.setdefault(begins, Cave(
            name=begins,
            is_start=begins == 'start',
            is_end=False,
            is_big=begins.isupper(),
        ))
        cave_map.setdefault(ends, Cave(
            name=ends,
            is_start=False,
            is_end=(ends == 'end'),
            is_big=ends.isupper(),
        ))
        cave_map[begins].connected_caves.append(cave_map[ends])
        cave_map[ends].connected_caves.append(cave_map[begins])
    return cave_map


def descend(start_cave, path, cycles):
    if 'end' in path:
        return

    for cave in start_cave.connected_caves:
        if cave.name == 'start':
            continue
        if (start_cave.name, cave.name) not in cycles:
            path.append(cave.name)
            cycles.append((start_cave.name, cave.name))
            descend(cave, path, cycles)
        return


def part_1(cave_map):
    start = cave_map['start']
    paths = []
    cycles = []
    while True:
        new_path = []
        descend(start, new_path, cycles)
        if not new_path:
            break
        paths.append(new_path)
    return paths


def part_2(input_data):
    pass


if __name__ == '__main__':
    print(part_1(parse_input(input_data)))
    print(part_2(input_data))
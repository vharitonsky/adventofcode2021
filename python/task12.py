# input_data = """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc""".split('\n')
input_data = open('task12_input').read().split('\n')


def parse_input(input_data):
    cave_map = {}
    for line in input_data:
        if not line:
            continue
        begins, ends = line.split('-')
        if begins not in cave_map:
            cave_map[begins] = []
        if ends not in cave_map:
            cave_map[ends] = []
        if begins == 'start':
            cave_map[begins].append(ends)
        elif ends == 'start':
            cave_map[ends].append(begins)
        elif begins == 'end':
            cave_map[ends].append(begins)
        elif ends == 'end':
            cave_map[begins].append(ends)
        else:
            cave_map[begins].append(ends)
            cave_map[ends].append(begins)
    return cave_map


def part_1(cave_map):
    paths = []

    def descend(path, visited):
        for connected in cave_map[path[-1]]:
            if connected == 'end':
                paths.append(path + ['end'])
            elif visited.get(connected) and not connected.isupper():
                continue
            else:
                new_visited = visited.copy()
                new_visited[connected] = True
                descend(path + [connected], new_visited)
    descend(['start'], {})
    return len(paths)


def part_2(cave_map):
    paths = []

    def descend(path, visited):
        for connected in cave_map[path[-1]]:
            if connected == 'end':
                paths.append(path + ['end'])
            elif connected.isupper():
                descend(path + [connected], visited.copy())
            elif visited.get(connected):
                if 2 in visited.values():
                    continue
                else:
                    new_visited = visited.copy()
                    new_visited[connected] += 1
                    descend(path + [connected], new_visited)
            else:
                new_visited = visited.copy()
                new_visited[connected] = 1
                descend(path + [connected], new_visited)
    descend(['start'], {})
    return len(paths)


if __name__ == '__main__':
    print(part_1(parse_input(input_data)))
    print(part_2(parse_input(input_data)))

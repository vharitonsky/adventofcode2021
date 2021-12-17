from collections import defaultdict
from queue import PriorityQueue

input_data = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split('\n')[1:]
input_data = open('task15_input').read().split('\n')[:-1]

inf = float('inf')


def part1(input_data):
    graph = defaultdict(dict)
    for i, line in enumerate(input_data):
        for j, risk in enumerate(line):
            if j + 1 < len(line):
                graph[(j, i)][(j + 1, i)] = int(line[j + 1])
            if j - 1 >= 0:
                graph[(j, i)][(j - 1, i)] = int(line[j - 1])
            if i - 1 >= 0:
                graph[(j, i)][(j, i - 1)] = int(input_data[i - 1][j])
            if i + 1 < len(input_data):
                graph[(j, i)][(j, i + 1)] = int(input_data[i + 1][j])
    right_bottom = (len(input_data[0]) - 1, len(input_data) - 1)
    return graph, right_bottom


def part2(input_data):
    offset = 0
    original_length = len(input_data)
    for step in range(1, 5):
        new_lines = []
        for i, line in enumerate(input_data[offset:]):
            new_line = []
            for value in line:
                new_value = str(int(value) + 1) if value != '9' else '1'
                new_line.append(new_value)
            new_lines.append(''.join(new_line))
        input_data.extend(new_lines)
        offset = original_length * step
    original_length = len(input_data[0])
    offset = 0
    for step in range(1, 5):
        for i, line in enumerate(input_data):
            new_segment = ''
            for value in line[offset: offset + original_length]:
                new_value = str(int(value) + 1) if value != '9' else '1'
                new_segment += new_value
            input_data[i] += new_segment
        offset = original_length * step
    graph = defaultdict(dict)
    for i, line in enumerate(input_data):
        for j, risk in enumerate(line):
            if j + 1 < len(line):
                graph[(j, i)][(j + 1, i)] = int(line[j + 1])
            if j - 1 >= 0:
                graph[(j, i)][(j - 1, i)] = int(line[j - 1])
            if i - 1 >= 0:
                graph[(j, i)][(j, i - 1)] = int(input_data[i - 1][j])
            if i + 1 < len(input_data):
                graph[(j, i)][(j, i + 1)] = int(input_data[i + 1][j])
    right_bottom = (len(input_data[0]) - 1, len(input_data) - 1)
    return graph, right_bottom


def dijkstra(graph, right_bottom):
    visited = set()
    start_vertex = (0, 0)
    cost_to_vertex = {c: float('inf') for c in graph}
    cost_to_vertex[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.add(current_vertex)
        if current_vertex == right_bottom:
            break
        for neighbor, distance in graph[current_vertex].items():
            if neighbor not in visited:
                old_cost = cost_to_vertex[neighbor]
                new_cost = cost_to_vertex[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    cost_to_vertex[neighbor] = new_cost
    return cost_to_vertex[right_bottom]


if __name__ == '__main__':
    print(dijkstra(*part1(input_data)))
    print(dijkstra(*part2(input_data)))

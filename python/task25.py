input_data = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>""".split('\n')

input_data = open('task25_input').read().split('\n')[:-1]


def part_1(trench):
    steps = 0
    for i in range(len(trench)):
        trench[i] = list(trench[i])
    for line in trench:
        print(''.join(line))
    print()

    while True:
        repositions_right = []
        repositions_bottom = []
        for i, line in enumerate(trench):
            for j, cell in enumerate(line):
                if trench[i][j] == '>':
                    right = j + 1
                    if right == len(line):
                        right = 0
                    if trench[i][right] == '.':
                        repositions_right.append(((i, j), (i, right), '>'))

        for (from_i, from_j), (to_i, to_j), cucumber in repositions_right:
            trench[from_i][from_j] = '.'
            trench[to_i][to_j] = cucumber

        for i, line in enumerate(trench):
            for j, cell in enumerate(line):
                if trench[i][j] == 'v':
                    bottom = i + 1
                    if bottom == len(trench):
                        bottom = 0
                    if trench[bottom][j] == '.':
                        repositions_bottom.append(((i, j), (bottom, j), 'v'))

        for (from_i, from_j), (to_i, to_j), cucumber in repositions_bottom:
            trench[from_i][from_j] = '.'
            trench[to_i][to_j] = cucumber
        steps += 1
        if not repositions_right and not repositions_bottom:
            break
        for line in trench:
            print(''.join(line))
        print()

    return steps


if __name__ == '__main__':
    print(part_1(input_data))

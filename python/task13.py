input_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split('\n')
input_data = open('task13_input').read().split('\n')


class XFold:

    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f'<X={self.x}>'


class YFold:

    def __init__(self, y):
        self.y = y

    def __repr__(self):
        return f'<Y={self.y}>'


def parse(input_data):
    dots = []
    folds = []
    it = iter(input_data)
    for line in it:
        if not line:
            break
        x, y = line.split(',')
        dots.append((int(x), int(y)))
    max_x = sorted(dots, key=lambda d: d[0])[-1][0]
    max_y = sorted(dots, key=lambda d: d[1])[-1][1]
    matrix = []
    for i in range(max_y + 1):
        matrix.append([0 for _ in range(max_x + 1)])

    for d in dots:
        matrix[d[1]][d[0]] = 1
    for line in it:
        if not line:
            break
        if 'x' in line:
            x = int(line.split('=')[1])
            folds.append(XFold(x))
        else:
            y = int(line.split('=')[1])
            folds.append(YFold(y))
    return matrix, folds


def _debug(matrix):
    for r in matrix:
        print(''.join(map(str, r)).replace('0', ' ').replace('1', '#'))
    print()


def _count(matrix):
    return sum(sum(r) for r in matrix)


def solve(matrix, folds, steps):
    for fold in folds[:steps]:
        if isinstance(fold, YFold):
            y = fold.y
            start = len(matrix[:y]) - len(matrix[y + 1:])
            for i, ii in enumerate(range(start, y)):
                mirror_y = len(matrix) - i - 1
                for k, x in enumerate(matrix[mirror_y]):
                    matrix[ii][k] = matrix[ii][k] or x
            matrix = matrix[:y]
        elif isinstance(fold, XFold):
            x = fold.x
            start = len(matrix[0][:x]) - len(matrix[0][x + 1:])
            for i, row in enumerate(matrix):
                for j, jj in enumerate(range(start, x)):
                    mirror_x = len(row) - j - 1
                    row[jj] = row[jj] or row[mirror_x]
                matrix[i] = matrix[i][:x]
    return matrix


if __name__ == '__main__':
    print(_count(solve(*parse(input_data), steps=1)))
    _debug(solve(*parse(input_data), steps=20))


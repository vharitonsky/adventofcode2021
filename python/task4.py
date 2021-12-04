example_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class BingoBoard:
    size = 5

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def play(self, numbers):
        marked_line = ' '.join(['x'] * self.size)
        for turn, number in enumerate(numbers):
            for i, row in enumerate(self.rows):
                self.rows[i] = row.replace(number, 'x')
            for i, column in enumerate(self.columns):
                self.columns[i] = column.replace(number, 'x')
            if marked_line in self.rows or marked_line in self.columns:
                return turn, self.calculate_win(), int(number)

        return -1, 0

    def calculate_win(self):
        return sum(
            sum((int(n) for n in row.split() if n != 'x'))
            for row in self.rows
        )

    def __str__(self):
        return '\n'.join(self.rows) + '\n'

    @classmethod
    def parse(cls, block):
        rows = []
        columns = [[] for s in range(cls.size)]
        for line in block:
            numbers = line.split()
            for i, n in enumerate(numbers):
                if int(n) < 10:
                    numbers[i] = '0' + n
            rows.append(' '.join(numbers))
            for i, n in enumerate(numbers):
                columns[i].append(n)
        for i, col in enumerate(columns):
            columns[i] = ' '.join(col)
        return BingoBoard(rows, columns)


def parse_boards(input_data):
    lines = input_data.split('\n')
    numbers = lines[0].split(',')
    for i, n in enumerate(numbers):
        if int(n) < 10:
            numbers[i] = '0' + n
    boards = []
    block = []
    for line in lines[2:]:
        if line == '':
            boards.append(BingoBoard.parse(block))
            block = []
        else:
            block.append(line)
    boards.append(BingoBoard.parse(block))
    return numbers, boards


def part_1(numbers, boards):
    results = sorted(
        [board.play(numbers) for board in boards],
        key=lambda res: res[0]
    )
    return [res[1] * res[2] for res in results if res[0] != -1]


def part_2(numbers, boards):
    results = sorted(
        [board.play(numbers) for board in boards],
        key=lambda res: res[0], reverse=True
    )
    return [res[1] * res[2] for res in results if res[0] != -1]


if __name__ == '__main__':
    # print(part_1(example_input))
    print(part_1(*parse_boards(open('task4_input').read())))
    print(part_2(*parse_boards(open('task4_input').read())))

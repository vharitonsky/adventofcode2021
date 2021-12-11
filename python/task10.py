# input_data = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""".split('\n')

input_data = open('task10_input').read().split('\n')


SCORES_CORRUPT = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

SCORES_INCOMPLETE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

OPEN = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

CLOSE = {value: key for key, value in OPEN.items()}


def part_1(input_data):
    score = 0
    for line in input_data:
        stack = []
        for char in line:
            if char in CLOSE:
                if OPEN[stack[-1]] == char:
                    stack.pop()
                else:
                    score += SCORES_CORRUPT[char]
                    break
            else:
                stack.append(char)
    return score


def part_2(input_data):
    incomplete = []
    for line in input_data:
        stack = []
        for char in line:
            if char in CLOSE:
                if OPEN[stack[-1]] == char:
                    stack.pop()
                else:
                    break
            else:
                stack.append(char)
        else:
            incomplete.append(stack)
    scores = []
    for stack in incomplete:
        stack_score = 0
        for char in stack[::-1]:
            stack_score *= 5
            stack_score += SCORES_INCOMPLETE[OPEN[char]]
        scores.append(stack_score)
    return list(sorted(scores))[len(scores)//2]


if __name__ == '__main__':
    print(part_1(input_data))
    print(part_2(input_data))

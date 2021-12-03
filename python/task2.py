# instructions = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2""".split('\n')

instructions = list(open('task2_input').readlines())


def part_1(instructions):
    horizontal = 0
    vertical = 0
    for instr in instructions:
        if instr.startswith("forward "):
            horizontal += int(instr.split()[1])
        elif instr.startswith("down "):
            vertical += int(instr.split()[1])
        else:
            vertical -= int(instr.split()[1])
    return horizontal * vertical


def part_2(instructions):
    aim = 0
    horizontal = 0
    vertical = 0
    for instr in instructions:
        if instr.startswith("forward "):
            horizontal += int(instr.split()[1])
            vertical += int(instr.split()[1]) * aim
        elif instr.startswith("down "):
            aim += int(instr.split()[1])
        else:
            aim -= int(instr.split()[1])
    return horizontal * vertical


if __name__ == '__main__':
    print(part_1(instructions))
    print(part_2(instructions))

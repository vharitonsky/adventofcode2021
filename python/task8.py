# input_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split('\n')

input_data = open('task8_input').readlines()

one_segments = 2
four_segments = 4
seven_segments = 3
eight_segments = 7

UNIQUE_SEGMENTS = [one_segments, four_segments, seven_segments, eight_segments]


def part_1(input_data):
    count = 0
    for line in input_data:
        _, output = line.split(' | ')
        for digit in output.split():
            if len(digit) in UNIQUE_SEGMENTS:
                count += 1
    return count


def part_2(input_data):
    total = 0
    for line in input_data:
        patterns, output = line.split(' | ')
        top_right = None
        bottom_right = None
        top_left = None
        middle = None
        bottom_left = None
        bottom = None

        zero_pattern = None
        one_pattern = None
        four_pattern = None
        seven_pattern = None
        eight_pattern = None

        patterns = [''.join(sorted(p)) for p in sorted(patterns.split(), key=lambda p: len(p))]

        for pattern in patterns:
            if len(pattern) == 2:
                one_pattern = pattern
            if len(pattern) == 3:
                seven_pattern = pattern
            if len(pattern) == 4:
                four_pattern = pattern
            if len(pattern) == 7:
                eight_pattern = pattern

        top = seven_pattern.replace(one_pattern[0], '').replace(one_pattern[1], '')
        for p in one_pattern:
            if eight_pattern.replace(p, '') in patterns:
                top_right = p
                bottom_right = one_pattern.replace(top_right, '')
                break

        top_left_middle = four_pattern.replace(one_pattern[0], '').replace(one_pattern[1], '')

        for p in top_left_middle:
            if eight_pattern.replace(p, '') in patterns:
                zero_pattern = eight_pattern.replace(p, '')
                middle = p
                top_left = top_left_middle.replace(middle, '')
                break
        left_bottom = zero_pattern.replace(top, '').replace(top_right, '').replace(bottom_right, '').replace(middle, '').replace(top_left, '')
        for p in left_bottom:
            if eight_pattern.replace(p, '') in patterns:
                bottom_left = p
                bottom = left_bottom.replace(p, '')
                break

        decoder_raw = {
            (top, bottom, bottom_left, bottom_right, top_right, top_left): 0,
            (bottom_right, top_right): 1,
            (top, bottom, bottom_left, top_right, middle): 2,
            (top, bottom, bottom_right, top_right, middle): 3,
            (bottom_right, middle, top_right, top_left): 4,
            (top, bottom, top_left, bottom_right, middle): 5,
            (top, bottom, bottom_left, bottom_right, top_left, middle): 6,
            (top, bottom_right, top_right): 7,
            (top, bottom, bottom_left, bottom_right, top_right, top_left, middle): 8,
            (top, bottom, bottom_right, top_right, top_left, middle): 9,
        }
        decoder = {
            tuple(sorted(key)): value
            for key, value in decoder_raw.items()
        }

        numbers = []
        for digit in output.split():
            numbers.append(str(decoder[tuple(sorted(digit))]))
        number = int(''.join(numbers))
        total += number

    return total


if __name__ == '__main__':
    print(part_1(input_data))
    print(part_2(input_data))

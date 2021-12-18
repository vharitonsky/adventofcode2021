input_data = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]""".split('\n')
input_data = open('task18_input').read().split('\n')[:-1]


class Value:
    children = None
    value = None

    def __init__(self, value=None, children=None, level=None):
        self.value = value
        self.children = children or []
        self.level = level

    def explodes(self):
        return bool(
            self.level == 4 and
            self.children and
            self.children[0].value is not None and
            self.children[1].value is not None
        )

    def splits(self):
        return self.value and self.value >= 10

    def __repr__(self):
        if self.children:
            return f"[{self.children[0]}, {self.children[1]}]"
        else:
            return str(self.value)

    __str__ = __repr__

    def mag(self):
        if not self.children:
            return self.value
        else:
            return 3 * self.children[0].mag() + 2 * self.children[1].mag()

    def inc_level(self,):
        self.level = self.level + 1
        for child in self.children:
            child.inc_level()
        return self

    def __add__(self, other):
        return Value(
            level=0,
            children=[self.inc_level(), other.inc_level()]
        )


def reduce(flat_list):
    for value in flat_list:
        if value.explodes():
            left_number = value.children[0].value
            right_number = value.children[1].value
            value_index = flat_list.index(value)
            for first_left in flat_list[value_index:0:-1]:
                if first_left.value is not None:
                    first_left.value += left_number
                    break

            for first_right in flat_list[value_index + 3:]:
                if first_right.value is not None:
                    first_right.value += right_number
                    break
            value.value = 0
            value.children = []
            return True
    for value in flat_list:
        if value.splits():
            left_child = Value(level=value.level + 1, value=value.value//2)
            right_child = Value(level=value.level + 1, value=value.value - value.value//2)
            value.value = None
            value.children = [left_child, right_child]
            return True
    return False


def parse_value(value_list, level=0):
    parsed_values = []
    for v in value_list:
        if isinstance(v, int):
            parsed_values.append(Value(value=v, level=level))
        else:
            parsed_values.append(Value(level=level, children=parse_value(v, level + 1)))
    return parsed_values


def parse(input_data):
    values = []
    for line in input_data:
        values.append(Value(level=0, children=parse_value(eval(line), level=1)))
    return values


def make_list(value, flat_list):
    flat_list.append(value)
    if value.children:
        for child in value.children:
            make_list(child, flat_list)


def part_1(values):
    acc = values[0]
    for val in values[1:]:
        acc += val
        while True:
            flat_list = []
            make_list(acc, flat_list)
            if not reduce(flat_list):
                break
    return acc.mag()


def part_2(input_data):
    max_mag = 0
    for i in range(len(input_data)):
        for j in range(len(input_data)):
            if i == j:
                continue
            value_sum = parse([input_data[i]])[0] + parse([input_data[j]])[0]
            while True:
                flat_list = []
                make_list(value_sum, flat_list)
                if not reduce(flat_list):
                    break
            new_mag = value_sum.mag()
            if new_mag > max_mag:
                max_mag = new_mag
    return max_mag


if __name__ == '__main__':
    print(part_1(parse(input_data)))
    print(part_2(input_data))

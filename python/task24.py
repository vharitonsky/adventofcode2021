input_data = """inp x
mod x 4""".split('\n')
input_data = open('task24_input').read().split('\n')[:-1]


def build_func(input_data):
    built_func = 'z = 0\nx = 0\ny = 0\nw = 0\n'
    variables = set()
    for line in input_data:
        if line.startswith('inp'):
            var = line.split()[1]
            variables.add(var)
            built_func += f'{var} = data.pop()\n'
        elif line.startswith('add'):
            _, left, right = line.split()
            variables.add(left)
            built_func += f'{left} = {left} + {right}\n'
        elif line.startswith('mul'):
            _, left, right = line.split()
            variables.add(left)
            built_func += f'{left} = {left} * {right}\n'
        elif line.startswith('div'):
            _, left, right = line.split()
            variables.add(left)
            built_func += f'{left} = int({left}/{right})\n'
        elif line.startswith('mod'):
            _, left, right = line.split()
            variables.add(left)
            built_func += f'{left} = {left} % {right}\n'
        elif line.startswith('eql'):
            _, left, right = line.split()
            variables.add(left)
            built_func += f'{left} = int({left} == {right})\n'
    variables = list(variables)
    built_func += 'print(' + ''.join(f"'{var}=', {var} ," for var in variables) + ')\n'
    built_func += 'res[0] = z\n'
    print(built_func)
    raise Exception()
    obj = compile(built_func, filename='alu.py', mode='exec')
    return obj


def find_valid_number():
    data = 99999999999999
    while True:
        current_data = str(data)
        if len(current_data) < 14:
            raise Exception("XXX")
        # print(current_data)
        if '0' in current_data:
            data -= 1
            continue
        current_data = [int(i) for i in current_data]
        z = 0
        x = 0
        y = 0
        w = 0
        w = current_data[0]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/1)
        x = x + 11
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 5
        y = y * x
        z = z + y
        w = current_data[1]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/1)
        x = x + 13
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 5
        y = y * x
        z = z + y
        w = current_data[2]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/1)
        x = x + 12
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 1
        y = y * x
        z = z + y
        w = current_data[3]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/1)
        x = x + 15
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 15
        y = y * x
        z = z + y
        w = current_data[4]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/1)
        x = x + 10
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 2
        y = y * x
        z = z + y
        w = current_data[5]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/26)
        x = x + -1
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 2
        y = y * x
        z = z + y
        w = current_data[6]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/1)
        x = x + 14
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 5
        y = y * x
        z = z + y
        w = current_data[7]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/26)
        x = x + -8
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 8
        y = y * x
        z = z + y
        w = current_data[8]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/26)
        x = x + -7
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 14
        y = y * x
        z = z + y
        w = current_data[9]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/26)
        x = x + -8
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 12
        y = y * x
        z = z + y
        w = current_data[10]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/1)
        x = x + 11
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 7
        y = y * x
        z = z + y
        w = current_data[11]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/26)
        x = x + -2
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 14
        y = y * x
        z = z + y
        w = current_data[12]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/26)
        x = x + -2
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 13
        y = y * x
        z = z + y
        w = current_data[13]
        x = x * 0
        x = x + z
        x = x % 26
        z = int(z/26)
        x = x + -13
        x = int(x == w)
        x = int(x == 0)
        y = y * 0
        y = y + 25
        y = y * x
        y = y + 1
        z = z * y
        y = y * 0
        y = y + w
        y = y + 6
        y = y * x
        z = z + y
        if z == 0:
            return current_data
        else:
            data -= 1


def part_1(input_data):
    return find_valid_number()


if __name__ == '__main__':
    print(part_1(input_data))

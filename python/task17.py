# input_data = "target area: x=20..30, y=-10..-5"
input_data = "target area: x=48..70, y=-189..-148"


def parse(input_data):
    x_range, y_range = input_data.split(': ')[1].split(', ')
    x_min, x_max = map(int, x_range.split('=')[1].split('..'))
    y_min, y_max = map(int, y_range.split('=')[1].split('..'))
    return (x_min, x_max), (y_min, y_max)


def simulate_shooting(xv, yv, x_range, y_range):
    x, y = 0, 0
    max_y = 0
    while True:
        if x > x_range[1]:
            return max_y, False
        if y < y_range[0]:
            return max_y, False
        if y >= y_range[0] and y <= y_range[1] and x >= x_range[0] and x <= x_range[1]:
            return max_y, True
        y = y + yv
        if y > max_y:
            max_y = y
        x = x + xv
        if xv > 0:
            xv -= 1
        yv -= 1


def part_1(x_range, y_range):
    max_y = 0
    for xv in range(-100, 100):
        for yv in range(1000):
            new_max_y, hit = simulate_shooting(xv, yv, x_range, y_range)
            if hit and new_max_y > max_y:
                max_y = new_max_y
    return max_y


def part_2(x_range, y_range):
    velocities = []
    for xv in range(-100, 100):
        for yv in range(-1000, 1000):
            new_max_y, hit = simulate_shooting(xv, yv, x_range, y_range)
            if hit:
                velocities.append((xv, yv))
    return len(velocities)


if __name__ == '__main__':
    print(part_1(*parse(input_data)))
    print(part_2(*parse(input_data)))

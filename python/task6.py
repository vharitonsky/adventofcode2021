# input_data = [int(i) for i in """3,4,3,1,2""".split(',')]
input_data = [int(i) for i in open('task6_input').read().strip().split(',')]


class Fish:

    timer: int

    def __init__(self, timer):
        self.timer = timer

    def tick(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return Fish(timer=8)


def part_1(timers, days):
    school = []
    for t in timers:
        school.append(Fish(t))
    for i in range(days):
        new_fish = []
        for f in school:
            spawn = f.tick()
            if spawn:
                new_fish.append(spawn)
        school.extend(new_fish)
    return len(school)


def part_2(timers, days):
    fish = [0] * 9
    for t in timers:
        fish[t] += 1
    for i in range(days):
        new_fish = fish[0]
        old_fish = fish[0]
        for j in range(8):
            fish[j] = fish[j + 1]
        fish[8] = new_fish
        fish[6] += old_fish
    return sum(fish)


if __name__ == '__main__':
    print(part_1(input_data, 80))
    print(part_2(input_data, 256))

import re
from collections import defaultdict
from itertools import permutations

input_data = open('task19_input_example').read().split('\n')
# input_data = open('task19_input').read().split('\n')


class Beacon:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"<Beacon {self.x} {self.y} {self.z}>"

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x or self.y == other.y or self.z != other.z

    def __add__(self, other):
        return Beacon(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Beacon(self.x - other.x, self.y - other.y, self.z - other.z)

    def orientations(self):
        for x, y, z in permutations((self.x, self.y, self.z), 3):
            yield Beacon(x, y, z)
            yield Beacon(-x, y, -z)
            yield Beacon(-x, -y, z)
            yield Beacon(x, -y, -z)

    __str__ = __repr__


class Scanner:
    def __init__(self, id, beacons):
        self.id, self.beacons = id, beacons

    def beacon_combinations(self):
        for b in self.beacons:
            for orientation in b.orientations():
                yield orientation

    def __repr__(self):
        return f"<Scanner {self.id}>"
    __str__ = __repr__


def parse(input_data):
    scanners = []
    beacons = []
    scanner_id = None
    for line in input_data:
        if line.startswith('--'):
            scanner_id = re.sub(r'[^\d]+', '', line)
        elif not line:
            scanners.append(Scanner(id=scanner_id, beacons=beacons))
            beacons = []
        else:
            beacons.append(Beacon(*map(int, line.split(','))))
    if scanner_id:
        scanners.append(Scanner(id=scanner_id, beacons=beacons))
    return scanners


def part_1(scanners):
    combs_1 = {beacon for beacon in scanners[0].beacon_combinations()}
    combs_2 = {beacon for beacon in scanners[1].beacon_combinations()}
    diff_count = defaultdict(int)
    for comb_1 in combs_1:
        for comb_2 in combs_2:
            diff_count[comb_1 - comb_2] += 1
    diff, count = sorted(
        diff_count.items(),
        key=lambda key_count: key_count[1],
        reverse=True
    )[0]

    for beacon in combs_1:
        if (beacon - diff) in combs_2:
            print(beacon)

    for beacon in combs_2:
        if (beacon + diff) in combs_1:
            print(beacon)

    return scanners


if __name__ == '__main__':
    print(part_1(parse(input_data)))

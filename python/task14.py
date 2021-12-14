from collections import defaultdict

# input_data = """NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""".split('\n')
input_data = open('task14_input').read().split('\n')[:-1]


def parse(input_data):
    it = iter(input_data)
    template = next(it)
    next(it)
    rules_map = {}
    for r in it:
        key, value = r.split(' -> ')
        rules_map[(key[0], key[1])] = value
    return template, rules_map


def count_template(template):
    counts = []
    for i in set(template):
        counts.append((i, template.count(i)))
    counts = sorted(counts, key=lambda c: c[1])
    return counts[-1][1] - counts[0][1]


def part_1(template, rules_map, steps):
    for s in range(steps):
        new_template = ''
        insert = None
        i = 0
        while True:
            if insert:
                new_template += insert
                insert = None
            else:
                new_template += template[i]
                if (template[i], template[i + 1]) in rules_map:
                    insert = rules_map[(template[i], template[i + 1])]
                i += 1
            if i == len(template) - 1:
                if insert:
                    new_template += insert
                new_template += template[i]
                break
        template = new_template
        count_template(template)
    return count_template(template)


def part_2(template, rules_map, steps):
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[(template[i], template[i + 1])] += 1
    elements = defaultdict(int)
    for n in template:
        elements[n] += 1
    for s in range(steps):
        new_pairs = defaultdict(int)
        breaking_pairs = defaultdict(int)
        for p, count in pairs.items():
            if count == 0:
                continue
            if p in rules_map:
                insert = rules_map[p]
                elements[insert] += count
                new_pairs[(p[0], insert)] += count
                new_pairs[(insert, p[1])] += count
                breaking_pairs[p] = count
        for p, count in breaking_pairs.items():
            pairs[p] -= count
        for p, count in new_pairs.items():
            pairs[p] += count

    counts = sorted(elements.items(), key=lambda c: c[1])
    return counts[-1][1] - counts[0][1]


if __name__ == '__main__':
    print(part_1(*parse(input_data), 10))
    print(part_2(*parse(input_data), 40))

import re
import time
from collections import Counter


def read_input():
    insertions = dict()
    #     with open("day14/test.txt") as file:
    with open("data/day14.txt") as file:
        template = next(file).strip()
        next(file)
        for l in file:
            l = l.strip()
            insertions[l.split(" -> ")[0]] = l.split(" -> ")[1]

    return template, insertions


def find_all(string, patter):
    return [m.start() for m in re.finditer(patter, string)]


def insert_char_in_string(string, c, pos):
    return string[:pos + 1] + c + string[pos + 1:]


def part_one(input, steps):
    template, insertions = input
    for s in range(steps):
        indices = list()
        for i in range(len(template) - 1):
            pattern = template[i] + template[i + 1]
            if pattern in insertions:
                indices.insert(0, (i, insertions[pattern]))

        for i in range(len(indices)):
            template = insert_char_in_string(template, indices[i][1], indices[i][0])

    count = Counter(list(template))
    print(max(count.values()) - min(count.values()))


def part_one_qick(input, steps):
    template, insertions = input
    count = Counter(template)
    pairs = [template[i] + template[i + 1] for i in range(len(template) - 1)]
    for s in range(steps):
        new_pars = list()
        for p in pairs:
            count[insertions[p]] += 1
            c = insertions[p]
            new_pars.append(p[0] + c)
            new_pars.append(c + p[1])

        pairs = new_pars
    print(max(count.values()) - min(count.values()))


def part_two(input, steps):
    pass


if __name__ == "__main__":
    t0 = time.time()
    part_one(read_input(), steps=10)
    t1 = time.time()
    part_one_qick(read_input(), steps=10)
    t2 = time.time()
    part_two(read_input(), steps=10)
    t3 = time.time()
    print("Total {total}ms".format(total=t3 - t0))
    print()
    print("One       {total}ms".format(total=t1 - t0))
    print("One quick {total}ms".format(total=t2 - t1))
    print("Two       {total}ms".format(total=t3 - t2))

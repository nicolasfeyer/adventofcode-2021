import re
import time
from collections import Counter


def read_input():
    rules = dict()
    # with open("day14/test.txt") as file:
    with open("data/day14.txt") as file:
        template = next(file).strip()
        next(file)
        for l in file:
            l = l.strip()
            rules[l.split(" -> ")[0]] = l.split(" -> ")[1]

    return template, rules


def insert_char_in_string(string, c, pos):
    return string[:pos + 1] + c + string[pos + 1:]


def part_one_two_naive(input, steps):
    template, rules = input
    for s in range(steps):
        indices = list()
        for i in range(len(template) - 1):
            pattern = template[i] + template[i + 1]
            if pattern in rules:
                indices.insert(0, (i, rules[pattern]))

        for i in range(len(indices)):
            template = insert_char_in_string(template, indices[i][1], indices[i][0])

    count = Counter(list(template))
    print(max(count.values()) - min(count.values()))


def part_one_two_quicker(input, steps):
    template, rules = input
    count = Counter(template)
    pairs = [template[i] + template[i + 1] for i in range(len(template) - 1)]
    for s in range(steps):
        new_pars = list()
        for p in pairs:
            count[rules[p]] += 1
            c = rules[p]
            new_pars.append(p[0] + c)
            new_pars.append(c + p[1])

        pairs = new_pars
    print(max(count.values()) - min(count.values()))


def part_one_two_optimal(input, steps):
    template, rules = input

    pair_counter = Counter(x + y for x, y in zip(template, template[1:]))  # count of pair in the original template

    chars_count = Counter(template)  # count of char in the original template
    for s in range(steps):
        new_counter = Counter()  # define a new counter for each step

        for (x, y), v in pair_counter.items():  # for each pair
            c = rules[x + y]  # find the resulting char
            chars_count[c] += v  # increment char counter

            # preparing for next iteration
            new_counter[x + c] += v  # increment first pair generated (for next iter)
            new_counter[c + y] += v  # increment second pair generated

        # replace with the new counter
        pair_counter = new_counter

    print(max(chars_count.values()) - min(chars_count.values()))


if __name__ == "__main__":
    t0 = time.time()
    part_one_two_optimal(read_input(), steps=10)
    t1 = time.time()
    part_one_two_optimal(read_input(), steps=40)
    t2 = time.time()
    print("Total {total}ms".format(total=t2 - t0))

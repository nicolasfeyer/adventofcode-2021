import numpy as np


def read_input():
    return np.array([int(x) for x in next(open("data/day7.txt", "r")).split(",")])


def cum_sum(n):
    return np.arange(1, n + 1).sum()


def part_one_two(positions, part_two=False):
    all_pos = np.arange(positions.min(), positions.max() + 1)

    results = all_pos.copy()

    if part_two:
        cum_sum_v = np.vectorize(cum_sum)

    for i in range(len(all_pos)):
        if part_two:
            results[i] = cum_sum_v(np.absolute(positions - all_pos[i])).sum()
        else:
            results[i] = np.sum(np.absolute(positions - all_pos[i]))
    print(results.min())


if __name__ == "__main__":
    part_one_two(read_input())
    part_one_two(read_input(), part_two=True)

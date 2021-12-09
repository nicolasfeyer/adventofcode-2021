import numpy as np


def read_input():
    # l = list()
    # for i in range(12):
    #     l.append([int(x[i]) for x in open("input.txt", "r").readlines()])
    # return l, [x.strip() for x in open("input.txt", "r").readlines()]
    return np.genfromtxt('data/day3.txt', delimiter=1, dtype=int, usecols=range(12))
    # return np.genfromtxt('ex.txt', delimiter=1, dtype=int, usecols=range(5))


def part_one(matrix):
    gamma_b = ""
    epsilon_b = ""
    for bc in matrix.T:
        gamma_b += "0" if sum(bc) < 500 else "1"
        epsilon_b += "0" if sum(bc) > 500 else "1"

    print(int(gamma_b, 2) * int(epsilon_b, 2))


def part_two(matrix):
    oxy = ""
    co2 = ""

    mask_oxy = np.array([True] * 1000)
    mask_co2 = np.array([True] * 1000)

    i = 0
    for col in matrix.T:
        most_common = 0 if sum(col[np.where(mask_oxy)]) < len(col[np.where(mask_oxy)]) / 2 else 1

        mask_oxy &= (col == most_common)

        if len(np.where(mask_oxy)[0]) == 1:
            oxy = matrix[np.where(mask_oxy)[0][0]]
            break

    for col in matrix.T:
        least_common = 0 if sum(col[np.where(mask_co2)]) >= len(col[np.where(mask_co2)]) / 2 else 1

        mask_co2 &= (col == least_common)

        if len(np.where(mask_co2)[0]) == 1:
            co2 = matrix[np.where(mask_co2)[0][0]]
            break

        i += 1

    print(int(''.join([str(x) for x in oxy]), 2) * int(''.join([str(x) for x in co2]), 2))


if __name__ == "__main__":
    part_one(read_input())
    part_two(read_input())

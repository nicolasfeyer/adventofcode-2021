import time
from typing import Optional, Tuple

import numpy as np


def read_input():
    return np.array([[[y, False] for y in x] for x in np.genfromtxt('data/day11.txt', delimiter=1, dtype=int)])
    # return np.array([[[y, False] for y in x] for x in np.genfromtxt('day11/test1.txt', delimiter=1, dtype=int)])


def safe_get_cell(i, j, m, n) -> Optional[Tuple]:
    return None if i < 0 or i >= m or j < 0 or j >= n else (i, j)


def get_8_adjacent(i, j, m, n):
    adjacent_indices = []

    for i_i in [-1, 0, 1]:
        for j_j in [-1, 0, 1]:
            if not (i_i == 0 and j_j == 0):
                pos: Optional[Tuple] = safe_get_cell(i + i_i, j + j_j, m, n)
                if pos: adjacent_indices.append(pos)

    return adjacent_indices


def flashV2(matrix):
    m, n = matrix.shape[0:2]
    nbr_flashes = 0
    while len(matrix[np.where(matrix > 9)]) > 0:
        for i in range(m):
            for j in range(n):
                if matrix[i][j][0] > 9:
                    nbr_flashes += 1
                    matrix[i][j][1] = 1
                    matrix[i][j][0] = 0
                    adjacent_indices = get_8_adjacent(i, j, m, n)
                    for ii, jj in adjacent_indices:
                        if matrix[ii][jj][1] != 1:
                            matrix[ii][jj][0] += 1

    return nbr_flashes


# broken
def flash_recur(i, j, matrix):
    m, n = matrix.shape[0:2]
    nbr_flash = 0

    if matrix[i][j][0] > 9:  # will flashed
        nbr_flash += 1

        matrix[i][j][1] = 1
        matrix[i][j][0] = 0

        adjacent_indices = get_8_adjacent(i, j, m, n)  # get adjacent flag where the flash will propagate
        for ii, jj in adjacent_indices:
            flash_recur(ii, jj, matrix)
    else:
        return nbr_flash

    # if matrix[i][j][0] > 9 and matrix[i][j][1] == 0:
    #     matrix[i][j][0] += 1  # add 1 level of energy
    #
    #     nbr_flash += 1  # a flash occurs !
    #     matrix[i][j][1] = 1  # set the octopus as flashed
    #     matrix[i][j][0] = 0
    #
    #     adjacent_indices = get_8_adjacent(i, j, m, n)  # get adjacent flag where the flash will propagate
    #
    #     # flash adjacent octopus
    #     for ii, jj in adjacent_indices:
    #         nbr_flash += flash(ii, jj, matrix)
    #         matrix[i][j][0] = 0

    return nbr_flash


def print_matrix(matrix):
    m, n = matrix.shape[0:2]
    for i in range(m):
        for j in range(n):
            if matrix[i][j][1] == 1:
                print(str(matrix[i][j][0]) + "<", end="")
            else:
                print(str(matrix[i][j][0]) + " ", end="")
        print()


def part_one(matrix, steps=100, draw=False):
    nbr_flashes = 0

    for step in range(steps):
        matrix[:, :, 0] += 1
        nbr_flashes += flashV2(matrix)

        if draw:
            print(step + 1, "\n")
            print_matrix(matrix)
        matrix[:, :, 1] = 0  # reset flag "is flashed"
    print(nbr_flashes)


def part_two(matrix):
    first_time_synchronized = None
    step = 1
    while not first_time_synchronized:
        matrix[:, :, 0] += 1
        flashV2(matrix)
        if matrix[np.where(matrix[:, :, 0] == 0)].sum() == matrix.shape[0] * matrix.shape[
            1] and not first_time_synchronized:
            first_time_synchronized = step

        step += 1
        matrix[:, :, 1] = 0  # reset flag "is flashed"
    print(first_time_synchronized)


if __name__ == "__main__":
    t0 = time.time()
    part_one(read_input())
    t1 = time.time()
    part_two(read_input())
    t2 = time.time()
    print("total {total}ms".format(total=t2 - t1))

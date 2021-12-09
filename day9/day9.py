import time
from typing import List, Tuple

import numpy as np


def read_input():
    # read the matrix and add a boolean to each cell to model if a cell was visited
    return np.array([[[y, False] for y in x] for x in np.genfromtxt('data/day9.txt', delimiter=1, dtype=int)])


# find basin recursively with a point
def find_basin(matrix, point):
    i, j = point
    m, n = matrix.shape[0:2]

    basin = list()

    adjacent_indices = get_adjacent_indices(i, j, m, n)
    valid_adjacent_indices = [ai for ai in adjacent_indices if
                              matrix[ai[0], ai[1]][0] != 9 and matrix[ai[0], ai[1]][1] != 1]

    matrix[i, j][1] = 1  # set visited after adjacent does not matter because point can not be adjacent of itself

    for ii, jj in valid_adjacent_indices:
        if matrix[ii][jj][1] != 1:  # recheck if visited because state can be changed after recursion
            basin.append((ii, jj))
            basin.extend(find_basin(matrix, (ii, jj)))

    return basin


def part_two(matrix, low_points: List[Tuple[int, int]], draw=False):
    basins: List[List[Tuple[int, int]]] = list()
    for lp in low_points:
        basin = find_basin(matrix, lp)
        basin.append(lp)  # add low point
        basins.append(basin)

    basins.sort(key=len, reverse=True)
    print(len(basins[0]) * len(basins[1]) * len(basins[2]))


def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i - 1, j))
    if i + 1 < m:
        adjacent_indices.append((i + 1, j))
    if j > 0:
        adjacent_indices.append((i, j - 1))
    if j + 1 < n:
        adjacent_indices.append((i, j + 1))
    return adjacent_indices


def part_one(matrix, draw=False):
    m, n = matrix.shape[0:2]
    low_points = list()
    for i in range(m):
        for j in range(n):
            if draw:
                print(matrix[i][j][0], end="")
            adjacent_indices = get_adjacent_indices(i, j, m, n)
            is_low_point = True
            for ii, jj in adjacent_indices:
                if matrix[i][j][0] >= matrix[ii][jj][0]:
                    is_low_point = False
                    break

            if is_low_point:
                if draw:
                    print("<", end="")
                low_points.append((i, j))  # 0 for non visited
            else:
                if draw:
                    print(" ", end="")
        if draw:
            print()

    print(sum([matrix[x[0], x[1]][0] + 1 for x in low_points]))
    return low_points


if __name__ == "__main__":
    t0 = time.time()
    low_points = part_one(read_input(), draw=False)
    t1 = time.time()
    part_two(read_input(), low_points, draw=False)
    t2 = time.time()
    print("total {total}ms".format(total=t2 - t1))

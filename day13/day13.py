import time

import numpy as np


def read_input():
    positions = set()
    folds = list()
    fold_instruction = False
    # with open("day13/test.txt", "r") as file:
    with open("data/day13.txt", "r") as file:
        for l in file:
            if l == "\n":
                fold_instruction = True
                continue

            if fold_instruction:
                folds.append((l.split("=")[0].strip().split(" ")[-1], int(l.split("=")[1].strip())))
            else:
                positions.add((int(l.split(",")[0].strip()), int(l.split(",")[1].strip())))

    return positions, folds


def print_matrix(positions, width, height):
    if not width:
        width = max([p[0] for p in positions])

    if not height:
        height = max([p[1] for p in positions])

    matrix = np.zeros((width, height), dtype=str)

    matrix[:] = "."
    for p in positions:
        matrix[p[0]][p[1]] = "#"

    for j in range(height):
        for i in range(width):
            print(matrix[i][j], end="")
        print()


def part_one_two(input):
    positions, folds = input
    max_x = max([p[0] for p in positions]) + 1
    max_y = max([p[1] for p in positions]) + 1
    nbr_first_fold = None
    for fold in folds:
        new_positions = set()
        if fold[0] == "x":
            for pos in positions:
                if pos[0] > fold[1]:
                    # new_x = max_x - pos[0] - 1
                    new_x = fold[1] - (pos[0] - fold[1])
                    new_positions.add((new_x, pos[1]))
                else:
                    new_positions.add((pos[0], pos[1]))
            max_x = int(max_x / 2) if (max_x % 2) == 1 else int(max_x / 2) + 1

        else:
            for pos in positions:
                if pos[1] > fold[1]:
                    # new_y = max_y - pos[1] - 1
                    new_y = fold[1] - (pos[1] - fold[1])
                    new_positions.add((pos[0], new_y))
                else:
                    new_positions.add((pos[0], pos[1]))

            max_y = int(max_y / 2) if (max_y % 2) == 1 else int(max_y / 2) + 1

        positions = new_positions.copy()
        if not nbr_first_fold:
            nbr_first_fold = len(positions)

    print(nbr_first_fold)
    print_matrix(positions, max_x, max_y)


if __name__ == "__main__":
    t0 = time.time()
    part_one_two(read_input())
    t2 = time.time()
    print("total {total}ms".format(total=t2 - t0))

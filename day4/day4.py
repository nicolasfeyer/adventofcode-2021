import numpy as np


def read_input():
    file = open("input.txt", "r")
    numbers = [int(x) for x in next(file).split(",")]

    counter = 0
    bingo_grids = list()
    grid = list()
    for l in file:
        if l != "\n":
            grid.append([int(x) for x in l.strip().split()])
            counter += 1

        if counter == 5:
            counter = 0
            bingo_grids.append(grid)
            grid = list()

    return np.array(bingo_grids), np.array(numbers)


def find_winner(bingo_grids, last):
    grid_no = 0
    for grid in bingo_grids:
        if np.all((grid < 0), axis=1).sum() > 0 or np.all((grid < 0), axis=0).sum() > 0:
            unmarked_sum = grid[grid > 0].sum()
            if not last:
                return unmarked_sum
            else:
                grid_temp = np.copy(grid)
                bingo_grids[grid_no] = 0  # when grid finished, replace all by 0
                if len(bingo_grids[bingo_grids.sum() == 0]):  # if all grid are finished
                    return grid_temp[grid_temp > 0].sum()

        grid_no += 1


def update_grid(bingo_grids, number):
    bingo_grids[bingo_grids == number] = -number
    return bingo_grids


def part_one(bingo_grids, numbers, last=False):
    for number in numbers:
        bingo_grids = update_grid(bingo_grids, number)
        unmarked_sum = find_winner(bingo_grids, last=last)

        if unmarked_sum:
            return unmarked_sum * number


if __name__ == "__main__":
    bingo_grids_, numbers_ = read_input()
    print(part_one(bingo_grids_, numbers_))
    print(part_one(bingo_grids_, numbers_, last=True))

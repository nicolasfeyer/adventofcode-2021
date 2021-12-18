import sys
import time
import heapq
import numpy as np


def read_input():
    return np.array([[y for y in x] for x in np.genfromtxt('data/day15.txt', delimiter=1, dtype=int)])
    # return np.array([[y for y in x] for x in np.genfromtxt('day15/test.txt', delimiter=1, dtype=int)])


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


def find_min_cost(matrix):
    todo = [(0, (0, 0))]  # list to store the next node
    visited = {(0, 0)}  # remember visited node
    m, n = matrix.shape

    # while the todo queue is not empty
    while todo:
        # pick a point
        cost, (i, j) = heapq.heappop(todo)
        if i == m - 1 and j == n - 1:  # target reached so we can return the cost
            return cost
        # for each neighbors
        for ii, jj in get_adjacent_indices(i, j, m, n):
            # check if visited
            if (ii, jj) not in visited:
                # add to the todo queue
                heapq.heappush(todo, (cost + matrix[ii][jj], (ii, jj)))
                visited.add((ii, jj))


def part_one(matrix):
    print(find_min_cost(matrix))


def enlarge(matrix):
    # generate all horizontal sub matrices
    multiple_horizontal = [matrix + i for i in range(5)]

    # concatenate horizontal matrices
    full_horizontal = multiple_horizontal[0]
    for i in range(1, len(multiple_horizontal)):
        full_horizontal = np.concatenate((full_horizontal, multiple_horizontal[i]), axis=1)

    # generate all vertical sub matrices
    multiple_vertical = [full_horizontal + i for i in range(5)]

    # concatenate vertical matrices
    enlarged_matrix = multiple_vertical[0]
    for i in range(1, len(multiple_vertical)):
        enlarged_matrix = np.concatenate((enlarged_matrix, multiple_vertical[i]), axis=0)

    # modulo 9 to deal with the cel above 9
    enlarged_matrix[np.where(enlarged_matrix > 9)] -= 9

    return enlarged_matrix


def print_numpy_matrix(matrix):
    for j in range(matrix.shape[1]):
        for i in range(matrix.shape[0]):
            print(matrix[i][j], end="")
        print()


def part_two(matrix):
    enlarged = enlarge(matrix)
    print(find_min_cost(enlarged))


if __name__ == "__main__":
    t0 = time.time()
    part_one(read_input())
    t1 = time.time()
    part_two(read_input())
    t2 = time.time()
    print("total {total}ms".format(total=t2 - t1))

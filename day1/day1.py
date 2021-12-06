from itertools import islice


def read_input():
    return [int(l.strip()) for l in open('input.txt', 'r').readlines()]


def part_one(depths_):
    nbr = 0
    for i_d in range(1, len(depths_)):
        if depths_[i_d] > depths_[i_d - 1]:
            nbr = nbr + 1

    print(nbr)


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def part_two(depths_):
    nbr = 0
    windows = list(window(depths_, n=3))
    for i_w in range(1, len(windows)):
        if sum(windows[i_w]) > sum(windows[i_w - 1]):
            nbr = nbr + 1
    print(nbr)


if __name__ == "__main__":
    depths = read_input()
    part_one(depths)
    part_two(depths)

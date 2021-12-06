from typing import Tuple, Set


def get_pts_of_line(line: Tuple[Tuple[int]], diagonal=False) -> Set:
    (x1, y1), (x2, y2) = line
    if x1 == x2:  # (3,0),(3,1) ->
        return set([(x1, i) for i in range(min(y1, y2), max(y1, y2) + 1)])
    elif y1 == y2:
        return set([(i, y1) for i in range(min(x1, x2), max(x1, x2) + 1)])
    else:  # ignore diagonal
        if not diagonal:
            return set()
        else:
            fx1 = x1
            fx2 = x2 + (1 if x1 < x2 else -1)
            fy1 = y1
            fy2 = y2 + (1 if y1 < y2 else -1)
            return set(
                [(i, j) for i, j in
                 zip(range(fx1, fx2, -1 if fx1 > fx2 else 1), range(fy1, fy2, -1 if fy1 > fy2 else 1))])


def points_of_intersection(line1, line2, diagonal=False) -> Set:
    return get_pts_of_line(line1, diagonal).intersection(get_pts_of_line(line2, diagonal))


def number_of_dangerous_areas(lines_, diagonal=False):
    points_occurence = dict()
    for l1 in lines_:
        pts = get_pts_of_line(l1, diagonal=diagonal)
        for p in pts:
            if p not in points_occurence:
                points_occurence[p] = 1
            else:
                points_occurence[p] += 1

    print(len({k: v for k, v in points_occurence.items() if v > 1}))


if __name__ == "__main__":
    lines = [((int(l.strip().split(" -> ")[0].split(",")[0]), int(l.strip().split(" -> ")[0].split(",")[1])),
              (int(l.strip().split(" -> ")[1].split(",")[0]), int(l.strip().split(" -> ")[1].split(",")[1]))) for l in
             open('input.txt', 'r').readlines()]

    number_of_dangerous_areas(lines, diagonal=False)
    number_of_dangerous_areas(lines, diagonal=True)

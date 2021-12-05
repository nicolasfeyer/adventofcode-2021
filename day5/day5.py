lines_raw = open('input.txt', 'r').readlines()

lines = list()

for l in lines_raw:
    l = l.strip()
    x1_y1 = l.split(" -> ")[0]
    x2_y2 = l.split(" -> ")[1]
    lines.append(
        ((int(x1_y1.split(",")[0]), int(x1_y1.split(",")[1])), (int(x2_y2.split(",")[0]), int(x2_y2.split(",")[1]))))


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


intersections_unique = set()
for l1 in lines:
    for l2 in lines:
        if l1 != l2:
            pts = line_intersection(l1, l2)
            if pts:
                intersections_unique.add(pts)

print(len(intersections_unique))

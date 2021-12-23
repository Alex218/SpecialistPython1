def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def inside(c1, c2, r1, r2):
    btw_centers = distance(*c1, *c2)
    return c1 == c2 or btw_centers <= abs(r1 - r2)


print(inside((0, 1), (-2, 1), 4, 2))

# c1 = 0, 1
# c2 = -2, 1
# r1 = 4
# r2 = 2
# print(inside(c1, c2, r1, r2))

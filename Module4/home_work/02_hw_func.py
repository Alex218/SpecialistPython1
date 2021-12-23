def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def shortest_segments(a, b, c):
    segments = {"AB": distance(*a, *b), "BC": distance(*b, *c), "AC": distance(*a, *c)}
    min_length = segments["AB"]
    for key in segments:
        if segments[key] <= min_length:
            shortest = key
            min_length = segments[key]
    return shortest


a = 3, 2
b = 1, -3
c = 4, 10

print("Самый короткий отрезок:", shortest_segments(a, b, c))

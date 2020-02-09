coords1 = eval(input(''))
print(coords1)


def is_equilateral(x1, y1, x2, y2, x3, y3):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) == ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2) == ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1 / 2)

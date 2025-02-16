import math


def main(x):
    if x < 81:
        return ((69 * pow(math.atan(x), 5)) - pow(math.tan(x), 3)
                - 82 * (73 * x - (48 * pow(x, 2)) - 1))
    elif 81 <= x < 132:
        return (pow(x, 4)) - (pow((23 * x), 5) / 91)
    else:
        return (34 * (89 - (67 * pow(x, 2)))) - (33 * pow(34 * pow(x, 3), 6))

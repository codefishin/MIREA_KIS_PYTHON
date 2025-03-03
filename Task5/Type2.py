import math


def main(x: list):
    return sum(10 * math.tan(pow(x[i], 2) + x[i // 2])
               for i in range(len(x)))

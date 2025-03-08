from math import prod


def main(n, a, m, y):
    s1 = sum(prod(60 * pow(33 * pow(k, 3), 7) - pow(c, 3)
                  for c in range(1, n + 1))
             for k in range(1, a + 1))

    s2 = sum(sum(sum(pow(29 * (1 - y - 86 * pow(j, 3)), 2)
                     + pow(c, 6) + pow(69 * k, 3)
             for c in range(1, n + 1))
             for k in range(1, a + 1))
             for j in range(1, m + 1))

    return s1 + s2

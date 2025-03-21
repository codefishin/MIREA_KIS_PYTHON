def inv_sqrt(number: float) -> float:
    x2 = number * 0.5
    y = number
    i = int(y)
    i = 0x5f3759df - (i >> 1)
    y = float(i)
    y = y * (1.5 - (x2 * y * y))
    return y
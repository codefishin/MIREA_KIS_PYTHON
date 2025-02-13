def main(x: float) -> float:
    numerator = ((29 * x ** 3 + 13 + x) ** 4) + (70 * x) / 45
    denominator = x ** 7
    term1 = numerator / denominator
    term2 = (51 * x ** 2 + 1 + 88 * x) ** 3
    return term1 + term2

def main(n: int) -> float:
    if n == 0:
        return 0.62
    elif n >= 1:
        return 1 - (((pow(main(n - 1), 2)) / 64) + 0.03 + main(n - 1))
    else:
        return 0

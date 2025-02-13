def main(x):
    try:
        return (((pow((29 * pow(x, 3)) + 13 + x, 4) + ((70 * x) / 45))
                 / pow(x, 7)) + pow((51 * pow(x, 2)) + 1 + (88 * x), 3))
    except ArithmeticError:
        return 0

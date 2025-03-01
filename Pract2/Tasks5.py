def ham_dist(num1: int, num2: int) -> str:
    return str(len(str(bin(num1 ^ num2))) - 2)


def main():
    print(ham_dist(0b00, 0b11))


if __name__ == "__main__":
    main()

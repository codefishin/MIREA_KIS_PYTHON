import random
import itertools


int_s = [2, 1, 1, 6, 14, 28, 40]
base10 = ['0', '1', '2',
          '3', '4', '5',
          '6', '7', '8', '9']
str_s = ['a', 'b', 'aaabbb', 'acd']
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-1234567890'


def Task1():
    return list(map(int, base10))
    # map делает так что функция int вызывается
    # для каждого элемента base10


def Task2():
    return len(int_s)


def Task3():
    return base10[::-1]  # в школе такой прикол был


def Task4(x: int):
    return [i for i, v in enumerate(int_s) if v == x]


def Task5():
    return sum(int_s[i] for i in range(0, len(int_s), 2))


def Task6():
    return max(str_s, key=len)


def Task7():
    return [n for n in int_s if n % sum(int(d) for d in str(n)) == 0]


def Task8(size: int):
    return ''.join(random.choices(alphabet, k=size))


def Task9(var='ABC'):
    return [(i, len(list(y))) for i, y in itertools.groupby(var)]
    # https://docs.python.org/3/library/itertools.html


def main():
    while 1:
        print('\n', '-' * 50, '\n')
        print("0. Завершить программу")
        print("1. LIST 's' to INT")
        print("2. Count unique 's' elements")
        print("3. reverse 's'")
        print("4. find x in 's'")
        print("5. sum even 's' elements")
        print("6. max string length in 's'")
        print("7. harsh-ad in 's' (dividable by sum of digits)")
        print("8. generate random text with set length")
        print("9. RLE-encode")
        user_input = int(input("Введите любое число из списка.\n"))
        print('\n', '-' * 50, '\n')
        match user_input:
            case 0:
                break
            case 1:
                print(Task1())
            case 2:
                print(Task2())
            case 3:
                print(Task3())
            case 4:
                print(Task4(1))
            case 5:
                print(Task5())
            case 6:
                print(Task6())
            case 7:
                print(Task7())
            case 8:
                print(Task8(20))
            case 9:
                print(Task9("ABCDCCEF2"))


if __name__ == "__main__":
    main()

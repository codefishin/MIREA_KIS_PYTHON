import random
import itertools


int_s = [2, 1, 1, 6, 14, 28, 40]
base10 = ['0', '1', '2',
          '3', '4', '5',
          '6', '7', '8', '9']
str_s = ['a', 'b', 'aaabbb', 'acd']
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-1234567890'


def funkyLine():
    """
    Рисует смешную строчку.
    Написано не однострочно.
    :return:
    """
    result = ''
    for i in range(0, 51):
        if i % 2 == 0:
            result += '-'
        else:
            result += '+'
    return result


def Task1():
    """
    Возвращает строковый список в виде числового.
    Работает со списками, где каждый элемент входит в систему счисления 10

    map делает так что функция int вызывается для каждого элемента base10
    :return:
    """
    return list(map(int, base10))


def Task2():
    """
    Возвращает длину списка.
    :return:
    """
    return len(int_s)


def Task3():
    """
    Возвращает обратный список.
    :return:
    """
    return base10[::-1]


def Task4(x: int):
    """
    Пробегает весь список и проверяет,
    равен ли текущий символ списка приведённому параметру.
    Enumerate возвращает значения списка в виде чисел и содержимого:
    ([0, "STUFF HERE"], [1, "MORE STUFF], ...)
    :param x:
    :return:
    """
    return [i for i, v in enumerate(int_s) if v == x]


def Task5():
    """
    Возвращает сумму всех чётных значений списка
    :return:
    """
    return sum(int_s[i] for i in range(0, len(int_s), 2))


def Task6():
    """
    Возвращает самый длинный элемент списка.
    Перепись параметра key нужна для того, чтобы max определял по длине.
    :return:
    """
    return max(str_s, key=len)


def Task7():
    """
    Эмм...
    Возвращает харшад.
    n - текущий элемент, хранится как строка
    d - один символ в строке n
    :return:
    """
    return [n for n in int_s if n % sum(int(d) for d in str(n)) == 0]


def Task8(size: int):
    """
    Генерирует случайную строку.
    :param size:
    :return:
    """
    return ''.join(random.choices(alphabet, k=size))


def Task9(var='ABC'):
    """
    https://docs.python.org/3/library/itertools.html
    Генерирует список, который зашифрован при помощи RLE.
    :param var:
    :return:
    """
    return [(i, len(list(y))) for i, y in itertools.groupby(var)]


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
        print(funkyLine())
        match user_input:
            case 0:
                break
            case 1:
                print(Task1())
                print(funkyLine())
                help(Task1)
            case 2:
                print(Task2())
                print(funkyLine())
                help(Task2)
            case 3:
                print(Task3())
                print(funkyLine())
                help(Task3)
            case 4:
                print(Task4(1))
                print(funkyLine())
                help(Task4)
            case 5:
                print(Task5())
                print(funkyLine())
                help(Task5)
            case 6:
                print(Task6())
                print(funkyLine())
                help(Task6)
            case 7:
                print(Task7())
                print(funkyLine())
                help(Task7)
            case 8:
                print(Task8(20))
                print(funkyLine())
                help(Task8)
            case 9:
                print(Task9("ABCDCCEF2"))
                print(funkyLine())
                help(Task9)


if __name__ == "__main__":
    main()

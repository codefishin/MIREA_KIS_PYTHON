import sys
import math
import tkinter as tk
sys.setrecursionlimit(5000)

def f1_1() -> None:
    var1 = 42
    var2 = '42'
    var3 = 0b101010
    var4 = 0x2A
    var5 = 0o52
    var6 = 42.0
    var7 = 4.2e1
    var8 = {42, 42}
    var9 = [42][0]
    var10 = (42, 42)[0]
    print(var1 == 42, int(var2) == 42, var3 == 42, var4 == 42, var5 == 42,
          var6 == 42, var7 == 42, var8.pop() == 42, var9 == 42, var10 == 42)


def f1_2() -> None:
    print("Для целочисленных чисел лимитом является 4300 символов, но это можно растянуть при помощи следующей строки:\n")
    print("sys.set_int_max_str_digits(DIGIT_HERE)")
    print("Для вещественных чисел лимитом является стандарт IEEE 754:")
    print(sys.float_info.max)


def f1_3() -> list:
    list1 = [42, 4, 2]
    list2 = ['fourty-two', 'four', 'two']
    zipped = zip(list1, list2) # даёт кортеж из двух значений
    return list(zipped) # соединяет в список


def f1_4() -> None:
    # a = 10
    #     while a != 0:
    #         a -= 0.1
    #         print(a)
    # не рабочий код
    a = 10
    while a >= 0:
        a -= 0.1
        print(a)
    print("Стандарт IEEE 754 не позволяет точному вычитанию вещественных чисел, из-за этого остаётся какой-либо остаток\nЧтобы избавится от данной проблемы, нужно использовать привидение числа, либо другие операторы, кроме == или !=.")


def f1_5() -> None:
    z = 1
    print("Начало программы: " + str(z))

    z <<= 40 # число становится 2 в степени 40 (сдвиг бита 1 на 40 мест влево)
    print("После 'z <<= 40': " + str(z))

    # 2 ** z # возводим 2 в очень большое число, программа будет это обрабатывать несколько тысячилетий (ну или крашнется)
    print("Для безопасности программы мы не будет возводить 2 в степень z, но вкратце такую цифру программа обрабатывает слишком долго.")


def f1_6() -> None:
    i = 0
    while i < 10:
        print(i)
        #++i # это не работает, оно не увеличивает i на 1
        i += 1 # это возводит на 1
    print("См. комментарии кода")


def f1_7() -> None:
    var = (True * 2 + False) * -True
    # Пояснение происходящего:
    # (1 * 2 + 0) * -1 == -2
    print(str(var) + "\nСм. комментарии кода")


def f1_8() -> None:
    x = 5
    var_true = 1 < x < 10 # Проверка на то, чтобы x был больше 1 и меньше 10
    print(var_true)
    var_false = 1 < (x < 10) # сначала проверит x < 10 (Возвращает True)
    # ^^ Потом проверит 1 < True (или же 1 < 1, что возвращает False)
    print(var_false)
    print("См. комментарии кода")

def f2() -> None:
    print("\nSyntaxError: invalid syntax: return x y (не хватает запятой)\n")
    print("\nSyntaxError: cannot assign to literal: 1 = 'FISHING')\n")
    print("\nNameError: name ... is not defined:\n    a\n    print(b)\n(нету переменной b)")
    print("\nSyntaxError: unterminated string literal:\n    a = 'I love errors\n    b = 'nooooo'\n(не закрыты ковычки)\n")
    print("\nTypeError: unsupported operand type(s) for ...:\n    a = 1\n    print('hello' + a)\n(Нельзя выводить 2 разные переменные)\n")
    print("\nIndentationError: expected an indented block: является ошибкой табуляции\n")
    print("\nIndentationError: unindent does not match any outer indentation level: тоже ошибка табуляции, когда юзер вставляет и пробелы и табуляцию\n")
    print("\nValueError: math domain error:\nsqrt(-1) # ну как бы с -1 корня не бывает\n")
    print("\nOverflowError: math range error\nПример ошибки: 1-math.exp(-4*1000000*-0.0641515994108)\nФикс:\ntry:\n    ans = math.exp(200000)\nexcept OverflowError:\n    ans = float('inf')")


def f3_1(x: float) -> float:
    x1 = x + x
    x2 = x1 + x1
    return x2 + x2 + x2


def f3_2(x: float) -> float:
    x1 = x + x
    x2 = x1 + x1
    x3 = x2 + x2
    return x3 + x3


def f3_3(x: float) -> float:
    x1 = x + x
    x2 = x1 + x1
    x3 = x2 + x2
    x4 = x3 - (x - x3)
    return x4


def f3_4(x: int, y: int) -> int:
    r = x
    for i in range(0, y - 1):
        x = x + r
    return x


def f3_5(x: int, y: int) -> int: #fast_mul
    result = x
    while y > 0:
        if y & 1: # Если число нечётное
            result <<= y

        x <<= 1 # Умножить x на 1
        y >>= 1 # Делить y на 1

    return result


def f3_6(x: int, y: int) -> int: #fast_pow
    result = 1
    while y > 0:
        if y & 1: # Если число нечётное
            result *= x

        x *= x
        y >>= 1 # Делить y на 1

    return result


def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def f3_7(x, y):
    x0 = x & 0xFF # младшие 8 бит
    x1 = (x >> 8) & 0xFF # старшие

    y0 = y & 0xFF  # младшие 8 бит
    y1 = (y >> 8) & 0xFF  # старшие

    # разделение чисел на половинки окончен

    z0 = mul_bits(x0, y0, 8) # первая половина
    z1 = mul_bits(x1, y1, 8) # вторая
    z2 = mul_bits(x1, y0, 8) + mul_bits(x0, y1, 8) # погрешность / та штука когда столбиком решаешь я не помню

    result = (z1 << 16) + (z2 << 8) + z0 # составление результата
    #print(z1 << 16)
    #print(z2 << 8)
    #print(z0)
    return result


def f3_8():
    # TODO
    return 0


def f3_9():
    # TODO
    return 0


def f3_10():
    # TODO
    return 0



def main():
    f1_1()


if __name__ == '__main__':
    main()

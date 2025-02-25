def Task1():
    """
    Строка кода:\n\n[0xfor _ in 'abc']

    Сама собой ничего не представляет, так как не запускается.
    Модификация этой строки: [0 for _ in 'abc'] уже запускается.
    Она создаёт список данных и работает следующим образом...
    Сначала код берёт длину строки 'abc' (возвращает 3)
    После заполняет массив каким-то числом/символом, в нашем случае 0
    _ это переменная для цикла, обычно так называют,
    когда итерация цикла не важна (т.е. Позиция)

    ...и да, это Python.
    :returns None:
    """
    var = [0 for _ in 'abc']  # не запускается при 0xfor _ in 'abc'
    print(var)


def Task2(*, var='str'):
    """
    Пример работы именованных параметров.
    В функции реализовано присоединение 'ing' к параметру var
    :param var:
    :returns None:
    """
    var.join('ing')


def Task3():
    """
    Я не могу сделать реплику ошибки.

    Возможно, тут ошибка в постановке.
    Если сюда поставить c = 300000.0, то ошибка из постановки сразу появится.
    Так происходит, потому что c здесь - FLOAT, но d - INT.
    :returns None:
    """
    a = 1
    b = 1
    c_int = 300000  # проверено в Python 3.11
    c = 300000.0
    d = 300000
    print(a is b, c is d)


def Task4():
    """
    Сократить до 19 символов: ['much','code','wow'][i] (24 символа)

    Непонятная ерунда в коде строки это слова
    much, code, wow сложенные следующим образом:
    Первый символ каждого слова - MCW
    Второй символ каждого слова - UOO
    Третий - CDW
    Четвёртый - HE (у wow нет символа)
    :returns None:
    """
    i = 2
    print('mcwuoocdwhe'[i::3])


def Task5():
    """
    В функции указано, почему список работает необычно.
    :returns None:
    """
    lst = ['a', 'b', 'c']
    lst += 'd'
    print(lst)
    print('-' * 50)
    print("    lst = lst + 'd'  # Ошибка?!\n"
          "    print(lst)")
    print("\n-- Это не работает, так как оператор + "
          "здесь работает следующим образом:")
    print("'Взять lst (тип LIST) и добавить к нему "
          "'d' (тип STRING)'")
    print("Нельзя напрямую сложить STRING и LIST,"
          "это две разные переменные")
    print("Оператор += работает примерно как append,"
          "т.е. оно не 'складывает', а вносит данные в LIST,"
          "но делает это при помощи итерации.\n\n")

    print("    lst += 42")
    print("    print(lst)  # Ошибка?!")
    print("\n-- Это не работает из-за того, что 42 - INT,"
          "и такое не итерируется")
    print("\n\nGOOD TO KNOW: в списках += вызывает "
          "'__iadd__', а + вызывает '__add__'")


def main():
    while 1:
        print('\n', '-' * 50, '\n')
        print("0. Завершить программу")
        print("1. [0xfor _ in 'abc'")
        print("2. Именованные аргументы")
        print("3. Несравнимые переменные")
        print("4. Сокращение кода")
        print("5. Странные ошибки")
        print("6. Помощь с 1 функцией")
        print("7. Помощь с 2 функцией")
        print("8. Помощь с 3 функцией")
        print("9. Помощь с 4 функцией")
        print("10. Помощь с 5 функцией")
        user_input = int(input("Введите любое число из списка.\n"))
        print('\n', '-' * 50, '\n')
        match user_input:
            case 0:
                break
            case 1:
                Task1()
            case 2:
                # Task2("a") # Вызывает ошибку, TypeError
                Task2(var="str_")
            case 3:
                Task3()
            case 4:
                Task4()
            case 5:
                Task5()
            case 6:
                help(Task1)
            case 7:
                help(Task2)
            case 8:
                help(Task3)
            case 9:
                help(Task4)
            case 10:
                help(Task5)


if __name__ == "__main__":
    main()

import sys
from datetime import datetime

group_name = ['ИВБО', 'ИКБО', 'ИМБО', 'ИНБО']
current_year = datetime.now().year


coded_message = [0xE3238557, 0x6204A1F8, 0xE6537611, 0x174E5747,
                 0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,
                 0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,
                 0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,
                 0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,
                 0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,
                 0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,
                 0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,
                 0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,
                 0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637]

decoded_message = []


def generate_groups():
    """
    Возвращает список групп от 1 до 11, в порядке как на https://kispython.ru
    DEV_NOTE: Я хотел сделать через read_html / прочтение скаченного html.
    ...но не получилось.
    :return:
    """
    result = []
    for group_tag in group_name:
        for i in range(1, 11):
            tmp = group_tag + '-'
            if i < 10:
                tmp = tmp + '0' + str(i)
            else:
                tmp += str(i)
            tmp = tmp + '-' + str(current_year)[-2:]
            result.append(tmp)
    return result


def myPrint(*var, sep=' ', end='\n', file=sys.stdout, flush=False):
    """
    Реализация print() своим способом.
    Использует параметры, как во встроенном print()
    Выводит текст.
    :param var:
    :param sep:
    :param end:
    :param file:
    :param flush:
    :return:
    """
    if file is None:
        file = sys.stdout  # чтобы не прикалывались
    tmp = list(map(str, var))
    msg = ''
    for char in tmp:
        msg = msg + char + sep
    msg += end
    file.write(msg)
    # Почитал что есть flush у print. Что он делает без понятия
    if flush is True:
        file.flush()


def decrypt(v, *, k=None):
    """
    Дешифрует первые 2 символа сообщения по ключу.
    :param v:
    :param k:
    :return:
    """
    if k is None:
        k = [0, 4, 5, 1]
    summ = 0xC6EF3720
    delta = 0x9E3779B9
    mask = 0xFFFFFFFF
    result = []
    v0 = v[0]
    v1 = v[1]
    for i in range(32):
        v1 = (v1 - (((v0 << 4) + k[2]) ^ (v0 + summ)
                    ^ ((v0 >> 5) + k[3]))) & mask
        v0 = (v0 - (((v1 << 4) + k[0]) ^ (v1 + summ)
                    ^ ((v1 >> 5) + k[1]))) & mask
        summ = (summ - delta) & mask
    decoded_message.append(v0)
    decoded_message.append(v1)
    coded_message.pop(0)
    coded_message.pop(0)

    return result


def main():
    while 1:
        print('\n', '-' * 50, '\n')
        print("0. Завершить программу")
        print("1. generate_groups")
        print("2. rewritten print")
        print("3. decrypted message")
        user_input = int(input("Введите любое число из списка.\n"))
        match user_input:
            case 0:
                break
            case 1:
                print('=' * 50)
                print(generate_groups())
                print('=' * 50)
                help(generate_groups)
            case 2:
                print('=' * 50)
                myPrint(123)
                myPrint("a", end='b')
                myPrint("f", sep='---')
                myPrint('=' * 50)
                help(myPrint)
            case 3:  # пришлось так
                print('=' * 50)
                length_of_msg = len(coded_message) // 2
                for _ in range(0, length_of_msg):
                    decrypt(coded_message)  # я хотел нормально, но я ИДИОТ
                msg = ''.join(list(map(chr, decoded_message)))
                print(msg)
                print('=' * 50)
                help(decrypt)


if __name__ == "__main__":
    main()

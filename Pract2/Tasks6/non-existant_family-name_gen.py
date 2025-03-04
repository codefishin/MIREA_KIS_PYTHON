import random


def read_data(file_name=''):
    if file_name == '':
        return None
    f = open(file_name, "r+", encoding="utf8")
    return f.read().splitlines()


def generate_family_name():
    p1 = ['Шо', 'Фе', 'Та', 'Му', 'Че', 'Ти', 'Гу', 'На']
    p2 = ['мид', 'нар', 'бян', 'бин', 'рев', 'зян', 'год', 'цач']
    p3 = ['ий', 'о', 'ич', 'як', '']
    result = p1[random.randint(0, len(p1) - 1)]
    result += p2[random.randint(0, len(p2) - 1)]
    result += p3[random.randint(0, len(p3) - 1)]
    return result


def generate_full_name():
    family_name = generate_family_name()
    names = read_data('names.txt')
    surname = names[random.randint(0, len(names) - 1)][0]
    surname += '.'
    return names[random.randint(0, len(names) - 1)] + ' ' + surname + ' ' + family_name


def main():
    print(generate_full_name())


if __name__ == '__main__':
    main()

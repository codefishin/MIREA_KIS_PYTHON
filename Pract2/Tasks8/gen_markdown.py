import sys


def convert_quotes(markdown_text):
    parts = markdown_text

    m = 0
    buf = ''
    res = ''
    change = ['«', '»']  # должно быть из 2 символов.
    if len(change) != 2:
        raise Exception("Check change length on line 10")

    for _ in parts:
        for i in _:  # XDXDXDXD зато своё
            if i == '`':
                buf += i
                res += i
                continue
            if buf == '```':
                res += i
                continue
            if buf == '```' and i == '`':
                buf += '\b'
                res += i
                continue
            if i == '"' and m == 0:
                m += 1
                res += change[0]
                continue
            elif i == '"':
                m = 0
                res += change[1]
                continue
            res += i

    return ''.join(res)


def main():
    # Все print переписаны на то, чтобы заполнять файл
    # Стандартный ввод: python gen_markdown.py FILE1.md
    # Ввод в файл: python gen_markdown.py FILE1.md > FILE2.md
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r', encoding='ISO-8859-1') as file:
            markdown_text = file.read()
    else:
        markdown_text = sys.stdin.read()

    converted_text = convert_quotes(markdown_text)
    print(converted_text)


if __name__ == "__main__":
    main()

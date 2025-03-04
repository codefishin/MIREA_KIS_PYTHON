import sys


def convert_quotes(markdown_text):
    parts = markdown_text

    m = 0
    buf = ''
    res = ''
    change = ['«', '»']  # должно быть из 2 символов.
    if len(change) != 2:
        raise Exception("Check change length on line 11")

    for i in parts:
        for _ in i:  # XDXDXDXD зато своё
            if _ == '`':
                buf += _
                res += _
                continue
            if buf == '```':
                res += _
                continue
            if buf == '```' and _ == '`':
                buf += '\b'
                res += _
                continue
            if _ == '"' and m == 0:
                m += 1
                res += change[0]
                continue
            elif _ == '"':
                m = 0
                res += change[1]
                continue
            res += _

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

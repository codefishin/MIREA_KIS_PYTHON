import os
import argparse
from datetime import datetime  # не помню встройка ли это :-)


def listDirectory(path='.', all_files=False, long_format=False):
    files = os.listdir(path)
    if not all_files:  # default
        files = [f for f in files if not f.startswith('.')]

    if long_format:  # если -l
        for f in files:
            f_path = os.path.join(path, f)
            stats = os.stat(f_path)
            permissions = oct(stats.st_mode)[-3:]
            size = stats.st_size
            modified_time = (datetime.fromtimestamp(stats.st_mtime)
                             .strftime('%Y-%m-%d %H:%M'))
            print(f"{permissions} {size} {modified_time} {f}")
    else:  # -a
        print("\n".join(files))


def main():
    parser = argparse.ArgumentParser(description='List directory contents.')
    parser.add_argument('-p',
                        nargs='?',
                        default='.',
                        help='Directory path to list')  # флаг для пути
    parser.add_argument('-a',
                        action='store_true',
                        help='Include hidden files')  # вывод всего
    parser.add_argument('-l',
                        action='store_true',
                        help='Use long listing format')  # swag

    args = parser.parse_args()

    listDirectory(args.path, args.a, args.l)
    # аргумент 1 -> путь (флаг -p)
    # аргумент 2 -> выводить ли всё? (флаг -a)
    # аргумент 3 -> выводить подробную информацию? (флаг -l)


if __name__ == '__main__':
    main()

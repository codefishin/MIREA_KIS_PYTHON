import os
import argparse


def generate_graphviz(path='.', parent=None, write_to_file=False):
    graph = ""
    if parent is None:
        graph += "digraph G {\n"

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        graph += f'    "{item_path}" [label="{item}"];\n'
        if parent is not None:
            graph += f'    "{parent}" -> "{item_path}";\n'

        if os.path.isdir(item_path):
            graph += generate_graphviz(item_path, item_path)

    if parent is None:
        graph += "}\n"

    if write_to_file is True:
        f = open("graph.dot", "w")
        f.write(graph)
        f.close()
        return f"Written to graph.dot in {path}"
    return graph


def main():
    parser = argparse.ArgumentParser(
        description='List directory contents.')
    parser.add_argument('path',
                        nargs='?',
                        default='.',
                        help='Directory path to list')  # флаг для пути
    parser.add_argument('-f',
                        action='store_true',
                        help='Write to file in PATH')  # вывод в файл

    args = parser.parse_args()
    print(generate_graphviz(args.path, None, args.f))


if __name__ == "__main__":
    main()

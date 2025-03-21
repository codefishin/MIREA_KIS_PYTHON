import requests

def AttributeErrorGen() -> int:  # 1
    url = "https://google.com"
    r = requests.get(url)  # выводит ошибку
    # вывод как в примере только в некоторых версиях Python
    return r.status_code


def ModuleTheory() -> None:  # 2
    # модуль загружается один раз при первом импорте,
    # а при последующих импортах используется уже загруженная версия
    import module_theory
    module_theory.isLoaded()
    import module_theory
    module_theory.isLoaded()


def WorkingWithGLOBAL_VAR():  # 3
    from module_theory import GLOBAL_VAR
    # импорт выше нигде не используется
    # а точнее его вообще нельзя использовать
    GLOBAL_VAR = 42  # задаёт рандомную переменную
    # число отвечающее на всё. nice
    import module_theory
    module_theory.GLOBAL_VAR = 84
    print("GLOBAL_VAR (переменная):", GLOBAL_VAR,
          "\nGLOBAL_VAR из module_theory:", module_theory.getGLOBAL_VAR())

from module_theory import *
def ControlImportStar():  # 4
    isLoaded()
    # getGLOBAL_VAR()  # вызывает ошибку.
    # хоть и getGLOBAL_VAR() есть в module_theory,
    # он не будет импортироваться из-за имени __all__


def load_config(filename):  # 5
    """
    Плюсы импорта: Безопасность, лёгкая отладка
    Минусы импорта: Зависимость от структуры модуля
    Плюсы прямого кода: Удобство, гибкость
    Минусы прямого кода: Опасность, сложность
    :param filename:
    :return:
    """
    cfg = {}
    with open(filename) as f:
        exec(f.read(), {}, cfg)
    return cfg


def main():
    # AttributeErrorGen()
    # ModuleTheory()
    # WorkingWithGLOBAL_VAR()
    # ControlImportStar()
    print(load_config("filename.txt"))


if __name__ == "__main__":
    main()

print("loading module_theory")
GLOBAL_VAR = 41


__all__ = ['isLoaded']  # чтобы * позволяла вызывать только isLoaded


def isLoaded():
    print("module_theory is loaded")


def getGLOBAL_VAR():
    return GLOBAL_VAR

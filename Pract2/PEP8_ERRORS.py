def function():
    return 1


def pow_func(x, y):
    return x ** y


def E211():
    print(function ())


def E225():
    return 1> 2


def E231():
    pow_func(1,2)


def E251(key = 'ard'):
    return key

def E302():
    print("error on lines 22 to 24")


def E701():
    var = 1
    if var != 0: print("error on line 30")


def E702():
    var = 1; var = 2


def E711(var):
    if var == None:
        print("error on line 38")


def E712(var: bool):
    if var == True:
        print("error on line 43")
    print("error on line 43")

# нужно оставлять 1 пустую строку для избежания ошибки W292

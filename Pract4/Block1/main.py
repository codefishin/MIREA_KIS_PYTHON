class foo:
    def __init__(self):
        self.name = 'me'
        self.age = '20'
        self.__private_data = 'private'

    def get_private_data(self):
        return self.__private_data


def get_fields(obj):
    return [field for field in dir(obj)
            if not field.startswith('__')
            and not field.startswith('_')]


def read_fields(obj):
    return {field: getattr(obj, field) for field in dir(obj)
            if not field.startswith('__') and not field.startswith('_')}


def try_method(obj, method_name: str):
    if hasattr(obj, method_name) and callable(getattr(obj, method_name)):
        method = getattr(obj, method_name)
        print(method())
    else:
        print("ERROR: statement does not exist or is uncallable")


def main():
    # 1
    obj = foo()
    print(get_fields(obj))
    print(read_fields(obj))
    print("*" * 50)
    # 2
    try_method(obj, 'get_private_data')
    try_method(obj, 'get_data')
    # 4
    get_inheritance = lambda cls: ' -> '.join(c.__name__ for c in cls.__mro__)
    print(get_inheritance(OSError))


# 3
class A:
    pass

class B(A):
    pass

class C(B):  # было class C(A, B), A лишнее, т.к. B уже наследует
    pass


if __name__ == "__main__":
    main()

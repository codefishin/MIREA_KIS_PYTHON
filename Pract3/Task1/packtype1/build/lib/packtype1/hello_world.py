def hello_world(*, printable=True):
    hello = 'hello world'
    if printable is True:
        print(hello)
        return None
    return hello
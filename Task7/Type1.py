def handle_2000(x):
    if x[0] == 'ROFF':
        return handle_roff(x)
    if x[0] == 'VCL':
        return handle_vcl(x)
    return 12


def handle_roff(x):
    adt = 0
    if x[2] == 'IDRIS':
        adt = 3
    if x[3] == 'VALA':
        return 0 + adt
    if x[3] == 'IO':
        return 1 + adt
    if x[3] == 'URWEB':
        return 2 + adt


def handle_vcl(x):
    if x[2] == 'PIC':
        return handle_pic(x)
    if x[2] == 'IDRIS':
        return handle_idris(x)


def handle_pic(x):
    if x[3] == 'VALA':
        return 6
    if x[3] == 'IO':
        return 7
    if x[3] == 'URWEB':
        return 8


def handle_idris(x):
    if x[1] == 1961:
        return 9
    if x[1] == 1974:
        return 10
    if x[1] == 1986:
        return 11


def main(x):
    if x[4] == 2000:
        return handle_2000(x)
    return 13

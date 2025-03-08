from math import ceil, prod


def get_I(num_set: set):  # code nesting cheat
    _I = set()
    for n in num_set:
        if -88 <= n < -13:
            _I.add(ceil(n / 5) + ceil(n / 3))
    return _I


def get_B(i_set: set):  # для упрощения функции main
    _B = set()
    for i in i_set:
        if -88 <= i <= 56:
            _B.add(4 * i)
    return _B


def get_SQ(num_set: set):  # может быть всё это потом патчнут
    _SQ = set()
    for n in num_set:
        if n <= -98 or n > -15:
            _SQ.add(abs(n) - n ** 2)
    return _SQ


def get_E(sq_set: set,
          b_set: set):  ## было бы плохо
    _E = set()
    for sq in sq_set:
        for b in b_set:
            if sq <= b:
                _E.add(abs(sq) - ceil(b / 2))
    return _E


def main(num_set: set):
    # смешная вилка -> psi, но для простоты написано num_set
    I_SET = get_I(num_set)
    B_SET = get_B(I_SET)
    SQ = get_SQ(num_set)
    E_SET = get_E(SQ, B_SET)

    return len(B_SET.union(E_SET)) + prod(e % 3
                                          for e in range(0, len(E_SET)))

from functools import cache


# 1


def ham_dist(num1: int, num2: int) -> str:
    return str(len(bin(num1 ^ num2)) - 2)


# 2 TODO


coded_message = [815608, 2064837,
                 2093080, 2063879,
                 196608, 2067983,
                 10457031, 1830912,
                 2067455, 2093116,
                 1044928, 2064407,
                 6262776, 2027968,
                 4423680, 2068231,
                 2068474, 1999352,
                 1019903, 2093113,
                 2068439, 2064455,
                 1831360, 1936903,
                 2067967, 2068456]


def encode_val(key=4, repeater=3, message=0b0):  # для чего тут key??????
    message = list(bin(message))
    message.pop(0)
    message.pop(0)
    message = ''.join(message)
    result = ''
    for char in message:
        result += char * repeater
    return int(result, 2)


def decode_val(key=4, repeater=3, message=None):
    print(message)  # idk yet


# 3


def dist_step(lev, i, j, s1, s2):
    c1 = s1[i - 1]
    c2 = s2[j - 1]

    a = lev[i - 1][j] + 1
    b = lev[i][j - 1] + 1
    c = lev[i - 1][j - 1] + (c1 != c2)
    d = c + 1
    lev[i][j] = min(a, b, c, d)


@cache
def lev_dist(str1: str, str2: str):
    m = len(str1)
    n = len(str2)
    d = [[i] for i in range(1, m + 1)]
    d.insert(0, list(range(0, n + 1)))
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            substitution_cost = int(str1[i - 1] != str2[j - 1])
            d[i].insert(j, min(d[i - 1][j] + 1,
                               d[i][j - 1] + 1,
                               d[i - 1][j - 1] + substitution_cost))
    return d[-1][-1]



def lev_dist2(param1: str, param2: str):
    len1 = len(param1)
    len2 = len(param2)

    lev = []
    for i in range(len1 + 1):
        lev.append([0] * (len2 + 1))
    for i in range(len1 + 1):
        lev[i][0] = i
    for j in range(len2 + 1):
        lev[0][j] = j

    for i in range(len1):
        for j in range(len2):
            dist_step(lev, i + 1, j + 1, param1, param2)
    return lev[len1][len2]


# 4 TODO


@cache
def lev_dist_ops(param1: str, param2: str):
    return 0


# 5 TODO


# 6 TODO


# main TODO: DRIVER


def main():
    print(lev_dist2('столб', 'слон'))
    #print(ham_dist(encode_val(4, 3, 0b1001), encode_val(4, 3, 0b1000)))

if __name__ == "__main__":
    main()

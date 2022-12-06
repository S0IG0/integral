from fractions import Fraction
from math import ceil


def trapezoid_method(f, a, b, n, debug=False):
    string = ''
    result = Fraction(0)
    h = Fraction(b - a, n)
    result += (f(a) + f(b))

    if debug:
        string = f'{h * Fraction(1, 2)}({float(f(a))} + 2 * ('
        print(f'h = (b - a)/n = ({b} - {a}) / {n} = {h}')
        print(f'a = {a}')
        print(f'f({a}) = {f(a)}')
        print(f'b = {b}')
        print(f'f({b}) = {f(b)}')

    for x in range(1, n):

        if debug:
            print(f'x{x} = {a} + {x} * {h} = {a + Fraction(x) * h}')
            print(f'f({a + Fraction(x) * h}) = {float(f(a + Fraction(x) * h)):.5}')
            string += f'{float(f(a + Fraction(x) * h))} + '

        result += 2 * f(a + Fraction(x) * h)
    if debug:
        string = string[:-2]
        string += f') + {float(f(b))}) = {float(Fraction(h, 2) * result)}'
        print(string)
    return Fraction(h, 2) * result


def simpsons_method(f, a, b, n, debug=False):
    out = []

    h = Fraction(b - a, 2 * n)
    result = Fraction(0)
    result += (f(a) + f(b))

    if debug:
        print(f'h = ({b} - {a}) / {2 * n} = {h}')
        print(f'{f(a)=}')
        print(f'{f(b)=}')

    for i in range(1, n):
        if debug:
            x = a + ((2 * i) * h)
            f_x = float(f(x))
            out.append((f'x{(2 * i)} = {a} + {(2 * i)} * {h} = {x};', f'f({x}) = {f_x:.5}'))

        result += 2 * f(a + ((2 * i) * h))

    for i in range(1, n + 1):
        if debug:
            x = a + ((2 * i - 1) * h)
            f_x = float(f(x))
            out.append((f'x{(2 * i - 1)} = {a} + {(2 * i - 1)} * {h} = {x};', f'f({x}) = {f_x:.5}'))
        result += 4 * f(a + ((2 * i - 1) * h))

    if debug:
        out.sort(key=lambda item: int(item[0][1:3]))
        print(*out, sep='\n')

        print(f'{Fraction(h, 3)}({float(f(a)):.5} + {float(f(b)):.5} + 2(', end='')
        print(*[item[1].split(' = ')[-1] for item in out if int(item[0][1]) % 2 == 0], sep=' + ', end=') + 4(')
        print(*[item[1].split(' = ')[-1] for item in out if int(item[0][1]) % 2 != 0], sep=' + ', end='))\n')

    return Fraction(h, 3) * result


def gauss_method(f, a, b, n, debug=False):
    results = []
    ai = [
        0.347854,
        0.652145,
        0.171324,
        0.360761,
        0.467913,
        0.101228,
        0.222381,
        0.313706,
        0.362683,
    ]

    ti = [
        0.861136,
        0.339981,
        0.932464,
        0.661209,
        0.238619,
        0.960289,
        0.796666,
        0.525532,
        0.183434,
    ]

    indexes = {
        4: {
            0: 0,
            1: 1,
            2: 1,
            3: 0,
        },
        6: {
            0: 2,
            1: 3,
            2: 4,
            3: 4,
            4: 3,
            5: 2,
        },
        8: {
            0: 5,
            1: 6,
            2: 7,
            3: 8,
            4: 8,
            5: 7,
            6: 6,
            7: 5,
        },

    }

    result = Fraction(0)
    for i in range(n):

        if i < n // 2:
            i = indexes[n][i]
            result += Fraction(ai[i]) * f(Fraction(a + b, 2) + (Fraction(b - a, 2) * Fraction(ti[i] * -1)))

            if debug:
                print(f'{ai[i]} * f({Fraction(a + b, 2)} + ({Fraction(b - a, 2)} * {ti[i] * -1}) = ', end='')
                print(f'{float(ai[i]) * f(Fraction(a + b, 2) + (Fraction(b - a, 2) * Fraction(ti[i] * -1))):.5}')
                results.append(f'{float(ai[i]) * f(Fraction(a + b, 2) + (Fraction(b - a, 2) * Fraction(ti[i] * -1))):.5}')

        else:
            index = indexes[n][i]
            result += Fraction(ai[index]) * f(Fraction(a + b, 2) + (Fraction(b - a, 2) * Fraction(ti[index])))
            if debug:
                print(f'{ai[index]} * f({Fraction(a + b, 2)} + ({Fraction(b - a, 2)} * {ti[index]}) = ', end='')
                print(f'{float(ai[index]) * f(Fraction(a + b, 2) + (Fraction(b - a, 2) * Fraction(ti[index]))):.5}')
                results.append(f'{float(ai[index]) * f(Fraction(a + b, 2) + (Fraction(b - a, 2) * Fraction(ti[index]))):.5}')
    if debug:
        print(Fraction((b - a), 2), end=' * (')
        print(*results, sep=' + ', end=')\n')
    return Fraction((b - a), 2) * result

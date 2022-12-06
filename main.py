from fractions import Fraction
from Integration_methods.trapezoid_method import trapezoid_method
from Integration_methods.trapezoid_method import simpsons_method
from Integration_methods.trapezoid_method import gauss_method
from matplotlib import pyplot as plt

L, K = Fraction(22, 10), Fraction(3)
a = Fraction((K - L), 2)
b = Fraction(K + L)


def f(x):
    global L, K
    return Fraction((x + L), (x ** 2 + x + K))


ns = (4, 6, 8)

trapezoid = [(float(trapezoid_method(f, a, b, n))) for n in ns]
simpsons = [float(simpsons_method(f, a, b, n)) for n in ns]
gauss = [float(gauss_method(f, a, b, n)) for n in ns]

plt.plot(ns, trapezoid, )
plt.plot(ns, simpsons, )
plt.plot(ns, gauss, )
plt.plot([0, max(ns)], [1.95652, 1.95652], c='deeppink')

plt.show()
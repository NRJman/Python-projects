first = 9.49
b = 35
n = 1
howlong = 0
from math import log, exp


def CountX(x):
    m = 0
    count = 1
    while count < x:
        count *= 2
        m += 1

    z = x/count
    a = (1-z)/(1+z)

    return m, a


def CountLn(x, eps):
    m, a = CountX(x)

    k = 1
    Lk = a
    Lcurr = Lk

    while Lk >= 4 * eps:
        k += 1
        Lk = (a ** (2 * k - 1)) / (2 * k - 1)
        Lcurr += Lk

    Rn = 1 / 4 * eps
    Lnx = m * log(2.0) - 2 * Lcurr - Rn
    return Lnx, Rn, k


def letsprintit():
    print('eps     n   Абсолютна похибка       Залишковий член')
    epsi = [10**i for i in range(-2, -15, -3)]
    for eps in epsi:
        LogX, Left, k = CountLn(first, eps)
        print('{}  \v{}  \v{}  \v{}'.format(eps, k, abs(LogX - log(first)), Left))

letsprintit()

print()
print('x(i)       Абсолютна похибка          Залишковий член')
eps = 10**(-8)
h = (b - first)/10
for i in range(0, 10):
    Logn, left, k = CountLn((first + h*i) / 2, eps)
    print('{:.3f}     {}     {}'.format(first + h*i, abs(Logn - log((first + h*i)/2)), left))
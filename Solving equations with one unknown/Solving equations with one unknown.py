from math import cos, sin


def func(x):
    return x**2 + x**3 - sin(x) - 0.5


def derivative(x):
    return 2*x + 3*x**2 - cos(x)


def sec_der(x):
    return 2 + 6*x + sin(x)


def minusfunc(x):
    return -x**2 - x**3 + sin(x) + 0.5


def iter_method(eps, x, min, max, myfunc):
    n = 0

    q = 1.0 - min/max
    L = 1.0/max

    sec_x = x
    x -= L*myfunc(x)

    while (1 - q)*eps/q <= abs(sec_x - x):
        sec_x = x
        x -= L*myfunc(x)
        n += 1

    comp = {}
    comp['MyX'] = x
    comp['MyAcc'] = abs(sec_x - x)*q/(1-q)
    comp['MyQuant'] = n
    return comp


def newton_method(eps, x, min,  myfunc, myderivative):
    xk = x
    n = 0
    while abs(myfunc(xk))/min > eps:
        xk = xk - myfunc(xk)/myderivative(xk)
        n += 1

    comp = {}
    comp['MyX'] = x
    comp['MyAcc'] = abs(myfunc(xk))/min
    comp['MyQuant'] = n
    return comp


print("                                 Just    iteration:")
print("{0:22} | {1:19} | {2:15}".format("Epsilon", "X", "Accuracy"))
tmp = 5
i = 0
eps = 10**(-2)
for i in range(tmp):
    dothat = iter_method(eps, -1.3, 1.48, 2.83, func)
    print("{0:22} | {1:15} | {2:15}".format(eps, dothat['MyX'], dothat['MyAcc']))
    eps /= 10 ** 3
print()

i = 0
eps = 10**(-2)
print("{0:22} | {1:19} | {2:15}".format("Epsilon", "X", "Accuracy"))
for i in range(tmp):
    dothat = iter_method(eps, -0.42, 1.21, 1.26, minusfunc)
    print("{0:22} | {1:15} | {2:15}".format(eps, dothat['MyX'], dothat['MyAcc']))
    eps /= 10 ** 3
print()

#0.75 0.9 0.83
i = 0
eps = 10**(-2)
print("{0:22} | {1:19} | {2:15}".format("Epsilon", "X", "Accuracy"))
for i in range(tmp):
    dothat = iter_method(eps, 0.83, 2.5, 3.76, func)
    print("{0:22} | {1:15} | {2:15}".format(eps, dothat['MyX'], dothat['MyAcc']))
    eps /= 10 ** 3
print()
#--------------------------------------------------------------------------------
print("                                      Newton's method   ")
print("{0:22} | {1:19} | {2:15}".format("Epsilon", "X", "Accuracy"))
tmp = 4
i = 0
eps = 10**(-2)
for i in range(tmp):
    dothat = newton_method(eps, -1.35, 1.48, func, derivative)
    print("{0:22} | {1:15} | {2:15}".format(eps, dothat['MyX'], dothat['MyAcc']))
    eps /= 10 ** 3
print()

tmp = 4
i = 0
eps = 10**(-2)
for i in range(tmp):
    dothat = newton_method(eps, -0.3, 0.36, func, derivative)
    print("{0:22} | {1:15} | {2:15}".format(eps, dothat['MyX'], dothat['MyAcc']))
    eps /= 10 ** 3
print()

tmp = 4
i = 0
eps = 10**(-2)
for i in range(tmp):
    dothat = newton_method(eps, 0.84, 7.03, func, derivative)
    print("{0:22} | {1:15} | {2:15}".format(eps, dothat['MyX'], dothat['MyAcc']))
    eps /= 10 ** 3
print()

print("\nLet's compare these numbers:")
print("{0:22} | {1:10} | {2:10}".format("Eps", "Iteration method", "Newton's method"))
i = 0
eps = 10**(-2)
for i in range(tmp):
    first_res = iter_method(eps, -1.3, 1.48, 2.83, func)
    second_res = newton_method(eps, -1.35, 1.48, func, derivative)
    print("{0:22} | {1:16} | {2:10}".format(eps, first_res['MyQuant'], second_res['MyQuant']))
    eps /= 10**3
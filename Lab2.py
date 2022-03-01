import math

def first():
    a = input()
    print(a[2:3:1])
    n = len(a)
    print(a[n - 2:n - 1:1])
    print(a[0:5:1])
    print(a[0:n - 2:1])
    print(a[::2])
    print(a[1::2])
    print(a[::-1])
    print(a[::-2])
    print(len(a))


def second():
    a = input()
    n = len(a)
    print(a[round(n / 2)::1], a[:round(n / 2):1], sep='')


def third():
    a = input()
    n = len(a)
    b = a[::-1]
    print(a[(n - b.index("h")):a.index("h"):-1])

def four():
    a = input()
    if "f" in a:
        if a.find("f") != a.rfind("f"):
            print(a.find("f"), a.rfind("f"))
        if a.find("f") == a.rfind("f"):
            print(a.find("f"))
    else:
        print()

def fifth():
    a = list(map(int, input().split(" ")))
    for c, n in enumerate(a):
        if n > a[c - 1]:
            print(n, end=" ")
    print()

def sixth():
    a = list(map(int, input().split(" ")))
    for c, n in enumerate(a):
        if (n > 0 and a[c - 1] > 0) or (n < 0 and a[c - 1] < 0):
            print(a[c - 1], n)
            break
# first()
# second()
# third()
# four()
# fifth()
# sixth()
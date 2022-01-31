"""
Quick Power
"""


def qp(a, n):
    res = 1
    while n:
        if n & 1:
            res *= a
        a *= a
        n >>= 1
    return res


def qpm(a, n, m):
    res = 1
    while n:
        if n & 1:
            res = (res * a) % m
        a = a * a % m
        n >>= 1
    return res

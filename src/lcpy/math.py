"""
math related algorithms
"""

def gcd(a, b):
    """
    non recursive
    while b:
        a, b = b, a % b
    return a
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def coprime(a, b):
    return gcd(a, b) == 1

def lcm(a, b):
    """
    Least Common Multiple
    """
    return a * b // gcd(a, b)
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

def primeFactorization(n):
    """
    pf is prime factor
    """
    if n == 1:
        yield 1
    pf = 2
    while n > 1:
        while n % pf == 0:
            n //= pf
            yield pf
        pf += 1
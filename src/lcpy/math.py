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

def gen_primes():
    """ 
    Generate an infinite sequence of prime numbers.
    from stackoverflow
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
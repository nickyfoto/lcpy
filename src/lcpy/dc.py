"""Divice and Conquer"""

def sort_return_index(l):
    """
    sort an array, return the sorted indices
    """
    return sorted(range(l), key=lambda k: groupSizes[k])



def find_n(num):
    """
    Params:
        num: a decimal number
    Return:
        n: power of 2 length of the binaray representation for given num.
    """
    n = 1
    while 2**n <= num:
        n *= 2
    return n

def convert(num, n):
    """
    convert a decimal num into its binary form of length n
    prepend 0 if the length is less than n
    """
    b = bin(num)[2:]
    return b.zfill(n)

def convertb(x, y):
    """
    convert x, y into binary form of equal length
    """
    n = max(find_n(x), find_n(y))
    xb = convert(x, n)
    yb = convert(y, n)
    return xb, yb

def easyMultiply(x, y):
    """
    Multiplication with bit manipulation
    """
    xb, yb = convertb(x, y)
    def multiply(xb, yb):
        n = len(xb)
        if n == 1:
            return int(xb)*int(yb)
        xl = xb[:n//2]
        xr = xb[n//2:]
        yl = yb[:n//2]
        yr = yb[n//2:]
        A = multiply(xl, yl)
        B = multiply(xr, yr)
        C = multiply(xl, yr)
        D = multiply(xr, yl)
        z = ((A<<n) + ((C+D)<<(n//2))) + B
        return z
    return multiply(xb, yb)

def fastMultiply(x, y):
    """
    DVP Figure 2.1
    """
    xb, yb = convertb(x, y)
    
    def multiply(xb, yb):
        n = len(xb)
        if n == 1:
            return int(xb)*int(yb)
        xl = xb[:n//2]
        xr = xb[n//2:]
        yl = yb[:n//2]
        yr = yb[n//2:]
        A = multiply(xl, yl)
        B = multiply(xr, yr)
        xl_plus_xr, yl_plus_yr = convertb(int(xl, 2)+ int(xr, 2), 
                                        int(yl, 2)+ int(yr, 2))
        C = multiply(xl_plus_xr, yl_plus_yr)
        z = ((A<<n) + ((C - A - B)<<(n//2))) + B
        return z
    
    return multiply(xb, yb)


def fastSelect(a, k):
    """
    median is defined as ceiling(n/2)
    1. break a into ceiling n/5 groups
    2. for i = 1 ... n/5 sort group[i], let mi = median(Gi)
    3. Let s = {m1, m2...m n/5}
    4. find the median p of s recursively call p = FastSelect(s, n/10)
    5. partition A into A < p, A = p and A > p
        if k < |a<p| then return FastSelect(A<p, k)
        if k > |a<p|+|a=p| then return FastSelect(A>p, k-|a<p|-|a=p|)
        else return p

    Params:
        a: array of int
        k: index
    
    Return:
        kth number in sorted(a)
    """
    n = len(a)
    if n < 6:
        return sorted(a)[k-1]
    groups = [a[x:x+5] for x in range(n)[::5]]
    s = [sorted(g)[len(g)//2] for g in groups]
    p = fastSelect(s, n//10)
    small = [i for i in a if i < p]
    equal = [i for i in a if i == p]
    big = [i for i in a if i > p]
    if k <= len(small):
        return fastSelect(small, k)
    elif k > len(small) + len(equal):
        return fastSelect(big, k-len(small) - len(equal))
    else:
        return p
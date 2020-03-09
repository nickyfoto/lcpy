from random import random

def merge(B, C):
    res = []
    i = 0
    j = 0
    while len(B) > 0 and len(C) > 0:
        if B[i] <= C[j]:
            res.append(B.pop(0))
        else:
            res.append(C.pop(0))
    if len(B) == 0:
        return res + C        
    elif len(C) == 0:
        return res + B
    
def merge_sort(A):
    n = len(A)
    if n == 1:
        return A
    else:
        B = merge_sort(A[:n//2])
        C = merge_sort(A[n//2:])
        return merge(B, C)

def shuffle(arr):
    """
    https://algs4.cs.princeton.edu/11model/Knuth.java.html
    """
    for i in range(len(arr)):
        r = int(random() * (i + 1))
        arr[i], arr[r] = arr[r], arr[i]
    return arr

def top_2_min_indices(arr):
    """
    one pass to find indices of top two min val
    """
    mn0 = mn1 = None
    for i, n in enumerate(arr):
        if mn0 is None or n < arr[mn0]:
            mn1 = mn0
            mn0 = i
        elif mn1 is None or n < arr[mn1]:
            mn1 = i
    return mn0, mn1
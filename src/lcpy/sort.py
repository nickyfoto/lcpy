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
"""
bit manipulation

AND: 67
<<: 67
XOR: 67, 136
"""


def singleNumber(nums):
    """
    lc 136
    """
    a = 0
    for n in nums:
        a ^= n
    return a

def binarize(nums):
    """
    input: [3,10,5,25,2,8]
    output:
        [[0, 0, 0, 1, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0]]
    """
    L = len(bin(max(nums))) - 2
    nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]
    return nums
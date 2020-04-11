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
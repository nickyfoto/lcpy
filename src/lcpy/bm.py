"""
bit manipulation

XOR: 136
"""


def singleNumber(nums):
    """
    lc 136
    """
    a = 0
    for n in nums:
        a ^= n
    return a
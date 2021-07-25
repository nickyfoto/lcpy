"""
diff array
"""

def range_to_freq(requests, n):
    """
    given a range of requests
    return frequnency array

    n: length of array
    requests: array of [start, end] indices

    https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/
    1, 2, 3, 4, 5
       +  +  +
    +  +
    --------------
    1  2  1  1  0
    """

    diff = [0] * (n + 1)
    for s, e in requests:
        diff[s] += 1
        diff[e + 1] -= 1
    freq = [0] * n
    pre = 0
    for i in range(n):
        pre += diff[i]
        freq[i] = pre
    return freq

# print(range_to_freq([[1, 3], [0, 1]], 5))
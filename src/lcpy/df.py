"""
diff array

798 and 1674 are similar


"""

def range_to_freq(requests, n):
    """
    LC 1589
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

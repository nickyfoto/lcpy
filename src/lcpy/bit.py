"""
bit manipulation
"""
from typing import List

def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
    """
    https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/discuss/1676852/Python3-bitmask
    """
    seen = set()
    for word in startWords:
        m = 0
        for ch in word:
            m ^= 1 << ord(ch)-97
        seen.add(m)

    ans = 0
    for word in targetWords:
        m = 0
        for ch in word:
            m ^= 1 << ord(ch) - 97
        for ch in word:
            if m ^ (1 << ord(ch)-97) in seen:
                ans += 1
                break
    return ans



class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n

    def update(self, i, delta):
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

    # use query can also get rangeSum(i, j)

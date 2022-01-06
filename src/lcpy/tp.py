"""
Two pointers
  3 https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
 76 https://leetcode.com/problems/minimum-window-substring/
209 https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
159
340 
"""


from types import List
from math import inf
from collections import Counter

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    """
    209
    """
    left = right = 0
    n = len(nums)
    acc = 0
    res = inf
    for right in range(n):
        acc += nums[right]
        while acc >= target:
            res = min(res, right - left + 1)
            acc -= nums[left]
            left += 1
    return res if res != inf else 0

def lengthOfLongestSubstring(self, s: str) -> int:
    """
    3
    """
    res = 0
    right = left = 0
    n = len(s)
    c = Counter()
    for right in range(n):
        c[s[right]] += 1
        while c[s[right]] > 1:
            c[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

def minWindow(self, s: str, t: str) -> str:
    """
    76 use a counter to keep track of difference between current string and target string
    """
    ct = Counter(t)
    right = left = 0
    length = inf
    res = ""
    needed_for_t = len(t)
    for right, ch in enumerate(s):
        if ch in ct:
            if ct[ch] > 0:
                needed_for_t -= 1
            ct[ch] -= 1
        while needed_for_t == 0:
            if right - left + 1 < length:
                length = right - left + 1
                res = s[left: right + 1]
            if s[left] in ct:
                ct[s[left]] += 1
                if ct[s[left]] > 0:
                    needed_for_t += 1
            left += 1
    return res

def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    """
    159, 340
    """
    res = left = right = 0
    n = len(s)
    c = Counter()
    for right, ch in enumerate(s):
        c[ch] += 1
        while len(c) > 2:
            c[s[left]] -= 1
            if c[s[left]] == 0:
                del c[s[left]]
            left += 1
        res = max(res, right - left + 1)
    return res
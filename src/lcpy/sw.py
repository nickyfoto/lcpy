"""
sliding window


LZL cheatsheet
https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175088/C%2B%2B-Maximum-Sliding-Window-Cheatsheet-Template!

three types


          / find longest substring/array satisfy certain condition
         /
string  /
array  ---- find longest substring/array satisfy certain condition given that you can update k elements
        \
         \
          \ count the number of substring/array satisfy certain condition

1. find longest substring/array satisfy certain condition
  3
  159
  340
  1838

2. find longest substring/array satisfy certain condition given that you can update k elements
  1004
   424
  2024

3. count the number of substring/array satisfy certain condition
  713
  930
  992
  1248
  2062



2009
Iterate left point, let right point to go as far as it can
    update results according to business results


why 2024, 424 return len(s) - l

left and right are always keeping a valid distance 
we can use their diff to get the result



713, 1208 need to use while and if condition to update answer

3 and 1695 have similar pattern






76(minimum)


"""
from typing import List


def lengthOfLongestSubstring(self, s: str) -> int:
    """
    LC 3
    update l whenever a repeated character found
    """   
    d = {}
    l = 0
    res = 0
    for r, ch in enumerate(s):
        ### business logic ###
        if ch in d:
            l = max(l, d[ch] + 1)
        ### business logic ###
        res = max(res, r - l + 1)
        d[ch] = r
    return res

def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    """
    159
    """
    d = {}
    l = 0
    res = 0
    for r, ch in enumerate(s):
        if ch not in d and len(d) == 2:
            v = min(d.values())
            l = max(l, v + 1)
            del d[s[v]]
        res = max(res, r - l + 1)
        d[ch] = r
    return res

def lengthOfLongestSubstringKDistinct(self, s: str, K: int) -> int:
    """
    340
    """
    if K == 0:
        return 0
    d = {}
    l = 0
    res = 0
    for r, c in enumerate(s):
        if len(d) == K and c not in d:
            v = min(d.values())
            # k = min(d, key=lambda x: d[x])
            l = max(l, v + 1)
            del d[s[v]]
        res = max(res, r - l + 1)
        d[c] = r
    return res

def minWindow(self, s: str, t: str) -> str:
    """
    LC 76
    """
    ct = Counter(t)
    l = 0
    needed = 0
    start = 0
    mn_l = inf
    for r, c in enumerate(s):
        if c in ct:
            if ct[c] > 0:
                needed += 1
            ct[c] -= 1
        while needed == len(t):
            curr_l = r - l + 1
            if curr_l < mn_l:
                mn_l = curr_l
                start = l
            if s[l] in ct:
                ct[s[l]] += 1
                if ct[s[l]] > 0:
                    needed -= 1
            l += 1
    if mn_l == inf:
        return ""
    return s[start:start+mn_l]

def longestOnes(self, nums: List[int], k: int) -> int:
    """
    LC 1004
    """
    res = 0
    if k == 0:
        for k, g in groupby(nums):
            if k == 1:
                res = max(res, len(list(g)))
        return res
    
    
    zeros = deque()
    l = 0
    for r, num in enumerate(nums):
        if num == 0 and len(zeros) == k:
            l = zeros.popleft() + 1
        res = max(res, r - l + 1)
        if num == 0:
            zeros.append(r)
    return res
# 1248 count number of nice subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-O(1)-Space


# atMost(k) - atMost(k - 1)



# https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175088/C%2B%2B-Maximum-Sliding-Window-Cheatsheet-Template!


# The following problems are also solvable using the shrinkable template with the "At Most to Equal" trick

# 930. Binary Subarrays With Sum (Medium)
#   num of subarray with a sum equal to goal

def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

    """
    Hash + prefix
    """

    res = 0
    preSum = 0
    c = Counter()
    c[0] = 1
    for num in nums:
        preSum += num                # update preSum
        res += c[preSum - goal]      # update res
        c[preSum] += 1               # update c
    return res

# 992. Subarrays with K Different Integers
#   num of subarray with num of unique interger equal to k
def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
    """
    Sliding window : Distinct Characters


    update c at the beginning

    if condition not satisfied
    make it satify

    update pre_cnt

    update res
    """
    counter = {}
    pre_cnt = 0
    l = 0
    res = 0
    for r in range(len(A)):
        counter[A[r]] = counter.get(A[r], 0) + 1
        if len(counter) > K:
            counter.pop(A[l]) # counter[A[l]] is always 1
            l += 1
            pre_cnt = 0 # reset pre_cnt here
        while counter[A[l]] > 1:
            counter[A[l]] -= 1
            pre_cnt += 1
            l += 1
        if len(counter) == K:
            res += pre_cnt + 1
    return res

# 1248. Count Number of Nice Subarrays (Medium)
#   num of subarray with k odd numbers in it

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    l = count = res = odds = 0
    for _, num in enumerate(nums):
        if num & 1:
            odds += 1
            count = 0
        while odds == k:
            odds -= nums[l] & 1
            l += 1
            count += 1
        res += count
    return res

# 2062. Count Vowel Substrings of a String (Easy)
#   num of subarray have all vowels

def countVowelSubstrings(self, word: str) -> int:
    ans = 0 
    freq = defaultdict(int)
    for i, x in enumerate(word): 
        if x in "aeiou": 
            if not i or word[i-1] not in "aeiou": 
                jj = j = i # set anchor
                freq.clear()
            freq[x] += 1
            while len(freq) == 5 and all(freq.values()): 
                freq[word[j]] -= 1
                j += 1
            ans += j - jj
    return ans 


def countVowelSubstrings(self, word: str) -> int:
    last_vowels = {c:-1 for c in 'aeiou'}
    last_non_vowel = -1
    res = 0
    for i, c in enumerate(word):
        if c in last_vowels:
            last_vowels[c] = i
            res += max(min(last_vowels.values()) - last_non_vowel, 0)
        else:
            last_non_vowel = i
    return res

def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    """
    1052
    grumpy[i] is 1 means he is grumpy
    consecutive for minutes
    """
    res = 0
    n = len(customers)
    happy = sum(customers[i] for i in range(n) if not grumpy[i])
    
    for r, num in enumerate(customers):
        if grumpy[r]:
            happy += num
        # this is a special case
        # from current r look back minutes
        if r - minutes >= 0 and grumpy[r - minutes]:
            happy -= customers[r - minutes]
        res = max(res, happy)
    return res

def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    """
    can also use classic window
    pop item from left when does not satify condition
    """
    res = 0
    n = len(customers)
    happy = sum(customers[i] for i in range(n) if not grumpy[i])
    window = deque()
    for r, num in enumerate(customers):
        if grumpy[r]:
            happy += num
            window.append(r)
        if window and r - window[0] >= minutes:
            happy -= customers[window.popleft()]
        res = max(res, happy)
    return res

def maxFrequency(self, nums: List[int], k: int) -> int:
    """
    1838

    """
    nums.sort()
    sm = 0
    l = 0
    res = 0
    for r, num in enumerate(nums):
        sm += num
        # use window length to calculate 
        # diff with sm and compare it with k
        while sm + k < num * (r - l + 1):
            sm -= nums[l]
            l += 1
        res = max(res, r - l + 1)
    return res
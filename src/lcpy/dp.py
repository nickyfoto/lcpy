"""Dynamic Programming"""

import math
from pprint import pprint

class Knapsack:
    def __init__(self):
        pass

    def knapsackNoRepeat(self, v, wt, B):
        """
        Each item can only be count once
        Params:
            v: list of values for each item
            wt: list of weights for each item
            B: bag size
        Returns:
            maximum value can acheive under weight and bag constrain
        Algo:
            n = number of items
            use a table of shape (n+1, B+1) to record the max value
            we can get considering the ith item. The col represents
            the max value acheived with current available weight

            if the weight of (i-1)th item is less than current 
            available weight w
                we set the current value to be the max of
                    the total value if take (i-1)th item
                    and 
                    the total value of not take (i-t)th item
            
            the total value of take (i-1)th item is calculated by
                value of (i-1)th item + value acheived without (i-1)them
            
            the total value of not take (i-t)th item is record by
                the value acheived with the same weight space
                in the previous row
        """
        n = len(v)
        value = [[0] * (B+1) for _ in range(n + 1)]
        for i in range(1, n+1):
            for w in range(1, B+1):
                value[i][w] = value[i-1][w]
                if wt[i-1] <= w:
                    value[i][w] = max(v[i-1] + value[i-1][w-wt[i-1]], value[i-1][w])
        return value[n][B]

    def knapsackRepeat(self, v, w, B):
        n = len(v)
        dp = [0] * (B+1)
        for b in range(B+1):
            for i in range(n):
                if w[i] <= b:
                    dp[b] = max(dp[b], dp[b-w[i]]+v[i])
        
        return dp[B]

    def ksNoRepeat_recur(self, B, wt, val, n):
        if n == 0 or B == 0:
            return 0
        if wt[n-1] > B:
            return self.ksNoRepeat_recur(B, wt, val, n-1)
        else:
            return max(val[n-1]+ self.ksNoRepeat_recur(B-wt[n-1], wt, val, n-1),
                       self.ksNoRepeat_recur(B, wt, val, n-1))
    
    def number_of_possible_fill(self, nums, target):
        """
        https://www.lintcode.com/problem/backpack-v/note/212945
        """
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j]
                if nums[i-1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        # print()
        # pprint(dp)
        return dp[n][target]

        # 1D dp
        # dp = [0] * (target + 1)
        # dp[0] = 1
        # for i in range(1, n + 1):
        #     for j in range(nums[i - 1], target + 1)[::-1]:
        #         dp[j] += dp[j - nums[i - 1]]
        # return dp[target]


def max_sum_continious_seq(a):
    """"""
    n = len(a)
    L = [(a[0], 0, 0)]
    for i in range(1, n):
        max_val, start_from  = L[i-1][:2]
        if max_val > 0:
            L.append((max_val+a[i], start_from, i))
        else:
            L.append((a[i], i, i))
    L.sort()
    start, end = L[-1][1:] 
    return a[start:end+1]

def LIS(a):
    """
    Longest Increasing Subsequences (LIS)
    length of LIS
    """
    L = [1] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[j] < a[i] and L[i] < 1+L[j]:
                L[i] = 1 + L[j]
    return max(L)

def LCS(text1, text2):
    """length of Longest common subsequences (LCS)
    https://leetcode.com/problems/longest-common-subsequence/
    """
    n1 = len(text1) + 1
    n2 = len(text2) + 1
    dp = [[0] * n2 for _ in range(n1)]
    for i in range(1, n1):
        for j in range(1, n2):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def LCS_string(text1, text2): 
    """
    LCS output string
    """
    n1 = len(text1) + 1
    n2 = len(text2) + 1
    dp = [["" for _ in range(n2)] for _ in range(n1)]
    for i in range(1, n1):
        for j in range(1, n2):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + text1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

def longest_common_substring(X, Y): 
    """
    length of common substring
    """
    # Create a table to store lengths of 
    # longest common suffixes of substrings.  
    # Note that LCSuff[i][j] contains the  
    # length of longest common suffix of  
    # X[0...i-1] and Y[0...j-1]. The first 
    # row and first column entries have no 
    # logical meaning, they are used only 
    # for simplicity of the program. 
      
    # LCSuff is the table with zero  
    # value initially in each cell 
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for l in range(m + 1)] 
      
    # To store the length of  
    # longest common substring 
    result = 0 
  
    # Following steps to build 
    # LCSuff[m+1][n+1] in bottom up fashion 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if X[i - 1] == Y[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
    return result 

def chainMultiply(m, n):
    """
    return the min cost of performing chain matrix multiplication
    Params:
        m: size of matrices
        n: number of matrices

        e.g.
            m = [50,20,1,10,100]
	        n = 4
            multiply 4 matrices of size
            (50,20), (20,1), (1, 10), (10, 100)
    
    Algo:
        TODO
    """
    c = [[x] * n for x in [0] * n]
    for s in range(n-1):
        for i in range(0, n-s-1):
            j = i+s+1
            c[i][j] = math.inf
            for l in range(i, j):
                cur = c[i][l] + c[l+1][j] + m[i-1]*m[l]*m[j]
                if c[i][j] > cur:
                    c[i][j] = cur
    return c[0][n-1]



def Optimal_BST(keys, freq, n):
    """
    TODO
    cost: (n+1, n+1) matrix
            diag is freq
    """
    cost = [[x] * (n+1) for x in [0] * (n+1)]
    for i in range(n):
        cost[i][i] = freq[i]
    for L in range(2, n+1):
        for i in range(n-L+2):
            j = i+L-1
            cost[i][j] = math.inf
            for r in range(i, j+1):
                left = cost[i][r-1] if r > i else 0
                right = cost[r+1][j] if r < j else 0
                s = sum(freq[i:j+1])
                c = left + right + s
                if c < cost[i][j]:
                    cost[i][j] = c
    return cost[0][n-1]


def coin_change(money, coins):
    """
    unlimited supply of coins
    return 1 if we can make the change
           0 we cannot
    """
    A = [0] * (money+1)
    A[0] = 1
    for u in range(1, money+1):
        for c in range(len(coins)):
            if u >= coins[c]:
                max_ = 0
                if A[u-coins[c]] > max_:
                    max_ = A[u-coins[c]]
                    A[u] = A[u-coins[c]]
    return A[money]


def coin_change2(money, coins):
    """
    can only use every coin once for the coin in coins
    return True or False
    """
    for c in coins:
        if c == money:
            return True
    
    D = [0] * (money+1)
    for m in range(1, money+1):
        for c in coins:
            if m == c:
                D[m] = c
    left_m = money
    for i in range(money, 0, -1):
        if D[i]:
            if left_m >= D[i]:
                left_m -= D[i]
                if left_m == 0:
                    return True
    return False

def coin_change3(money, coins):
    """
    given money and coins
    return min number of coins to make the change
    if cannot make the change, return -1
    """
    D = [float('inf')] * (money + 1)
    D[0] = 0
    for m in range(1, money+1):
        for c in coins:
            if m >= c:
                D[m] = min(D[m - c] + 1, D[m])
    if D[money] == float('inf'):
        return -1
    return D[money]

def coin_change4(money, coins):
    """
    given amount of money and coins
    return number of ways to change the amount
    """
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] += dp[x - coin]
    return dp[money]


def coin_change5(money, coins):
    """
    https://leetcode.com/problems/combination-sum-iv/submissions/
    """
    dp = [0] * (money + 1)
    dp[0] = 1
    for i in range(1, len(dp)):
        dp[i] = sum(dp[i - coins[j]] for j in range(len(coins)) if i - coins[j] >= 0)
        # print(dp)
    return dp[money]

    

def is_palindrome(s):
    """
    given a string
    return a matrix of 0 and 1 
    where matrix[i][j] is whether s[i:j+1] is a palindrome
    complexity O(n^2)
    """
    n = len(s)
    matrix = [[0] * n for _ in range(n)]
    for mid in range(n):
        i = j = mid
        while 0 <= i and j < n and s[i] == s[j]:
            matrix[i][j] = 1
            i -= 1
            j += 1
        i = mid
        j = mid + 1
        while 0 <= i and j < n and s[i] == s[j]:
            matrix[i][j] = 1
            i -= 1
            j += 1
    return matrix


    
    
def copyBooks(pages, k):
    """
    TLE
    from math import inf
    from itertools import combinations, accumulate
    if k == 1:
        return sum(pages)
    n = len(pages)
    if n <= k:
        return max(pages)
    splits = list(range(n-1))
    res = inf
    options = combinations(splits, k - 1)
    acc = list(accumulate(pages))
    
    for op in options:
        local_max = 0
        for i in range(len(op)):
            if i == 0:
                local_max = max(local_max, acc[op[i]])
                if len(op) == 1:
                    local_max = max(local_max, acc[-1] - acc[op[i]])    
            elif i == len(op) - 1:
                local_max = max(local_max, acc[op[i]] - acc[op[i-1]])
                local_max = max(local_max, acc[-1] - acc[op[i]])
            else:
                local_max = max(local_max, acc[op[i]] - acc[op[i-1]])
        res = min(local_max, res)
    return res
    """
    if k == 1:
        return sum(pages)
    n = len(pages)
    if n <= k:
        return max(pages)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0] = [math.inf] * (n + 1)
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = math.inf
            s = 0
            for l in range(j + 1)[::-1]:
                if dp[i - 1][l] != math.inf:
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][l], s))
                if l > 0:
                    s += pages[l - 1]
    # print(dp)
    return dp[-1][-1]

def copyBooks2(pages, k):
    """
    binary search + greedy
    """
    def valid(pages, limit, k):
        cnt = 1
        sm = 0
        for p in pages:
            if p > limit: return False
            if p + sm > limit:
                cnt += 1
                sm = p
            else:
                sm += p
        return cnt <= k
        
    n = len(pages)
    if n == 0: return 0
    max_page = max(pages)
    sm = sum(pages)
    l = max_page
    r = sm
    while l + 1 < r:
        mid = (r + l) // 2
        if valid(pages, mid, k):
            r = mid
        else:
            l = mid
    if valid(pages, l, k): return l
    return r
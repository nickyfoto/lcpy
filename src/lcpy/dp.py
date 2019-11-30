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
        value = [[x] * (B+1) for x in [0] * (n+1)]
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

def LCS(x, y):
    """length of Longest common subsequences (LCS)"""
    n = len(x)
    L = [[x] * n for x in [0] * n]
    for i in range(n):
        for j in range(n):
            if x[i] == y[j]:
                if i == 0 or j == 0:
                    L[i][j] = 1
                else:
                    L[i][j] = 1 + L[i-1][j-1]
            else:
                if i == 0 or j == 0:
                    L[i][j] = 0
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[n-1][n-1]

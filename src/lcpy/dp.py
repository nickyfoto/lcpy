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
        """
        n = len(v)
        value = [[x] * (B+1) for x in [0] * (n+1)]
        for w in range(1, B+1):
            for i in range(1, n+1):
                value[i][w] = value[i-1][w]
                if wt[i-1] <= w:
                    value[i][w] = max(v[i-1] + value[i-1][w-wt[i-1]], value[i-1][w])

        return value[n][B]
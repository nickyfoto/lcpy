from itertools import permutations

def unique_comb_of_two_lists(A, B):
    """
    get all unique combinations of two lists in Python

    https://leetcode.com/problems/maximum-compatibility-score-sum/submissions/
    """
    res = []
    for p in permutations(A, len(B)):
        zipped = zip(p, B)
        res.append(list(zipped))
    return res

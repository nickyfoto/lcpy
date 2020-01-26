"""
backtrack examples
"""


def value_based_permutation(nums):
    """
    when a number has the same val with its previous
    we can use this number only if its previous is used
    """
    def backtrack(nums, used, lst, res):
        if len(lst) == len(nums):
            res.append(lst.copy())
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i - 1] == nums[i] and not used[i - 1]):
                    continue
                used[i] = True
                lst.append(nums[i])
                backtrack(nums, used, lst, res)
                used[i] = False
                lst.pop()
        
    res = []
    used = [False] * len(nums)
    lst = []
    nums.sort()
    backtrack(nums, used, lst, res)

    return res
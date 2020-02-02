"""
binary search
"""

def bs_recur(nums, target):
    """
    recursive
    if not found, return -1
    """
    mid = len(nums) // 2
    if mid == 0 and target != nums[0]:
        return -1
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return bs_recur(nums[:mid], target)
    else:
        b = bs_recur(nums[mid:], target)
        return -1 if b == -1 else mid + b
        
def bs(nums, target):
    """
    while version
    """
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (hi + lo) // 2
        if target < nums[mid]:
            hi = mid
        elif target > nums[mid]:
            lo = mid + 1
        else:
            return mid
    return -1


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
    l, r = 0, len(nums) - 1
    res = -1
    while l <= r:
        # mid = (l + r) // 2
        mid = l + (r - l) // 2 # prevent overflow in Java
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            res = mid
            break
    return res


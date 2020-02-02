"""
binary search
"""

def bs(nums, target):
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
        return bs(nums[:mid], target)
    else:
        b = bs(nums[mid:], target)
        return -1 if b == -1 else mid + b
        



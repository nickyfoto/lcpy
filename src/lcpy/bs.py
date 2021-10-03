"""
binary search

while l < r:
    mid = l + (r - l) // 2
    # mid = r - (r - l) // 2
    if isOK(mid):
        left = mid + 1
    else:
        right = mid
    return left
"""
from types import List




class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        
        """
        n = len(nums)
        l = 0
        r = n - 1
        if nums[r] >= nums[l]:
            return nums[l]
        
        while l < r:
            mid = l + (r - l) // 2
            # mod = r - (r - l) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]













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


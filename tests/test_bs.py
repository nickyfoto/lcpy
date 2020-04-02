"""
test binary search
"""

from lcpy import bs

def test_bs():

    nums = [1,2,3,4,5]
    assert bs(nums, 1) == 0
    assert bs(nums, 2) == 1
    assert bs(nums, 4) == 3
    assert bs(nums, 5) == 4
    assert bs(nums, 10) == -1
    assert bs(nums, -1) == -1

    nums = [5]
    assert bs(nums, 5) == 0
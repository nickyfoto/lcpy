from lcpy.bm import singleNumber


def test_singleNumber():
    nums = [2,2,1]
    assert singleNumber(nums) == 1
    nums = [4,1,2,1,2]
    assert singleNumber(nums) == 4
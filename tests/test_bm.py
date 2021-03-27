from lcpy.bm import singleNumber, binarize


def test_singleNumber():
    nums = [2,2,1]
    assert singleNumber(nums) == 1
    nums = [4,1,2,1,2]
    assert singleNumber(nums) == 4

def test_binarize():
    nums = [3,10,5,25,2,8]
    assert binarize(nums) == [[0, 0, 0, 1, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0]]

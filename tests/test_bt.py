"""
test backtrack
"""
from lcpy import value_based_permutation

def test_value_based_permutation():
    nums = [1,1,2]
    Output = [
                [1,1,2],
                [1,2,1],
                [2,1,1]
                ]
    assert value_based_permutation(nums) == Output
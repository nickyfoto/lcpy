"""
test backtrack
"""
from lcpy import value_based_permutation, subsets

def test_value_based_permutation():
    nums = [1,1,2]
    Output = [
                [1,1,2],
                [1,2,1],
                [2,1,1]
                ]
    assert value_based_permutation(nums) == Output

def test_subsets():
    nums = [1,2,3]
    Output = [
                [3],
                [1],
                [2],
                [1,2,3],
                [1,3],
                [2,3],
                [1,2],
                []
                ]
    ds = {tuple(v):v for v in  subsets(nums)}
    do = {tuple(v):v for v in  Output}
    assert ds == do
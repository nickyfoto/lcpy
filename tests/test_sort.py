"""
test sort
"""
from lcpy import top_2_min_indices

def test_top_2_min_indices():
    arr = [1,5,2]
    assert top_2_min_indices(arr) == (0, 2)

    arr = [1,5,1]
    assert top_2_min_indices(arr) == (0, 2)
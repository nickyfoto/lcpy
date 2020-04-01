"""
test segment tree
"""

from lcpy import SegmentTree

def test_SegmentTree():
    nums = [1, 3, 5]
    st = SegmentTree(nums)
    assert st.sumRange(0, 2) == 9
    st.update(1, 2)
    assert st.sumRange(0, 2) == 8

    nums = [0,9,5,7,3]
    st = SegmentTree(nums)
    assert st.sumRange(2, 4) == 15
from lcpy import TreeNode, build_root


def test_pre_post():
    l = [1,2,3,4,5,6,7]
    root = build_root(l)
    # print(root.post)
    assert root.pre == [1,2,4,5,3,6,7]
    assert root.post == [4,5,2,6,7,3,1]
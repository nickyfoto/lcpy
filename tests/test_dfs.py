from lcpy.dfs import coloring_area
def test_coloring_area():

    mat = [
        [1,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,1]
    ]

    target = [[2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0],
    [3, 3, 3, 3, 3],
    [0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4]]

    assert coloring_area(mat) == target

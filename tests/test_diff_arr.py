from lcpy.df import range_to_freq

def test_diff_arr():
    requests ,n = [[1, 3], [0, 1]], 5
    assert range_to_freq(requests, n) == [1, 2, 1, 1, 0]
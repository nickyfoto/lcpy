from lcpy.it import unique_comb_of_two_lists

def test_unique_comb_of_two_lists():
    A = [1,2,3]
    B = ['a', 'b', 'c']
    res = unique_comb_of_two_lists(A, B)
    assert res == [
        [(1, 'a'), (2, 'b'), (3, 'c')], 
        [(1, 'a'), (3, 'b'), (2, 'c')], 
        [(2, 'a'), (1, 'b'), (3, 'c')], 
        [(2, 'a'), (3, 'b'), (1, 'c')], 
        [(3, 'a'), (1, 'b'), (2, 'c')], 
        [(3, 'a'), (2, 'b'), (1, 'c')]
    ]
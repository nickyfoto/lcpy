
from lcpy.dp import Knapsack
from lcpy.dp import max_sum_continious_seq
from lcpy.dp import LIS
from lcpy.dp import LCS


def test_knapsack():
	values =  [15, 10, 8, 1]
	weights = [15, 12, 10, 5]
	B = 22
	sack = Knapsack()
	# print(sack.knapsackNoRepeat(values, weights, B))
	assert 18 == sack.knapsackNoRepeat(values, weights, B)

	values = [30, 14, 16, 9]
	weights = [6 ,3, 4, 2]
	B = 10

	assert 46 == sack.knapsackNoRepeat(values, weights, B)

	values =  [15, 10, 8, 1]
	weights = [15, 12, 10, 5]
	B = 22
	assert 18 == sack.knapsackRepeat(values, weights, B)

	assert 18 == sack.ksNoRepeat_recur(B, weights, values, len(values))

def test_mscs():
	a = [5, 15, -30, 10, -5, 40, 10, -5]
	assert max_sum_continious_seq(a) == [10, -5, 40, 10]


def test_LIS():
	a = [5,7,4,-3,9,1,10,4,5,8,9,3]
	assert LIS(a) == 6

def test_LCS():
	x = "BCABCDA"
	y = "ABECBAB"
	assert LCS(x, y) == 4
	x = "B"
	y = "A"
	assert LCS(x, y) == 0
	x = "NBA"
	y = "BAN"
	assert LCS(x, y) == 2
	x = "ABBA"
	y = "BBAA"
	assert LCS(x, y) == 3
	text2 = "aceXX" 
	text1 = "abcde" 
	assert LCS(text1, text2) == 2
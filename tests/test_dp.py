
from lcpy import Knapsack



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
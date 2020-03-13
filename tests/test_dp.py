
from lcpy.dp import Knapsack
from lcpy.dp import max_sum_continious_seq
from lcpy.dp import LIS
from lcpy.dp import LCS
from lcpy.dp import LCSubStr
from lcpy.dp import chainMultiply
from lcpy.dp import Optimal_BST
from lcpy.dp import coin_change
from lcpy.dp import coin_change2
from lcpy.dp import coin_change3
from lcpy.dp import coin_change4
from lcpy.dp import copyBooks
from lcpy.dp import copyBooks2

def test_knapsack():
	values =  [15, 10, 8, 1]
	weights = [15, 12, 10, 5]
	B = 22
	sack = Knapsack()
	assert 18 == sack.knapsackNoRepeat(values, weights, B)

	values = weights = [1]
	B = 3
	sack = Knapsack()
	assert 1 == sack.knapsackNoRepeat(values, weights, B)

	values = [30, 14, 16, 9]
	weights = [6 ,3, 4, 2]
	B = 10
	assert 46 == sack.knapsackNoRepeat(values, weights, B)

	values =  [15, 10, 8, 1]
	weights = [15, 12, 10, 5]
	B = 22
	assert 18 == sack.knapsackRepeat(values, weights, B)


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

def test_chainMultiply():
	m = [50,20,1,10,100]
	n = 4
	assert chainMultiply(m, n) == 7000
	assert chainMultiply(m=[2,40,2,40,5], n=4) == 580



def test_Optimal_BST():
	assert Optimal_BST(keys=[10, 12, 20],
           			 	freq=[34, 8, 50],
            			n = 3) == 142

def test_coin_change():
	assert coin_change(15, [5, 10]) == 1
	assert coin_change(12, [5, 10]) == 0

def test_coin_change2():
	assert coin_change2(1, [1, 5, 10, 20]) == True
	assert coin_change2(2, [1, 5, 10, 20]) == False
	assert coin_change2(5, [1, 5, 10, 20]) == True
	assert coin_change2(6, [1, 5, 10, 20]) == True
	assert coin_change2(7, [1, 5, 10, 20]) == False
	assert coin_change2(15, [1, 5, 10, 20]) == True
	assert coin_change2(16, [1, 5, 10, 20]) == True
	assert coin_change2(17, [1, 5, 10, 20]) == False
	assert coin_change2(31, [1, 5, 10, 20]) == True
	assert coin_change2(40, [1, 5, 10, 20]) == False

def test_coin_change3():
	assert coin_change3(10, [1, 5, 6]) == 2

def test_coint_change4():
	assert coin_change4(5, [1,2,5]) == 4

def test_LCSubStr():
	x = 'OldSite:GeeksforGeeks.org'
	y = 'NewSite:GeeksQuiz.com'
	assert LCSubStr(x, y, len(x), len(y)) == 10

def test_copyBooks():
	pages = [3, 2, 4]
	k = 2
	assert copyBooks(pages, k) == 5
	assert copyBooks2(pages, k) == 5
sort by compare two element a, b

```py
# LC 179
def largestNumber(self, nums: List[int]) -> str:
    if not any(nums):
        return "0"
    
    return "".join(sorted(map(str, nums), key=cmp_to_key(lambda n1, n2: -1 if n1+n2>n2+n1 else 1)))
```

subset enumeration

```py
def enum_subset(n):
    """
    n = 3
    1 1
    2 2
    3 3, 2, 1
    4 4
    5 5, 4, 1
    6 6, 4, 2
    7 7, 6, 5, 4, 3, 2, 1
    """
    for state in range(1, 1 << n):
        subset = state
        while subset > 0:
            print(state, subset)
            subset = (subset - 1) & state
```

enumerate subset


```py

# dp = [0] * (1 << n)
dp = [inf] * (1 << n)

# initialize
for state in range(1 << n):
    dp[state] = sth

for state in range(1, 1 << n):
    subset = state
    while subset > 0:
        # update dp
        dp[state] = min(dp[state], sth)
        subset = (subset - 1) & state

```

compress matrix into array

each array represents from row[i:j]
inclusive
0, 0
0, 1
1, 1

```py
m = len(matrix)
n = len(matrix[0])

for i in range(m):
    temp = [0] * n
    for j in range(i, m):
        for k in range(n):
            temp[k] += matrix[j][k]
        print(temp)

matrix = [[1,0,1],[0,-2,3]]

[1, 0, 1]
[1, -2, 4]
[0, -2, 3]

```



```py
# get all possible combinations from an array be choosing number of elements from 1 to len(nums)
nums = [1,2,3,4]
N = len(nums)

for k in range(1, N+1): # takes k element for nums
    for comb in combinations(nums, k):
        print(list(comb))

# LC 1775
# LC 2035

```




Tree

```py
# 285
# if p has right, find the left most at it's right

if p.right:
    p = p.right
    while p.left:
        p = p.left
    return p

# 236 LCA
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left, right = [self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right)]
        return root if left and right else left or right


```
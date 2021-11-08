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



```py
# 124 Binary Tree Maximum Path Sum
# 2049 Count Nodes With the Highest Score
# 687 Longest Univalue Path
# 543 Diameter of Binary Tree

# Have a global variable to save the result
# the recursion itself dosen't return the result
# we use intermediate result to update the global answer



def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    """
    dfs returns number of nodes from node to its furthest leave node, including the node itself.
    we can update the result when doing dfs
    since we are counting the number of nodes and the question
    is asking about the number of edges
    we need to subtract 1 in the end
    """
    self.res = 0
    def dfs(node):
        if node:
            l = dfs(node.left)
            r = dfs(node.right)
            self.res = max(self.res, l + r + 1)
            return max(l, r) + 1
        return 0
    dfs(root)
    return self.res - 1


def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    """
    dfs returns the longest univalue a node has, including itself
    """
    self.res = 0
    def dfs(node):
        if node:
            l = dfs(node.left)
            r = dfs(node.right)
            ll = rr = 0
            if node.left and node.left.val == node.val:
                ll += l
            if node.right and node.right.val == node.val:
                rr += r
            self.res = max(self.res, ll + rr)
            return max(ll, rr) + 1
    dfs(root)
    return self.res

def maxPathSum(self, root: Optional[TreeNode]) -> int:
    self.res = -inf
    def dfs(node):
        """
        return max sum starting from this node and goes to one of its child
        """
        if node:
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            mx = node.val + l + r
            self.res = max(self.res, mx)
            return node.val + max(l, r)
        return 0    
    dfs(root)
    return self.res
```

Geometry

```py
# 223

def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = abs(ax1 - ax2) * abs(ay1 - ay2)
        b = abs(bx1 - bx2) * abs(by1 - by2)
        if ax1 >= bx2:     # if A is on the left of B
            return a + b
        if ax2 <= bx1:     # if A is on the right of B
            return a + b
        if ay1 >= by2:     # if A is above B
            return a + b
        if ay2 <= by1:     # if A is below B
            return a + b
        # otherwise find lower left and upper right using min, max
        # and subtract duplicated area
        xll = max(ax1, bx1)
        yll = max(ay1, by1)
        xur = min(ax2, bx2)
        yur = min(ay2, by2)
        return a + b - abs(yll - yur) * abs(xll - xur)
```



Sliding window

```py
# 1248 count number of nice subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-O(1)-Space


atMost(k) - atMost(k - 1)



# https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175088/C%2B%2B-Maximum-Sliding-Window-Cheatsheet-Template!


# The following problems are also solvable using the shrinkable template with the "At Most to Equal" trick

# 930. Binary Subarrays With Sum (Medium)
# 992. Subarrays with K Different Integers
# 1248. Count Number of Nice Subarrays (Medium)
# 2062. Count Vowel Substrings of a String (Easy)


```

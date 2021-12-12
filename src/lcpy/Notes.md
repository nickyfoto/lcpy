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


https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1579702/Python-Further-break-down-Sliding-Window-Template




---

1838. Frequency of the Most Frequent Element

```py
def maxFrequency(self, nums: List[int], k: int) -> int:
    nums.sort()
    sm = 0
    l = 0
    res = 0
    for r, num in enumerate(nums):
        sm += num
        while sm + k < num * (r - l + 1):
            sm -= nums[l]
            l += 1
        res = max(res, r - l + 1)
    return res
```

2009. Minimum Number of Operations to Make Array Continuous




State Machine
524.Longest-Word-in-Dictionary-through-Deleting (M+)

we need a data structure that given an index and a letter
we can know that whether from that index going right, there's the letter

Given a string `abpcplea`, resulting data structure is


```py

nxt = defaultdict(lambda: defaultdict(lambda: -1))
m = len(s)
s = '#' + s
for i in range(1, m + 1)[::-1]:
    for k in nxt[i]:
        nxt[i - 1][k] = nxt[i][k]
    nxt[i - 1][s[i]] = i

{
    8: {},
    7: {'a': 8},
    6: {'a': 8, 'e': 7},
    5: {'a': 8, 'e': 7, 'l': 6},
    4: {'a': 8, 'e': 7, 'l': 6, 'p': 5}
    3: {'a': 8, 'e': 7, 'l': 6, 'p': 5, 'c': 4},
    2: {'a': 8, 'e': 7, 'l': 6, 'p': 3, 'c': 4}
    1: {'a': 8, 'e': 7, 'l': 6, 'p': 3, 'c': 4, 'b': 2}
    0: {'a': 1, 'e': 7, 'l': 6, 'p': 3, 'c': 4, 'b': 2}
}


# after we have this, we can use
flag = 1
for ch in word:
    i = nxt[i][ch]
    if i == -1:
        flag = 0
        break
if flag:
    print('word is subsequence of abpcplea')
```



727.Minimum-Window-Subsequence (H-)
792.Number-of-Matching-Subsequences (H-)
1055.Shortest-Way-to-Form-String (M+)
2055.Plates-Between-Candles (M+)
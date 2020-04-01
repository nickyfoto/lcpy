"""
segment tree
"""

class SegmentNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.val = 0
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return "{" + f'l: {self.l}, r: {self.r}, val: {self.val}, lchild: {self.lchild}, rchild: {self.rchild}' + "}"

class SegmentTree:

    def __init__(self, nums):
        
        def createTree(nums, l, r):
            if l > r: return None
            if l == r:
                n = SegmentNode(l, r)
                n.val = nums[l]
                return n
            mid = (l + r) // 2
            root = SegmentNode(l, r)
            root.lchild = createTree(nums, l, mid)
            root.rchild = createTree(nums, mid + 1, r)
            root.val = root.lchild.val + root.rchild.val
            return root
        
        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        
        def updateVal(node, i, val):
            # print(node)
            # print('i=', i)
            if i < node.l or node.r < i:
                return
            if node.l == node.r:
                node.val = val
                return val
            updateVal(node.lchild, i, val) 
            updateVal(node.rchild, i, val) 
            node.val = node.lchild.val + node.rchild.val
            return node.val
        
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):

        def rangeSum(node, i ,j):
            if j < node.l or node.r < i:
                return 0 
            if i <= node.l and node.r <= j:
                return node.val
            return rangeSum(node.lchild, i, j) + rangeSum(node.rchild, i ,j)
        return rangeSum(self.root, i, j)


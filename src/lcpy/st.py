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
        self.nums = nums
        self.root = self._createTree(0, len(nums) - 1)
        
    def _createTree(self, l, r):
        if l > r: return None
        if l == r:
            n = SegmentNode(l, r)
            n.val = self.nums[l]
            return n
        mid = (l + r) // 2
        root = SegmentNode(l, r)
        root.lchild = self._createTree(l, mid)
        root.rchild = self._createTree(mid + 1, r)
        root.val = root.lchild.val + root.rchild.val
        return root
        
    def update(self, i, val, node=None):
        if not node: node = self.root
        if i < node.l or node.r < i: return
        if node.l == node.r:
            node.val = val
            return val
        self.update(i, val, node.lchild) 
        self.update(i, val, node.rchild) 
        node.val = node.lchild.val + node.rchild.val
        return node.val

    def query(self,i ,j, node=None):
        if not node: node = self.root
        if j < node.l or node.r < i: return 0 
        if i <= node.l and node.r <= j: return node.val
        return self.query(i, j, node.lchild) + self.query(i ,j, node.rchild)


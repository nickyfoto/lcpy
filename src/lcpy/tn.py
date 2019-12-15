"""
name tree.py is better?
"""
null = None
class TreeNode:
    """
    Helper function for TreeNode in LeetCode
    You can inspect the tree
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self._pre = []
        self._post = []
    
    def dfs(self, node):
        if node:
            self._pre.append(node.val)
            self.dfs(node.left)
            self.dfs(node.right)
            self._post.append(node.val)

    @property
    def pre(self):
        if not self._pre:
            self.dfs(self)
        return self._pre
    
    @property
    def post(self):
        if not self._pre:
            self.dfs(self)
        return self._post

    def is_leaf(self, node):
        return not node.left and not node.right

    def bfs_null(self):
        res = [self]
        q = [self]
        while q:
            node = q.pop(0)
            if self.is_leaf(node):
                continue
            res.append(node.left)
            if node.left:
                q.append(node.left)    
            res.append(node.right)
            if node.right:
                q.append(node.right)
        return str([n.val if n else n for n in res])

    def __eq__(self, other): 
        """
        equality of TreeNode instance
        use bfs to compare equality, keep aligned with print statement
        """
        l1 = self.bfs(self)
        l2 = self.bfs(other)
        # print('my=', l1, 'output=', l2)
        return l1 == l2

    def bfs(self, root):
        res = [root]
        q = [root]
        while q:
            node = q.pop(0)
            if node.left:
                res.append(node.left)
                q.append(node.left)
            if node.right:
                res.append(node.right)
                q.append(node.right)
        return [n.val for n in res]


    # def __str__(self):
    #     res = []
    #     def dfs(node):
    #         if node:
    #             res.append(node.val)
    #             dfs(node.left)
    #             dfs(node.right)
    #     dfs(self)
    #     return str(res)

    def __str__(self):
        res = [self]
        q = [self]
        while q:
            node = q.pop(0)
            if node.left:
                res.append(node.left)
                q.append(node.left)
            if node.right:
                res.append(node.right)
                q.append(node.right)
        return str([n.val for n in res])
        
    # def __str__(self):
    #     res = []
    #     def dfs(node):
    #         if node:
    #             res.append(node.val)
    #             dfs(node.left)
    #             dfs(node.right)
    #         else:
    #             res.append(None)
    #     dfs(self)
    #     return str(res)
        
def build_root(l):
    root = TreeNode(l.pop(0))
    temp = [root]
    while temp:
        # print(temp)
        node = temp.pop(0)
        if l:
            p = l.pop(0)
            if p == null:
                node.left = p
            else:
                node.left = TreeNode(p)
                temp.append(node.left)
        if l:
            p = l.pop(0)
            if p == null:
                node.right = p
            else:
                node.right = TreeNode(p)
                temp.append(node.right)
    return root


# l = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# root = build_root(l)
# print(s.findMode(root))

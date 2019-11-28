
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

    # def bfs(self):
    #     res = [self]
    #     q = [self]
    #     while q:
    #         node = q.pop(0)
    #         if node.left:
    #             res.append(node.left)
    #             q.append(node.left)
    #         if node.right:
    #             res.append(node.right)
    #             q.append(node.right)
    #     # bfs(self)
    #     return str([n.val for n in res])
    # def dfs(self, node):

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
        
def buildRoot(l):
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
# root = buildRoot(l)
# print(s.findMode(root))

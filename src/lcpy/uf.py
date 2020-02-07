"""
Union Find
"""
class UF:
    
    def __init__(self, n):
        self.arr = list(range(n))
        self.num_of_roots = n

    def find(self, p):
        while p != self.arr[p]:
            p = self.arr[p]
        return p
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.arr[rootP] = rootQ
        self.num_of_roots -= 1
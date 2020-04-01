"""
Union Find

130 
778 not understand yet
305
947
952 similar to 947 but n dimension
990
1102


class UF:
    
    @lee215
    
    def __init__(self):
        self.d = {}
    def find(self, p):
        while p != self.d[p]:
            p = self.d[p]
        return p
    def union(self, p, q):
        self.d.setdefault(p, p)
        self.d.setdefault(q, q)
        self.d[self.find(q)] = self.find(p)
"""
class UF:
    
    def __init__(self, n):
        self.arr = list(range(n))
        self.num_of_roots = n

    def find(self, p):
        while p != self.arr[p]:
            p = self.arr[p]
        return p

    def find_opt(self, p):
        """
        path compression
        """
        if p == self.arr[p]: return p
        self.arr[p] = self.find_opt(p)
        return self.arr[p]
    
    def union(self, sm, lg):
        """
        sm: small, lg: large
        """
        rs = self.find(sm)
        rl = self.find(lg)
        if rs == rl:
            return
        self.arr[rl] = rs
        self.num_of_roots -= 1
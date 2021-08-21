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

from collections import Counter

class UF:
    
    def __init__(self, n):
        """
        self.c count number of nodes connected to this root
        """
        self.arr = list(range(n))
        self.num_of_roots = n
        self.c = [1] * n

    def find(self, p):
        while p != self.arr[p]:
            p = self.arr[p]
        return p

    def find_opt(self, p):
        """
        path compression
        """
        if p != self.arr[p]:
            self.arr[p] = self.find_opt(self.arr[p])
        return self.arr[p]
    
    def union(self, u, v):
        """
        Union by larger root
        huifeng template no compare length of nodes
        x = Father[x];
        y = Father[y];
        if (x<y) Father[y] = x;
        else Father[x] = y;
        """
        ru = self.find_opt(u)
        rv = self.find_opt(v)
        if ru == rv:
            return
        if self.c[ru] > self.c[rv]:
            self.c[ru] += self.c[rv]
            self.arr[rv] = ru
        else:
            self.c[rv] += self.c[ru]
            self.arr[ru] = rv
        self.num_of_roots -= 1

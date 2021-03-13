from collections import defaultdict
from heapq import heappop, heappush
from math import inf

def dijkstra(n, edges):  
    """
    Dijkstra to find shortest distance of paths from node `n` to any other nodes
    """
    g = defaultdict(dict)
    for u, v, w in edges:
        g[u][v] = w
        g[v][u] = w
    pq = [(0, n)]
    dist = [inf] * (n + 1)
    dist[n] = 0
    while pq:
        d, u = heappop(pq)
        if d != dist[u]: continue
        for v in g[u]:
            if dist[v] > dist[u] + g[u][v]:
                dist[v] = dist[u] + g[u][v]
                heappush(pq, (dist[v], v))
    return dist


class DiGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            self.nodes[n] = None
        
    def add_edges_from(self, edges):
        self.edges = edges

    def __len__(self):
        return len(self.nodes)



def floyd_warshall(dg):
    n = len(dg)
    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))

    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in dg.edges:
        dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    # for k, v in dist.items():
    # print(k, {kk:vv for kk, vv in v.items()})
    return dist
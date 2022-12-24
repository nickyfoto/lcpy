from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List, Optional








def have_circle_dfs(g, n):

    visited = [0] * n
    def dfs(node):
        if visited[node] == 1:
            return True
        visited[node] = 2
        for nxt in g[node]:
            if visited[nxt] == 1:
                continue
            if visited[nxt] == 2:
                return False
            if dfs(nxt) == False:
                return False
        visited[node] = 1
        return True
    for i in range(n):
        if dfs(i) == False:
            return False
    return False

def have_circle_bfs(g, n):
    q = []
    cnt = 0
    indegree = Counter()
    for i in range(n):
        for j in g[i]:
            indegree[j] += 1
    q = [i for i in range(n) if indegree[i] == 0]
    cnt = len(q)
    while q:
        node = q.pop(0)
        for nxt in g[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
                cnt += 1

    return cnt == n












def dijkstra(g: dict, n: int, start: int, target: Optional[int] =None) -> List:  
    """
    :param g: directed graph
    :param n: total number of nodes in graph, 1 indexed
    :param state: start point
    :param target: target point

    Dijkstra to find shortest distance of paths from node `start` to any other nodes
    no need to use visited set
    use only one array dist to keep track of distance
    reason is, when d == dist[u]
    means dist[u] is already the shortest
    we can update its neighbor
    """
    
    pq = [(0, start)]
    dist = [inf] * (n + 1)
    dist[start] = 0
    while pq:
        d, u = heappop(pq)
        if d != dist[u]: continue
        for v in g[u]:
            if dist[v] > dist[u] + g[u][v]:
                dist[v] = dist[u] + g[u][v]
                heappush(pq, (dist[v], v))
    return dist[1:]


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

def all_simple_paths_graph(source, targets, cutoff):

    g = defaultdict(dict)
    edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
    for u, v, w in edges:
        g[u][v] = w
        g[v][u] = w
    visited = dict.fromkeys([source])
    stack = [iter(g[source])]
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.popitem()
        elif len(visited) < cutoff:
            if child in visited:
                continue
            if child in targets:
                yield list(visited) + [child]
            visited[child] = None
            if targets - set(visited.keys()):
                stack.append(iter(g[child]))
            else:
                visited.popitem()
        else:
            for target in (targets & set(children) | {child} - set(visited.keys())):
                yield list(visited) + [target]
            stack.pop()
            visited.popitem()
for path in all_simple_paths_graph(1, {5}, 4):
    print('path:', path)

__all__ = ['dijkstra', 'DiGraph', 'floyd_warshall']

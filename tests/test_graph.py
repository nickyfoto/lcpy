from lcpy import DiGraph, floyd_warshall
import networkx as nx

n = 4
edges = [
            [0,2,-2],
            [1,0,4],
            [1,2,3],
            [2,3,2],
            [3,1,-1]
        ]


def test_floyd_warshall():
    dg = DiGraph()
    dg.add_nodes_from(range(4))
    dg.add_edges_from(edges)
    
    dist = floyd_warshall(dg)
    
    dgx = nx.DiGraph()
    dgx.add_nodes_from(range(4))
    edgesx = [(a,b, {'weight': c}) for a,b,c in edges]
    dgx.add_edges_from(edgesx)
    
    distx = nx.floyd_warshall(dgx)
    assert dist == distx

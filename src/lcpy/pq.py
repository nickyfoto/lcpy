from queue import PriorityQueue

pq = PriorityQueue()

def pq_add(k, v):
    pq.add(-v, k)


def pq_get(k):
    v, k = pq.get(k)
    return k, -v
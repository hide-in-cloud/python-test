import heapq
import math


class PriorityQueue:
    def __init__(self):
        self.key = {}  # 记录结点的key值
        self.pqueue = []  # 用于建堆，存储结点集合V-S


def prim(graph, source):
    Q = PriorityQueue()
    mst = {}  # 最小生成树,集合S
    parent = {}

    # 将图中结点初始化到堆中
    for v in graph:
        if v == source:
            Q.key[v] = 0
            heapq.heappush(Q.pqueue, (0, v))
        else:
            Q.key[v] = math.inf
            heapq.heappush(Q.pqueue, (math.inf, v))
    parent[source] = None

    while Q.pqueue:
        (v_key, v) = heapq.heappop(Q.pqueue)  # 取出堆中最小元素
        del Q.key[v]  # 从集合V中删除该元素
        mst[v] = parent[v]
        for u in graph[v]:
            if u in Q.key and u not in mst:  # u还没有加入mst
                if graph[v][u] < Q.key[u]:
                    # 将堆Q.pqueue中结点u的key值更新为graph[v][u]
                    ind_key = Q.pqueue.index((Q.key[u], u))  # 找到堆中元素u的位置
                    Q.pqueue.pop(ind_key)  # 在堆中删除这个元素(边)
                    heapq.heappush(Q.pqueue, (graph[v][u], u))  # 将新key的结点u加入堆中(更小的边)
                    Q.key[u] = graph[v][u]
                    parent[u] = v
    return mst


if __name__ == '__main__':
    graph = {'s': {'a': 4, 'c': 11, 'b': 6},
             'a': {'b': 3, 's': 4},
             'c': {'b': 5, 'd': 2, 'e': 7, 's': 11},
             'b': {'a': 3, 'c': 5, 'e': 4, 's': 6},
             'e': {'c': 7, 'd': 3, 'b': 4},
             'd': {'c': 2, 'e': 3}}
    print(prim(graph, 's'))

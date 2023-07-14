class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if self.adj[u] is None:
            self.adj[u] = []
        self.adj[u].append(v)


class BFSResult:
    def __init__(self):
        self.level = {}
        self.parent = {}


def bfs(g, s):
    r = BFSResult()
    r.level = {s: 0}
    r.parent = {s: None}

    i = 1  # 当前level
    frontier = [s]  # 存放当前层的结点
    while frontier:
        next = []  # 存放下一层结点
        for u in frontier:
            for v in g.adj[u]:
                if v not in r.level:  # 若v没有被遍历过，避免v被重复遍历
                    r.parent[v] = u
                    r.level[v] = i
                    next.append(v)
        frontier = next
        i += 1
    return r


def find_shortest_path(bfs_result, v):
    """
        查询最短路径的节点
    :param bfs_result:
    :param v:
    :return:
    """
    source_vertex = [vertex for vertex, level in bfs_result.level.items() if level == 0]
    v_parent_list = []
    if v != source_vertex[0]:
        v_parent = bfs_result.parent[v]
        v_parent_list.append(v_parent)
        while v_parent != source_vertex[0] and v_parent is not None:
            v_parent = bfs_result.parent[v_parent]
            v_parent_list.append(v_parent)
    return v_parent_list


if __name__ == '__main__':
    g = Graph()
    g.adj = {'s': ['a', 'x'],
             'a': ['z', 's'],
             'd': ['f', 'c', 'x'],
             'c': ['x', 'd', 'f', 'v'],
             'v': ['f', 'c'],
             'f': ['c', 'd', 'v'],
             'x': ['s', 'd', 'c'],
             'z': []}
    bfs_result = bfs(g, 's')
    print(bfs_result.level)
    print(find_shortest_path(bfs_result, 'f'))

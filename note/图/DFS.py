class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if self.adj[u] is None:
            self.adj[u] = []
        self.adj[u].append(v)


class DFSResult:
    def __init__(self):
        self.parent = {}
        self.visited = []


def dfs_visit_r(g, v, results, parent=None):
    """
        一直遍历邻结点的邻结点
    :param g:
    :param v:当前遍历的结点
    :param results:
    :param parent:父节点
    :return:
    """
    results.parent[v] = parent
    for u in g.adj[v]:
        if u not in results.parent:        # 结点u还未遍历到
            dfs_visit_r(g, u, results, v)  # 递归


def dfs(g):
    results = DFSResult()
    for v in g.adj.keys():  # 遍历所有结点
        if v not in results.parent:        # 结点v还未遍历到
            dfs_visit_r(g, v, results)
    return results


def dfs_iterative(graph):
    """
        基于堆栈的DFS算法
    :param graph:
    :return:
    """
    results = DFSResult()
    for v in graph.adj.keys():
        if v not in results.parent:
            results.parent[v] = None
            if v not in results.visited:
                stack = [v]
                while stack:
                    u = stack.pop()
                    if u not in results.visited:
                        results.visited.append(u)
                    for n in graph.adj[u]:
                        if n not in results.visited:
                            results.parent[n] = results.visited[-1]
                            stack.extend(n)
    return results


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
    dfs_result = dfs_iterative(g)
    print('parent=', dfs_result.parent)
    print('visited=', dfs_result.visited)


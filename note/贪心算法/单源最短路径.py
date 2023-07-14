import heapq  # 最小堆


def dijkstra(graph, source):
    priority_queue = []  # 优先队列
    heapq.heappush(priority_queue, (0, source))  # 堆初始化
    visited = {}  # 存储输出结果的字典结构

    while priority_queue:
        (current_distance, current) = heapq.heappop(priority_queue)  # 从堆中获取最小距离结点
        if current not in visited:  # 将距离值添加到visited
            visited[current] = current_distance
        if current not in graph:
            continue
        for neighbour, distance in graph[current].items():  # 更新与current相邻的各结点neighbour的distance
            if neighbour in visited:
                continue
            new_distance = current_distance + distance
            heapq.heappush(priority_queue, (new_distance, neighbour))
    return visited


if __name__ == '__main__':
    graph = {'s': {'a': 4, 'c': 11, 'b': 6},
             'a': {'b': 3},
             'c': {'d': 2},
             'b': {'c': 5, 'e': 4},
             'e': {'c': 7, 'd': 3},
             'd': {}}
    print(dijkstra(graph, 's'))

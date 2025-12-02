#Use BFS, because in unweighted graphs, every edge has equal cost (assume 1).
from collections import deque, defaultdict

def shortest_path(n, edges, start, end):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected

    visited = set()
    queue = deque([(start, 0)])  # (node, distance)

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1  # no path
print(shortest_path(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], 0, 5))  # Output: 4

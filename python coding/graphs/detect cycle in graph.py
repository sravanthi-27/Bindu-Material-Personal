#🔁 For Undirected Graph:
#Do DFS.
#
#If you visit a neighbor that is already visited and it’s not the parent, there’s a cycle.
#
#🔁 For Directed Graph:
#Use DFS + recursion stack.
#
#If a node is visited and also in the recursion stack → cycle detected.
from collections import defaultdict
def has_cycle(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False
print(has_cycle(5, [[0,1],[1,2],[2,0],[3,4]]))  # Output: True (cycle exists in 0-1-2)

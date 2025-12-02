from collections import defaultdict

def count_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    count = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1  # new component
    return count
print(count_components(5, [[0, 1], [1, 2], [3, 4]]))  # Output: 2
#You are given n nodes labeled from 0 to n-1 and a list of undirected edges. Find how many connected components are in the graph.
#Explanation: One component is {0,1,2}, another is {3,4}. use dfs or bfs
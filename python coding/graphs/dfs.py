graph = {
  0: [1, 3],
  1: [0, 2],
  2: [1, 4],
  3: [0, 4],
  4: [3, 2]
}
visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        dfs(neighbor)

dfs(0)

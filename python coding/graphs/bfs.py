from collections import deque
graph = {
  0: [1, 3],
  1: [0, 2],
  2: [1, 4],
  3: [0, 4],
  4: [3, 2]
}
visited = set()
queue = deque([0])
visited.add(0)

while queue:
    node = queue.popleft()
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

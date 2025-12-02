def is_safe(node, graph, color, colors, n):
    # Check if any neighbor has the same color
    for neighbor in range(n):
        if graph[node][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True

def solve(node, graph, colors, n, k):
    if node == n:
        return True  # All nodes are colored

    for c in range(1, k+1):  # Try all colors from 1 to k
        if is_safe(node, graph, c, colors, n):
            colors[node] = c
            if solve(node + 1, graph, colors, n, k):
                return True
            colors[node] = 0  # Backtrack

    return False  # No color worked

def graph_coloring(graph, k):
    n = len(graph)
    colors = [0] * n  # 0 means no color assigned , colors = [0, 0, 0, 0]  # all uncolored


    if solve(0, graph, colors, n, k):
        return colors
    else:
        return None  # No solution
# Graph represented as adjacency matrix
# Example: 4 nodes in a line (like 0-1-2-3)
graph = [
     [0, 1, 0, 0],  # 0 is connected to 1
    [1, 0, 1, 0],  # 1 is connected to 0 and 2
    [0, 1, 0, 1],  # 2 is connected to 1 and 3
    [0, 0, 1, 0]   # 3 is connected to 2
]

k = 3  # Try with 3 colors
result = graph_coloring(graph, k)

if result:
    print("Color assignment:", result)
else:
    print("No solution possible with", k, "colors")

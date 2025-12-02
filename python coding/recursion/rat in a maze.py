def is_safe(x, y, maze, visited, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y] #This function checks if it's safe for the rat to move to position (x, y).x (row) , y(column) should be from 0 to n-1 because matrix starts from 0 to n-1

def solve_maze_util(x, y, maze, n, path, visited, result):
    # If destination is reached, add the path to result
    if x == n - 1 and y == n - 1: #If we’ve reached the bottom-right corner, we found a complete path.
        result.append(path)
        return

    # Mark the current cell as visited
    visited[x][y] = True

    # Define possible movements: Down, Left, Right, Up
    directions = [('D', x + 1, y), ('L', x, y - 1), ('R', x, y + 1), ('U', x - 1, y)]

    # Explore all possible directions
    for move, next_x, next_y in directions: #Try all 4 directions one by one.
        if is_safe(next_x, next_y, maze, visited, n):
            solve_maze_util(next_x, next_y, maze, n, path + move, visited, result)

    # Backtrack: Unmark the current cell as visited
    visited[x][y] = False

def find_paths(maze):
    n = len(maze)
    result = []

    # If the starting cell is blocked, return empty result
    if maze[0][0] == 0:
        return result

    visited = [[False for _ in range(n)] for _ in range(n)]
    solve_maze_util(0, 0, maze, n, '', visited, result)
    return sorted(result)
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

paths = find_paths(maze)
print(paths)

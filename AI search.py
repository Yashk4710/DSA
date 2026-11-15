
from collections import deque

# Maze: 0 = Path, 1 = Wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

def bfs(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([(start, [start])])
    visited = {start}

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if (0 <= nx < rows and 0 <= ny < cols
                    and maze[nx][ny] == 0
                    and (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None


# Main Program
path = bfs(maze, start, goal)

print("Maze:")
for row in maze:
    print(row)

if path:
    print("\nPath found:")
    print(path)
    print("Path length:", len(path) - 1)

    print("\nMaze with path (*):")
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print("*", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()
else:
    print("No path found!")

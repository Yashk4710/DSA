
# AI Maze Navigation using BFS

# Enter maze size
n = int(input("Enter maze size (3): "))

# Enter maze values: 0 = Free path, 1 = Wall
maze = []
for i in range(n):
    row = list(map(int, input("Enter row values: ").split()))
    maze.append(row)

# Enter starting position
sx = int(input("Enter start row: "))
sy = int(input("Enter start column: "))
start = (sx, sy)

# Enter goal position
gx = int(input("Enter goal row: "))
gy = int(input("Enter goal column: "))
goal = (gx, gy)

# Create queue and visited list
queue = [[start]]
visited = [start]

# Repeat until the queue is empty
while queue:
    path = queue.pop(0)
    x, y = path[-1]

    # Check whether the goal is reached
    if (x, y) == goal:
        print("Goal Found!")
        print("Path:", path)
        print("Path length:", len(path) - 1)
        break

    # Check four directions
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy

        # Check whether position is inside the maze
        if 0 <= nx < n and 0 <= ny < n:

            # Check for a free and unvisited position
            if maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append(path + [(nx, ny)])
                visited.append((nx, ny))

else:
    print("Goal Not Found!")

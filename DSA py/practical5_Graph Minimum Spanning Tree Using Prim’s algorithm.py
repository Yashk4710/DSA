# Prim's Algorithm

graph = [
    [0, 2, 6, 999, 999],
    [2, 0, 3, 999, 5],
    [6, 3, 0, 4, 7],
    [999, 999, 4, 0, 8],
    [999, 5, 7, 8, 0]
]

name = ["CSE", "ECE", "ME", "CE", "Admin"]

visited = [False] * 5
visited[0] = True

total = 0

print("Prim's Minimum Spanning Tree:")

for i in range(5):

    minimum = 999

    for j in range(4):
        if visited[j]:

            for k in range(5):
                if not visited[k] and graph[j][k] < minimum:
                    minimum = graph[j][k]
                    x = j
                    y = k

    print(name[x], "--", name[y], "=", minimum, "m")

    total = total + minimum
    visited[y] = True

print("Total Distance =", total, "m")


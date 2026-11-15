# Kruskal's Algorithm

graph = [
    [0, 2, 6, 999, 999],
    [2, 0, 3, 999, 5],
    [6, 3, 0, 4, 7],
    [999, 999, 4, 0, 8],
    [999, 5, 7, 8, 0]
]

name = ["CSE", "ECE", "ME", "CE", "Admin"]

# Store all edges
edges = []

for i in range(5):
    for j in range(i + 1, 5):
        if graph[i][j] != 999:
            edges.append((graph[i][j], i, j))

# Sort edges according to distance
edges.sort()

# Each vertex is initially its own group
parent = [0, 1, 2, 3, 4]

total = 0
count = 0

print("Kruskal's Minimum Spanning Tree:")

for weight, u, v in edges:

    if parent[u] != parent[v]:

        print(name[u], "--", name[v], "=", weight, "m")

        total = total + weight
        count = count + 1

        old = parent[v]
        new = parent[u]

        for i in range(5):
            if parent[i] == old:
                parent[i] = new

    if count == 4:
        break

print("Total Distance =", total, "m")

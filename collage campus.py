
# College Campus Graph using Adjacency List

graph = {
    'A': [('B', 10), ('C', 20)],
    'B': [('A', 10), ('C', 15), ('D', 25)],
    'C': [('A', 20), ('B', 15), ('D', 30), ('E', 35)],
    'D': [('B', 25), ('C', 30), ('E', 40)],
    'E': [('C', 35), ('D', 40)]
}

# Kruskal's Algorithm
def kruskal():
    edges = []

    for u in graph:
        for v, w in graph[u]:
            if u < v:
                edges.append((w, u, v))

    edges.sort()

    parent = {v: v for v in graph}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    mst = []
    total = 0

    for w, u, v in edges:
        pu = find(u)
        pv = find(v)

        if pu != pv:
            mst.append((u, v, w))
            total += w
            parent[pu] = pv

    print("\nKruskal's MST:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Total Distance =", total)


# Prim's Algorithm
def prim():
    visited = set()
    start = 'A'
    visited.add(start)

    mst = []
    total = 0

    while len(visited) < len(graph):
        min_edge = None

        for u in visited:
            for v, w in graph[u]:
                if v not in visited:
                    if min_edge is None or w < min_edge[2]:
                        min_edge = (u, v, w)

        if min_edge is None:
            print("Graph is disconnected!")
            return

        u, v, w = min_edge
        visited.add(v)
        mst.append((u, v, w))
        total += w

    print("\nPrim's MST:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Total Distance =", total)


# Main Program
print("College Campus Graph")
for u in graph:
    print(u, ":", graph[u])

kruskal()
prim()

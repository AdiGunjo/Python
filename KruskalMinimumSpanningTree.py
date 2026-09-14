class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        self.parent[rx] = ry
        return True

def kruskal(n, edges):
    edges.sort(key=lambda e: e[2])  # sort by weight
    uf = UnionFind(n)
    mst, total_cost = [], 0

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_cost += w
    return mst, total_cost

edges = [(0, 1, 4), (0, 2, 1), (1, 2, 2), (1, 3, 5), (2, 3, 8)]
mst, cost = kruskal(4, edges)
print("MST edges:", mst, "| Total cost:", cost)
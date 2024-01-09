class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_solution(self, dist, path):
        print("Vertex \tDistance \tPath")
        for node in range(self.V):
            print(f"{node}\t{dist[node]}\t\t{path[node]}")

    def min_distance(self, dist, spt_set):
        min_dist = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_dist and not spt_set[v]:
                min_dist = dist[v]
                min_index = v
        return min_index


    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        path = [''] * self.V  # Store the path from source to each vertex
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    path[v] = f'{path[u]} -> {u}' if path[u] else str(u)
        self.print_solution(dist, path)


class GraphWithPaths(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # Assuming the graph is undirected

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        path = [''] * self.V

        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v, w in self.graph[u]:
                if not spt_set[v] and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    path[v] = f'{path[u]} -> {u}' if path[u] else str(u)

        self.print_solution(dist, path)


if __name__ == "__main__":
    # Using the graph class
    g = Graph(9)
    g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    print("Using adjacency matrix: O(V^2)")
    g.dijkstra(0)

    # Using the extended graph class with paths
    g_with_paths = GraphWithPaths(9)
    g_with_paths.add_edge(0, 1, 4)
    g_with_paths.add_edge(0, 7, 8)
    g_with_paths.add_edge(1, 2, 8)
    g_with_paths.add_edge(1, 7, 11)
    g_with_paths.add_edge(2, 3, 7)
    g_with_paths.add_edge(2, 8, 2)
    g_with_paths.add_edge(2, 5, 4)
    g_with_paths.add_edge(3, 4, 9)
    g_with_paths.add_edge(3, 5, 14)
    g_with_paths.add_edge(4, 5, 10)
    g_with_paths.add_edge(5, 6, 2)
    g_with_paths.add_edge(6, 7, 1)
    g_with_paths.add_edge(6, 8, 6)
    g_with_paths.add_edge(7, 8, 7)

    print("\nUsing adjacency list: O(E + VlogV)")

    g_with_paths.dijkstra(0)

from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    # Add edge in graph
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # BFS Traversal
    def bfs(self, start):
        visited = [False] * self.V
        queue = deque()

        # Start node visited
        visited[start] = True
        queue.append(start)

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            # Visit all neighbors
            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        print()


# Main Program
V = int(input("Enter number of vertices: "))
g = Graph(V)

E = int(input("Enter number of edges: "))

print(f"Enter {E} edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting node: "))

g.bfs(start)
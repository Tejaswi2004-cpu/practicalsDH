from collections import deque
import time
from concurrent.futures import ThreadPoolExecutor


class Graph:

    def __init__(self, vertices):

        self.V = vertices

        # Adjacency list
        self.adj = [[] for _ in range(vertices)]

        # Visited array for DFS
        self.visited = [False] * vertices


    # Add edge
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


    # Parallel DFS
    def parallel_dfs(self, node):

        # Check visited
        if not self.visited[node]:

            self.visited[node] = True

            print(node, end=" ")

            # Function for visiting neighbors
            def visit(neighbor):

                self.parallel_dfs(neighbor)

            # Parallel execution
            with ThreadPoolExecutor() as executor:

                executor.map(visit, self.adj[node])


# Main Program

V = int(input("Enter number of vertices: "))

g = Graph(V)

E = int(input("Enter number of edges: "))

print(f"Enter {E} edges (u v):")

for i in range(E):

    u, v = map(int, input().split())

    g.add_edge(u, v)


start_node = int(input("Enter starting node: "))


# BFS Traversal
g.bfs(start_node)


# DFS Traversal Timing
start_time = time.time()

print("Parallel DFS Traversal:")

g.parallel_dfs(start_node)

# End time
end_time = time.time()

execution_time = (end_time - start_time) * 1000

print("\nExecution Time:", round(execution_time, 2), "ms")
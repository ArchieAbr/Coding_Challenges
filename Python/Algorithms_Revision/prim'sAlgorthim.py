# Prim's Algorthim based on the course pseudocode
# Date: 10/10/21

# A Python3 program for
# Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix
# representation of the graph

# Library for INT_MAX
import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # Print the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

    # Find the vertex with the minimum key value from the set of vertices not yet included in MST
    def minKey(self, key, mstSet):
        # Initialize minimum value
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_value and not mstSet[v]:
                min_value = key[v]
                min_index = v

        print(f"Selected vertex {min_index} with minimum key value {min_value}")
        return min_index

    # Function to construct and print MST using Prim's algorithm
    def primMST(self):
        key = [sys.maxsize] * self.V  # Key values used to pick minimum weight edge in cut
        parent = [None] * self.V  # Array to store constructed MST
        key[0] = 0  # Make key 0 so that this vertex is picked as the first vertex
        mstSet = [False] * self.V  # MST set

        parent[0] = -1  # First node is always the root of MST

        for _ in range(self.V):
            # Pick the minimum key vertex from the set of vertices not yet included in MST
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            print(f"Include vertex {u} in MST")

            # Update key value and parent index of the adjacent vertices of the picked vertex
            for v in range(self.V):
                # Only consider adjacent vertices and not yet included in MST
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    print(f"Update vertex {v}: new key = {key[v]}, parent = {parent[v]}")

        self.printMST(parent)


# Example to run Prim's algorithm
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.primMST()


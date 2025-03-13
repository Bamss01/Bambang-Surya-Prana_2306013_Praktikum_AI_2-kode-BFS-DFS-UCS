# -*- coding: utf-8 -*-
"""DFS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fhkB_PEg8pwwYG1riTl9QFGT_HmDLnzJ
"""

# DFS algorithm in Python

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end='')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Berikut adalah Penelusuran Depth First (dimulai dari node 2)")
    g.DFS(2)

# Kode ini disumbangkan oleh Neelam Yadav
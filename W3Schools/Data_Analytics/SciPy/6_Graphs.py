
# PYTHON: W3Schools - SciPy Tutorial
# Section 6: Graphs

import numpy as np
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order
from scipy.sparse import csr_matrix

# BASICS
    # We can use SciPy to represent a graph with its adjacency matrix:
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print("1.", newarr)

    # We can use connected_components() to find all connected components in the graph:
print("2.", connected_components(newarr))

    # We can use dijkstra() to find the distance between one point (set with index) and every other in the graph:
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print("3.", dijkstra(newarr, return_predecessors=True, indices=0))

    # We can use floyd_warshall() to find the distance between all pairs of points in a graph:
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print("4.", floyd_warshall(newarr, return_predecessors=True))

    # We can use bellman_ford() to find the distance between all pairs of points in a graph, however this also handles negative weights:
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print("5.", bellman_ford(newarr, return_predecessors=True, indices=0))

    # We can use depth_first_order() to perform a depth first search of the graph:
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr = csr_matrix(arr)
print("6.", depth_first_order(newarr, 1))

    # We can use breadth_first_order() to perform a breadth first search of the graph:
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr = csr_matrix(arr)
print("7.", breadth_first_order(newarr, 1))

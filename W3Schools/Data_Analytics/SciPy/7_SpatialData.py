
# PYTHON: W3Schools - SciPy Tutorial
# Section 7: Spatial Data

import numpy as np
from scipy.spatial import Delaunay, ConvexHull, KDTree
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming
import matplotlib.pyplot as plt

# BASICS
    # To subdivide a surface into triangles, we use triangulate to return an ndarray of the triangles listed by their corners:
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])
simplices = Delaunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.show()

    # ConvexHull() finds the polygon that forms a convex hull containing all points:
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])
hull = ConvexHull(points)
hull_points = hull.simplices
plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()

    # SciPy has a KDTree implementation, a datastructure optimized for nearest neighbour queries:
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print("1.", res)


# DISTANCE METRICS
    # The function euclidean() finds the euclidean distance between two points:
p1 = (1, 0)
p2 = (10, 2)
print("2.", euclidean(p1, p2))

    # The function cityblock() finds the manhattan distance between two points:
p1 = (1, 0)
p2 = (10, 2)
print("3.", cityblock(p1, p2))

    # The function cosine() finds the cosine distance between two points:
p1 = (1, 0)
p2 = (10, 2)
print("4.", euclidean(p1, p2))

    # The function hamming() finds the hamming distance between two points:
p1 = (1, 0)
p2 = (10, 2)
print("5.", hamming(p1, p2))

# SciPy Spatial Data
The scipy.spatial module in SciPy is a collection of spatial algorithms and data structures, primarily used for handling multidimensional data. 

## Triangulation
Delaunay triangulation can be performed using the Delaunay class in the scipy.spatial module. Delaunay triangulation is useful for mesh generation, computer graphics, and numerical simulations.

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

points = np.array([
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1],
    [0.5, 0.5]
])

tri = Delaunay(points)

plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.show()
```
In this, a set of points is defined in a 2D numpy array. 

## Convex Hull
The scipy.spatial module also provides the ConvexHull class for computing the convex hull of a set of points. The convex hull is the smallest convex polygon that can enclose all the given points. 

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0.5, 0.5],
    [0.25, 0.75],
    [0.75, 0.25]
])

hull = ConvexHull(points)

plt.plot(points[:, 0], points[:, 1], 'o')

for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.plot(points[hull.vertices, 0], points[hull.vertices, 1], 'ro')

plt.show()
```
In this example:

1. A set of points is defined in a 2D numpy array.
2. The ConvexHull class is used to compute the convex hull of these points.
3. The plt.plot function from Matplotlib is used to plot the points and the edges of the convex hull.
4. The vertices of the convex hull are highlighted in red.

## KDTrees
KD-Trees are a data structure useful for organizing points in a k-dimensional space, making it efficient to perform operations like nearest-neighbor search. SciPy's scipy.spatial module provides the KDTree class for this purpose.

```
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0.5, 0.5],
    [0.25, 0.75],
    [0.75, 0.25]
])

tree = KDTree(points)

query_point = [0.1, 0.1]
distance, index = tree.query(query_point)

nearest_point = points[index]

print(f"Query point: {query_point}")
print(f"Nearest point: {nearest_point}")
print(f"Distance: {distance}")

plt.plot(points[:, 0], points[:, 1], 'o')
plt.plot(query_point[0], query_point[1], 'x', label='Query Point', markersize=10)
plt.plot(nearest_point[0], nearest_point[1], 'ro', label='Nearest Neighbor')

plt.plot([query_point[0], nearest_point[0]], [query_point[1], nearest_point[1]], 'k--')

plt.legend()
plt.show()
```

## Euclidean Distance
In SciPy, you can calculate the Euclidean distance between two points using the scipy.spatial.distance module. 

```
from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)

print(res)
```

## Hamming Distance
The Hamming distance measures the number of positions at which the corresponding elements of two sequences are different. In SciPy, you can calculate the Hamming distance using the scipy.spatial.distance module.

```
from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)

print(res)
```

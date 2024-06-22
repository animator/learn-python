# SciPy Graphs
Graphs are also a type of data structure, SciPy provides a module called scipy.sparse.csgraph for working with graphs.
## Adjacency Matrix
An adjacency matrix is a way of representing a graph using a square matrix. In the matrix, the element at the i-th row and j-th column indicates whether there is an edge from vertex 
i to vertex j.
```
import numpy as np
from scipy.sparse import csr_matrix

adj_matrix = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
])


sparse_matrix = csr_matrix(adj_matrix)

print(sparse_matrix)
```
In this example:

1. The graph has 4 nodes.
2.  is an edge between node 0 and node 1, node 1 and node 2, and node 2 and node 3.
3. The csr_matrix function converts the dense adjacency matrix into a compressed sparse row (CSR) format, which is efficient for storing large, sparse matrices.
## Floyd Warshall
The Floyd-Warshall algorithm is a classic algorithm used to find the shortest paths between all pairs of nodes in a weighted graph.
```
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors=True))
```
### Output
```
(array([[0., 1., 2.],
       [1., 0., 3.],
       [2., 3., 0.]]), array([[-9999,     0,     0],
       [    1, -9999,     0],
       [    2,     0, -9999]], dtype=int32))
```
## Dijkstra
Dijkstra's algorithm is used to find the shortest path from a source node to all other nodes in a graph with non-negative edge weights.
```
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))
```
### Output
```
(array([ 0.,  1.,  2.]), array([-9999,     0,     0], dtype=int32))
```
## Bellman Ford
The Bellman-Ford algorithm is used to find the shortest path from a single source vertex to all other vertices in a weighted graph. It can handle graphs with negative weights, and it also detects negative weight cycles.
```
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))
```
### Output
```
(array([ 0., -1.,  2.]), array([-9999,     0,     0], dtype=int32))
```
## Depth First Order
Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root and explores as far as possible along each branch before backtracking.
```
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))
```
### Output
```
(array([1, 0, 3, 2], dtype=int32), array([    1, -9999,     1,     0], dtype=int32))
```
## Breadth First Order
Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root present depth level before moving on to nodes at the next depth level.
```
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))
```
### Output
```
(array([1, 0, 2, 3], dtype=int32), array([    1, -9999,     1,     1], dtype=int32))
```

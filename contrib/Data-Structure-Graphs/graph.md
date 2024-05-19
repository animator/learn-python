# Graph Data Stucture

Graph is a non-linear data structure consisting of vertices and edges. It is a powerful tool for representing and analyzing complex relationships between objects or entities.

## Components of a Graph 

1. **Vertices:** Vertices are the fundamental units of the graph. Sometimes, vertices are also known as vertex or nodes. Every node/vertex can be labeled or unlabeled.

2. **Edges:** Edges are drawn or used to connect two nodes of the graph. It can be ordered pair of nodes in a directed graph. Edges can connect any two nodes in any possible way. There are no rules. very edge can be labelled/unlabelled.

## Basic Operations on Graphs
- Insertion of Nodes/Edges in the graph
- Deletion of Nodes/Edges in the graph
- Searching on Graphs 
- Traversal of Graphs

## Types of Graph 


**1. Undirected Graph:** In an undirected graph, edges have no direction, and they represent symmetric relationships between nodes. If there is an edge between node A and node B, you can travel from A to B and from B to A.

**2. Directed Graph (Digraph):** In a directed graph, edges have a direction, indicating a one-way relationship between nodes. If there is an edge from node A to node B, you can travel from A to B but not necessarily from B to A.

**3. Weighted Graph:** In a weighted graph, edges have associated weights or costs. These weights can represent various attributes such as distance, cost, or capacity. Weighted graphs are commonly used in applications like route planning or network optimization.

**4. Cyclic Graph:** A cyclic graph contains at least one cycle, which is a path that starts and ends at the same node. In other words, you can traverse the graph and return to a previously visited node by following the edges.

**5. Acyclic Graph:** An acyclic graph, as the name suggests, does not contain any cycles. This type of graph is often used in scenarios where a cycle would be nonsensical or undesirable, such as representing dependencies between tasks or events.

**6. Tree:** A tree is a special type of acyclic graph where each node has a unique parent except for the root node, which has no parent. Trees have a hierarchical structure and are frequently used in data structures like binary trees or decision trees.

## Representation of Graphs
There are two ways to store a graph:

1. **Adjacency Matrix:**
In this method, the graph is stored in the form of the 2D matrix where rows and columns denote vertices. Each entry in the matrix represents the weight of the edge between those vertices. 

```python
def create_adjacency_matrix(graph):
    num_vertices = len(graph)

    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1

    return adj_matrix


graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

adj_matrix = create_adjacency_matrix(graph)

for row in adj_matrix:
    print(' '.join(map(str, row)))

```

2. **Adjacency List:**
In this method, the graph is represented as a collection of linked lists. There is an array of pointer which points to the edges connected to that vertex. 

```python
def create_adjacency_list(edges, num_vertices):
    adj_list = [[] for _ in range(num_vertices)]

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list

if __name__ == "__main__":
    num_vertices = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1)]

    adj_list = create_adjacency_list(edges, num_vertices)

    for i in range(num_vertices):
        print(f"{i} -> {' '.join(map(str, adj_list[i]))}")
```
`Output`
`0 -> 1 2` 
`1 -> 0 2 3` 
`2 -> 0 1 3`
`3 -> 2 1 `



# Traversal Techniques 

## Breadth First Search (BFS) 
- It is a graph traversal algorithm that explores all the vertices in a graph at the current depth before moving on to the vertices at the next depth level. 
- It starts at a specified vertex and visits all its neighbors before moving on to the next level of neighbors. 
BFS is commonly used in algorithms for pathfinding, connected components, and shortest path problems in graphs.

**Steps of BFS algorithms**


- **Step 1:** Initially queue and visited arrays are empty.
- **Step 2:** Push node 0 into queue and mark it visited.
- **Step 3:** Remove node 0 from the front of queue and visit the unvisited neighbours and push them into queue.
- **Step 4:** Remove node 1 from the front of queue and visit the unvisited neighbours and push them into queue.
- **Step 5:** Remove node 2 from the front of queue and visit the unvisited neighbours and push them into queue.
- **Step 6:** Remove node 3 from the front of queue and visit the unvisited neighbours and push them into queue. 
- **Step 7:** Remove node 4 from the front of queue and visit the unvisited neighbours and push them into queue. 

```python

from collections import deque

def bfs(adjList, startNode, visited):
    q = deque()

    visited[startNode] = True
    q.append(startNode)

    while q:
        currentNode = q.popleft()
        print(currentNode, end=" ")

        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    vertices = 5

    adjList = [[] for _ in range(vertices)]

    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 3)
    addEdge(adjList, 1, 4)
    addEdge(adjList, 2, 4)

    visited = [False] * vertices

    print("Breadth First Traversal", end=" ")
    bfs(adjList, 0, visited)

if __name__ == "__main__": #Output : Breadth First Traversal 0 1 2 3 4
    main()     

```

- **Time Complexity:** `O(V+E)`, where V is the number of nodes and E is the number of edges.
- **Auxiliary Space:** `O(V)`


## Depth-first search 

Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

**Steps of DFS algorithms**

- **Step 1:** Initially stack and visited arrays are empty.
- **Step 2:** Visit 0 and put its adjacent nodes which are not visited yet into the stack.
- **Step 3:** Now, Node 1 at the top of the stack, so visit node 1 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.
- **Step 4:** Now, Node 2 at the top of the stack, so visit node 2 and pop it from the stack and put all of its adjacent nodes which are not visited (i.e, 3, 4) in the stack.
- **Step 5:** Now, Node 4 at the top of the stack, so visit node 4 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.
- **Step 6:** Now, Node 3 at the top of the stack, so visit node 3 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.



```python
from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):
		visited.add(v)
		print(v, end=' ')

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

	print("Depth First Traversal (starting from vertex 2): ",g.DFS(2)) 

```
`Output: Depth First Traversal (starting from vertex 2): 2 0 1 3 `

- **Time complexity:** `O(V + E)`, where V is the number of vertices and E is the number of edges in the graph.
- **Auxiliary Space:** `O(V + E)`, since an extra visited array of size V is required, And stack size for iterative call to DFS function.

</br>



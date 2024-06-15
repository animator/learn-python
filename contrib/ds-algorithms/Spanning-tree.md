# Introduction to Spanning Tree

In this article, we going to cover one of the most commonly asked DSA topic which is the Spanning Tree with its definition,properties and aplications.

## What is a Spanning Tree?

A spanning tree can be defined as the subgraph of an undirected connected graph. It includes all vertices along with the least possible number of edges.
Hence a spanning tree does not have cycles.

## Properties of a Spanning Tree:

- A Spanning tree does not exist for a disconnected graph.
- For a connected graph having **N** vertices then the number of edges in the spanning tree for that graph will be **N-1**.
- We can construct a spanning tree for a complete graph by removing **E-N+1** edges, where **E** is the number of edges and **N** is the number of vertices.

# Minimum Spanning Tree(MST):

The weight of a spanning tree is determined by the sum of weight of all the edge involved in it.

``` A minimum spanning tree(MST) is defined as a spanning tree that has the minimum weight among all the possible spanning trees.```

## Properties of Minimum Spanning Tree:

- A minimum spanning tree connects all vertices in the graph, ensuring that there is a path between any pair of nodes.
- An **MST** is **acyclic** , meaning it contains no cycles. This property ensures that it remains a tree and not a graph with loops.
- An **MST** with **V** vertices (where **V** is the number of vertices in the original graph) wil have exactly **V-1** edges.
- An **MST** is optimal for minimizing the total edge weight, but it may not necessarily be unique.

## Algorithms to Find Minimum Spanning Tree of a graph :
There are several algorithms to find the minimum spanning tree some of them are listed below:
<ol type="1">
<li> <b/>Kruskal's MST Algorithm</li>
<li> <b/>Prim's MST Algorithm</li>
<li> <b/>Boruvka's Algorithm</li>
<li> <b/>Reverse-Delete Algorithm</li></ol>
 
 Let us discuss these algorithms one by one.
<ol type="1">
<li> Kruskal's Minimum Spanning Tree :

<h4>Kruskal's Minimum spanning Tree(MST) algorithm is to connect all the vertices of a graph with the minimum total edge weight avoiding cycles. This algorithm employs a greedy approach, meaning it makes locally optimal choices at each step to achieve a globally optimal solution.</h4>

### Algorithm
- First , it sorts all the edges of the graph by their weights 
- Then start the iteration of finding the spanning tree.
- At each iteration, the algorithm adds the next lowest-weight edge one by one, such that the edges picked until now does not form a cycle.

#### Implementation of kruskal's algorithm

``` python
# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree

# Class to represent a graph
class Graph:

  def __init__(self,vertices):
    self.V = vertices
    self.graph = []

  # Function to add an edge to graph
  def addEdge(self,u,v,w):
    self.graph.append([u,v,w])

  # A utility function to find set of an element i

  def find(self,parent,i):
    if(parent[i] != i):
      parent[i] = self.find(parent,parent[i])
     return parent[i]
  def union(self,parent,rank,x,y):
    if rank[x] < rank[y]:
      parent[x]=y
     elif rank[x] > rank[y]:
      parent[y] = x
     else:
      parent[y] = x
      rank[x] +=1
  # The Main function to construct MST using Kruskal's algorithm
  def KruskalMST(self):
    result =[]
    i=0
    e=0
    self.graph = sorted(self.graph,key=lambda item: item[2])
    parent = []
    rank = []
     for node in range(self.V):
      parent.append(node)
      rank.append(0)
    # Number of edges to be taken is less than to V-1
     while e < self.V-1:
      u,v,w = self.graph[i]
      i = i+1
      x = self.find(parent, u)
      y = self.find(parent, v) 
      # if including this edge does not cause cycle , then include it in result
      if x != y:
        e = e+1
        result.append([u,v,w])
        self.union(parent,rank,x,y)
        # else discard the edge
    minimumCost=0
    print("Edges in the constructed MST")
    for u,v,weight in result :
      minimumCost += weight
      print("%d -- %d == %d" % (u,v,weight))
    print("Minimum Cost Spanning Tree",minimumCost)
  # Driver code
  if __name__ == '__main__':
    g=Graph(4)
    g.addEdge(0,1,10)       
    g.addEdge(0,2,6)       
    g.addEdge(0,3,5)       
    g.addEdge(1,3,15)       
    g.addEdge(2,3,4)
    # Function call
    g.KruskalMST()
```
### Output   
```markdown
Following are the edges in the constructed MST
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
Minimum Cost Spanning Tree: 19
```
**Time Complexity :** (E`*`logE) or O(E`*`logV)
- Sorting of edges takes O(E`*`logE) time.
- After sorting, we iterate through all edges and apply the find-union operation can take at most O(logV) time.
- So overall complexity is O(E`*`logE + E`*`logV) time
- The value of E can be at most O(V<sup>2</sup>), so O(logV) and O(logE) are the same.
Therfore , the overall time complexity is O(E`*`logE) or O(E`*`logV)

**Auxiliary Space** :
O(V+E), where V is the number of vertices and E is the number of edges in the graph.

<li>Prim's Minimum Spanning Tree Algorithm:</li>
<h4>Like Kruskal's algorithm, Prim's algorithm is also a Greedy algorithm.
This algorithm always start with a single node and moves through several adjacent nodes, in order to explore all the connected edges along the way.</h4>

### How does Prim's Algorithm Work?

The working of Prim's algorithm can be described by using the following steps:

**Step 1:** Determine an arbitrary vertex as the starting vertex of the MST.

**Step 2:** Follow steps 3 to 5 till there are vertices that are not included in the MST.

**Step 3:** Find edges connecting any tree vertex with the fringe vertices.

<b>Step 4:</b> Find the minimum among these edges.

**Step 5:** Add the chosen edge to the MST if it does not form any cycle.

**Step 6:** Return the MST and exit.

#### Implementation of Prim's Algorithm

```python
# Prim's Minimum Tree algorithm
# The program is for adjacency matrix representation of the graph

import sys

class Graph():
  def __init__(self,vertices):
    self.V = vertices
    self.graph = [[0 for column in range(vertices)]
    for row in range(vertices)]
  # A utility function to print the constructed MST stored in parent[]
  def printMST(self,parent):
    print("Edge \t Weight")
    for i in range(1,self.V):
      print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
  # A utility function to find the vertex with minimum distance value, from the set of vertices not yet includedin shortest path tree
  def minKey(self, key, mstSet):
    # initialise min value 
    min = sys.maxsize
    for v in range(self.V):
      if key[v] < min and mstSet[v] == False:
        min = key[v]
        min_index = v
    return min_index
  # Function to construct and print MST for a graph
  def primMST(self):
    # key values used to pick minimumweight edge
    key = [sys.maxsize]*self.V
    parent = [None]*self.V

    # Make key 0 so that this vertex is picked as first vertex 
    key[0] = 0
    mstSet = [False]*self.V
    parent[0] = -1
    for cout in range(self.V):
      # pick the minimum distance vertex
      u = self.minKey(key,mstSet)
      # Put the minimum distance vertex in the shortest path tree
      mstSet[u] = true

    # Update dist value of the adjacency vertices of the picked vertex only if the current distance is greater than new distance and the vertex in not the shortest path tree
    for v in range(self.V):
      # graph[u][v] is non zero only for vertices of m
      # mstSet[v] is false for vertices not yet included in MST
      
      if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
        key[v] = self.graph[u][v]
        parent[v] = u
  self.printMST(parent)
# Driver's code
if __name__ == '__main__':
  g= Graph(5)
  g.graph = [[0,2,0,6,0],
             [2,0,3,8,5],
             [0,3,0,0,7],
             [6,8,0,0,9],
             [0,5,7,9,0]]    
  g.primMST()
```
### Output
```markdown
Edge        Weight
0-1           2
1-2           3
0-3           6
1-4           5
```
### Complexity Analysis of Prim's Algorithm

#### Time complexity:
O(V<sup>2</sup>) , if the input graph is represented using an adjacency list , then the time complexity of Prim's algorithm can reduced to O(E`*`logV) with the help of binary heap.
#### Auxiliary Space : O(V)

## Applications of Minimum Spanning Trees:
- **Network design:** Spanning trees can be used in network design to find the minimum number of connections required to connect all nodes.
Minimum spanning tree , in particular, can help minimize the cost of the connections by selecting the cheapest edges.

- **Image Processing:** Spanning Tree can be used in image processing to identify regions of similar intensity or color, which can be useful for segmentation and classification tasks.

- **Social Network Analysis**: Spanning Trees and Minimum spanning tree can be used in social network analysis to identify important connections and relationships among individuals or groups. 
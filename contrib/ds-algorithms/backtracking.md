# Backtracking 

Backtracking is an algorithmic technique used for solving problems incrementally by trying out partial solutions and then abandoning them if they are not suitable. It is commonly used in situations where you need to find all (or some) solutions to problems that can be broken down into a series of decisions, each of which can be explored to a certain depth.

## Pseudocode for general backtracking problem

``` 
function backtrack(candidate):
    if candidate is a solution:
        process_solution(candidate)
        return
    for next_candidate in candidates:
        if is_valid(next_candidate):
            make_move(next_candidate)
            backtrack(candidate)
            undo_move(next_candidate)
```



## Here are some common problems solved by `Backtracking`


### 1. N-Queens Problem:

N-Queens problem involves placing N queens on an N×N chessboard such that no two queens conflict with each other.Queens conflict with each other when they are in same row,same column or same diagonal. 



#### Code for N-Queens Problem:

```python
def solveNQueens(N):
    def isSafe(board, row, col):
        # Check if there's a queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check upper right diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def solve(board, row):
        if row == N:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(N):
            if isSafe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1)
                board[row][col] = '.'
    
    result = []
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve(board, 0)
    return result


N = 4
solutions = solveNQueens(N)
for solution in solutions:
    for row in solution:
        print(row)
    print()

```

**Time Complexity:**  $O(N!)$

**Space Complexity:**  $O(N^2)$


### 2. Graph Coloring Problem

Graph Coloring Problem is a classic problem in computer science and graph theory. It involves coloring the vertices of a graph in such a way that no two adjacent vertices (connected by an edge) share the same color, while using the fewest possible number of colors.

**Problem Statement:**

Given an undirected graph 𝐺=(𝑉,𝐸) , where 𝑉 is the set of vertices and 𝐸 is the set of edges, the goal is to assign a color to each vertex in such a way that no two adjacent vertices have the same color.

**Key Concepts:**

1. Vertex Coloring: Assigning colors to the vertices of a graph.
2. Adjacent Vertices: Two vertices are adjacent if they are connected by an edge in the graph.
3. Chromatic Number: The smallest number of colors needed to color a graph such that no two adjacent vertices share the same color. This number is denoted by 𝜒(𝐺)
4. Optimization Problem: Minimizing the number of colors used while satisfying the coloring constraints.

#### Code for graph-coloring problem 

```python
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: set() for v in vertices}

    def add_edge(self, u, v):
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)

    def is_safe(self, vertex, color, colors):
        for neighbor in self.adj_list[vertex]:
            if colors.get(neighbor) == color:
                return False
        return True

    def graph_coloring_backtracking(self, vertex, colors, num_colors):
        if vertex == len(self.vertices):
            return True

        for color in range(num_colors):
            if self.is_safe(self.vertices[vertex], color, colors):
                colors[self.vertices[vertex]] = color
                if self.graph_coloring_backtracking(vertex + 1, colors, num_colors):
                    return True
                colors[self.vertices[vertex]] = None

        return False

    def color_graph(self, num_colors):
        colors = {v: None for v in self.vertices}
        if self.graph_coloring_backtracking(0, colors, num_colors):
            return colors
        else:
            return None


# Example usage
if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('D', 'E'), ('D', 'F'), ('E', 'F')]
    graph = Graph(vertices)
    for edge in edges:
        graph.add_edge(*edge)

    num_colors = 3
    colors = graph.color_graph(num_colors)
    if colors:
        for vertex, color in colors.items():
            print(f"Vertex {vertex} is colored with color {color}")
    else:
        print("Graph cannot be colored with the given number of colors.")

```

**Time Complexity:**  $O(n^m)$   

**Space Complexity:**  $O(n+m)$

where n is the number of vertices and m is the number of available colors.


### Sum-of-subsets Problem

 Subset Sum Problem is a classic problem in computer science and combinatorial optimization. It involves determining whether a given set of integers contains a subset whose sum equals a specified target value.

**Problem Statement:**

Given a set of positive integers 𝑆={𝑎1,𝑎2,...,𝑎𝑛} and a target value `𝑡𝑎𝑟𝑔𝑒𝑡`, the task is to find a subset of 𝑆 whose sum equals `𝑡𝑎𝑟𝑔𝑒𝑡`.

#### Code for sum-of-subsets problem 

```python
def subset_sum_backtracking(numbers, target):
    def backtrack(start_index, current_sum, subset):
        if current_sum == target:
            result.append(subset[:])  # Append a copy of the subset
            return
        if current_sum > target:
            return
        for i in range(start_index, len(numbers)):
            subset.append(numbers[i])  # Include the current number in the subset
            backtrack(i + 1, current_sum + numbers[i], subset)  # Recursive call
            subset.pop()  # Backtrack by removing the current number from the subset
    
    result = []
    backtrack(0, 0, [])
    return result

# Example usage
if __name__ == "__main__":
    numbers = [3, 1, 5, 9, 12]
    target = 8
    subsets = subset_sum_backtracking(numbers, target)
    print("Subsets with sum equal to", target, ":")
    for subset in subsets:
        print(subset)
```
**Time Complexity:**  $O(2^n)$   

**Space Complexity:**  $O(n)$

 where 𝑛 is the number of elements in the input list.

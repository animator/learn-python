# Recursion
Recursion is a programming technique where a function calls itself in order to solve a problem.

A recursive function breaks down a problem into smaller instances of the same problem, solving each smaller instance until reaching the simplest form (base case).

**Base Case**: The condition under which the function stops calling itself to prevent infinite recursion.

## Advantages of using recursion

 - A complicated function can be split down into smaller sub-problems utilizing recursion.
 - Sequence creation is simpler through recursion than utilizing any nested iteration.
 - Makes code more readable and easier to understand for certain problems.

## Disadvantages of using recursion

 - A lot of memory and time is taken through recursive calls which makes it expensive for use.
 - Recursive functions are challenging to debug.
 - Risk of stack overflow if the base case is not properly defined or if the recursion depth is too high.


</br>
<hr>
</br>


Recursion is a powerful programming technique with a wide range of applications across different domains. Here are some key uses of recursion:

# 1. Mathematical Computations
  ## Factorials:
  Calculating the factorial of a number is a classic example of recursion.

  The factorial of a non-negative integer 𝑛 is the product of all positive integers less than or equal to 𝑛. It's commonly denoted as 𝑛!
   
  - **Base Case:** if n == 0 ensures that the recursion stops when 𝑛 is 0.
  - **Recursive Case:** return n * factorial(n-1) multiplies 𝑛 by the factorial of 𝑛−1.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

   **Time and Space Complexity**
 - **Time Complexity:** `𝑂(𝑛)` – The function makes 𝑛 recursive calls.
 - **Space Complexity:** `𝑂(𝑛)` – The function uses stack space proportional to 𝑛.



  ## Fibonacci Sequence:
   The Fibonacci sequence is a series where each number is the sum of the two preceding ones, starting from 0 and 1.

  - **Base Case:** If 𝑛 is 0 or 1, return 𝑛.
  - **Recursive Case:** Return the sum of the Fibonacci of 𝑛−1 and 𝑛−2.
   
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

  **Time and Space Complexity**
  - **Time Complexity:** `𝑂(2^𝑛)` – Exponential, due to overlapping subproblems.
  - **Space Complexity:** `𝑂(𝑛)` – The function uses stack space proportional to 𝑛.


# 2. Data Structures
  ## Tree Traversal: 
 Recursion is often used to traverse tree data structures, such as binary trees, in order to perform operations like searching, insertion, and deletion.
 Tree traversal algorithms are used to visit all the nodes in a tree data structure.

 - **Base Case:** if node ensures the function returns if the current node is None.
 - **Recursive Case:** The function calls itself for the left child, prints the current node’s value, and calls itself for the right child.
   
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)
```

  **Time and Space Complexity**
  - **Time Complexity:** `𝑂(𝑛)` – Each node is visited once.
  - **Space Complexity:** `𝑂(ℎ)` – Where ℎ is the height of the tree, due to the call stack.


# 3. Algorithms
  ## Sorting Algorithms:
 Recursive algorithms like quicksort and mergesort are efficient and widely used for sorting data.

 1. Choose a pivot element.
 2. Partition the array into elements less than and greater than the pivot.
 3. Recursively sort the subarrays.

 - **Base Case:** if len(arr) <= 1 returns the array if it has 0 or 1 element.
 - **Recursive Case:** The array is partitioned into left, middle, and right based on the pivot, and the function recursively sorts the left and right subarrays.
 
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```
**Time and Space Complexity**
- **Time Complexity:** `O(𝑛log𝑛)` on average, `𝑂(𝑛^2)` in the worst case.
- **Space Complexity:** `O(log𝑛)` due to the recursive call stack.


## Divide and Conquer:
  Many algorithms, such as binary search, utilize the divide and conquer approach, which is inherently recursive.
  Binary search efficiently finds the position of a target value within a sorted array.

  1. Calculate the middle index.
  2. Compare the target with the middle element.
  3. Recursively search in the left or right subarray based on the comparison.



  - **Base Case:** if low > high returns -1 when the subarray is empty.
  - **Recursive Case:** The function updates low or high based on the comparison and recursively searches the subarray.
    
```python
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)
```

**Time and Space Complexity**
- **Time Complexity:** `𝑂(log𝑛)`– The array is halved with each recursive call.
- **Space Complexity:** `𝑂(log𝑛)` – Due to the call stack.


# 4. Dynamic Programming
## Memoization:
  Recursion combined with memoization is used to solve problems efficiently by storing results of subproblems.

  1. Use a dictionary to store results of Fibonacci numbers.
  2. Check if the result is already computed before making a recursive call.


  - **Base Case:** if n in memo returns the stored result if already computed.
  - **Recursive Case:** memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo) computes and stores the result before returning it.
  - 
```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

**Time and Space Complexity**
- **Time Complexity:** `𝑂(𝑛)` – Each number is computed once.
- **Space Complexity:** `𝑂(𝑛)` – Due to the dictionary storing results.

# 5. Problem Solving
 ## Backtracking:
  Problems like the N-Queens puzzle and Sudoku solving use recursion with backtracking to find solutions.
  The N-Queens problem involves placing N queens on an N×N chessboard such that no two queens threaten each other.

  1. Place a queen on the board.
  2. Use backtracking to place the next queen in a valid position.
  3. If a valid placement is not found, backtrack and try a different position.


  - **Base Case:** if row == len(board) returns True when all queens are placed.
  - **Recursive Case:** The function tries placing a queen in each column and recursively attempts to place the next queen. If placing the next queen fails, it backtracks by removing the current queen.

```python
def solve_n_queens(board, row):
    if row == len(board):
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0
    return False
```

**Time and Space Complexity**
 - **Time Complexity:** `O(𝑛!)` – There are 𝑛 choices for each queen placement.
 - **Space Complexity:** `O(𝑛)` – Due to the call stack.

# 6. Graph Algorithms
  ## Depth-First Search (DFS):
   DFS is a common graph traversal technique implemented using recursion.
   DFS is a graph traversal technique that explores as far as possible along each branch before backtracking.

   1. Visit the current node and mark it as visited.
   2. Recursively visit all adjacent unvisited nodes.


   - **Base Case:** if visited is None initializes the visited set.
   - **Recursive Case:** The function adds the current node to the visited set and recursively visits unvisited neighbors.
     
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

**Time and Space Complexity**
- **Time Complexity:** 𝑂(𝑉+𝐸) – Where 𝑉 is the number of vertices and 𝐸 is the number of edges.
- **Space Complexity:** 𝑂(𝑉) – Due to the visited set and call stack.

</br>
<hr>
</br>

# Key Points about Recursion:

- **Simplicity and Elegance:**
   Recursion can simplify code for problems that naturally fit the recursive paradigm, making the solution more readable and easier to understand.
- **Base and Recursive Cases:**
  A recursive function must have a base case to terminate the recursion and a recursive case to process the problem and make the recursive call.
- **Wide Range of Applications:**
  Recursion is used in mathematical computations (e.g., factorial, Fibonacci), data structures (e.g., tree traversal), algorithms (e.g., quicksort, binary search), problem-solving techniques (e.g., backtracking), and more.
- **Efficiency Considerations:**
  While recursion can simplify problem-solving, it can also lead to high memory usage and stack overflow if not carefully managed. Techniques like memoization can optimize recursive solutions.
- **Understanding Trade-offs:**
  Recursive algorithms often have different time and space complexities compared to their iterative counterparts. Understanding these trade-offs is crucial for selecting the appropriate approach.

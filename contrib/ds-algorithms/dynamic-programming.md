# Dynamic Programming

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems and solving each subproblem only once. It stores the solutions to subproblems to avoid redundant computations, making it particularly useful for optimization problems where the solution can be obtained by combining solutions to smaller subproblems.

## Real-Life Examples of Dynamic Programming
- **Fibonacci Sequence:** Computing the nth Fibonacci number efficiently.
- **Shortest Path:** Finding the shortest path in a graph from a source to a destination.
- **String Edit Distance:** Calculating the minimum number of operations required to transform one string into another.
- **Knapsack Problem:** Maximizing the value of items in a knapsack without exceeding its weight capacity.
- **Matrix Chain Multiplication:** Finding the optimal order to multiply a sequence of matrices to minimize computational cost.
- **Optimal Binary Search Tree:** Constructing a binary search tree that minimizes search cost using given key frequencies.

# Some Common Dynamic Programming Techniques

# 1. Fibonacci Sequence

The Fibonacci sequence is a classic example used to illustrate dynamic programming. It is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

**Algorithm Overview:**
- **Base Cases:** The first two numbers in the Fibonacci sequence are defined as 0 and 1.
- **Memoization:** Store the results of previously computed Fibonacci numbers to avoid redundant computations.
- **Recurrence Relation:** Compute each Fibonacci number by adding the two preceding numbers.

## Fibonacci Sequence Code in Python (Top-Down Approach with Memoization)

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}.")
```

## Fibonacci Sequence Code in Python (Bottom-Up Approach)

```python
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}.")
```

## Complexity Analysis
- **Time Complexity**: O(n) for both approaches
- **Space Complexity**: O(n) for the top-down approach (due to memoization), O(1) for the bottom-up approach

</br>
<hr>
</br>

# 2. Longest Common Subsequence

The longest common subsequence (LCS) problem is to find the longest subsequence common to two sequences. A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.

**Algorithm Overview:**
- **Base Cases:** If one of the sequences is empty, the LCS is empty.
- **Memoization:** Store the results of previously computed LCS lengths to avoid redundant computations.
- **Recurrence Relation:** Compute the LCS length by comparing characters of the sequences and making decisions based on whether they match.

## Longest Common Subsequence Code in Python (Top-Down Approach with Memoization)

```python
def longest_common_subsequence(X, Y, m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        memo[(m, n)] = 1 + longest_common_subsequence(X, Y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(longest_common_subsequence(X, Y, m, n - 1, memo),
                            longest_common_subsequence(X, Y, m - 1, n, memo))
    return memo[(m, n)]

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of Longest Common Subsequence:", longest_common_subsequence(X, Y, len(X), len(Y)))
```

## Complexity Analysis
- **Time Complexity**: O(m * n) for the top-down approach, where m and n are the lengths of the input sequences
- **Space Complexity**: O(m * n) for the memoization table

</br>
<hr>
</br>

# 3. 0-1 Knapsack Problem

The 0-1 knapsack problem is a classic optimization problem where the goal is to maximize the total value of items selected while keeping the total weight within a specified limit.

**Algorithm Overview:**
- **Base Cases:** If the capacity of the knapsack is 0 or there are no items to select, the total value is 0.
- **Memoization:** Store the results of previously computed subproblems to avoid redundant computations.
- **Recurrence Relation:** Compute the maximum value by considering whether to include the current item or not.

## 0-1 Knapsack Problem Code in Python (Top-Down Approach with Memoization)

```python
def knapsack(weights, values, capacity, n, memo={}):
    if (capacity, n) in memo:
        return memo[(capacity, n)]
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        memo[(capacity, n)] = knapsack(weights, values, capacity, n - 1, memo)
    else:
        memo[(capacity, n)] = max(values[n - 1] + knapsack(weights, values, capacity - weights[n - 1], n - 1, memo),
                                  knapsack(weights, values, capacity, n - 1, memo))
    return memo[(capacity, n)]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
n = len(weights)
print("Maximum value that can be obtained:", knapsack(weights, values, capacity, n))

```

## Complexity Analysis
- **Time Complexity**: O(n * W) for the top-down approach, where n is the number of items and W is the capacity of the knapsack
- **Space Complexity**: O(n * W) for the memoization table

</br>
<hr>
</br>

# 4. String Edit Distance 

The String Edit Distance algorithm calculates the minimum number of operations (insertions, deletions, or substitutions) required to convert one string into another.

**Algorithm Overview:**
- **Base Cases:** If one string is empty, the edit distance is the length of the other string.
- **Memoization:** Store the results of previously computed edit distances to avoid redundant computations.
- **Recurrence Relation:** Compute the edit distance by considering insertion, deletion, and substitution operations.
  
## String Edit Distance Code in Python (Top-Down Approach with Memoization)
```python
def edit_distance(str1, str2, memo={}):
    m, n = len(str1), len(str2)
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m - 1] == str2[n - 1]:
        memo[(m, n)] = edit_distance(str1[:m-1], str2[:n-1], memo)
    else:
        memo[(m, n)] = 1 + min(edit_distance(str1, str2[:n-1], memo),     # Insert
                               edit_distance(str1[:m-1], str2, memo),     # Remove
                               edit_distance(str1[:m-1], str2[:n-1], memo)) # Replace
    return memo[(m, n)]

str1 = "sunday"
str2 = "saturday"
print(f"Edit Distance between '{str1}' and '{str2}' is {edit_distance(str1, str2)}.")
# Output: Edit Distance between 'sunday' and 'saturday' is 3.
```
## String Edit Distance Code in Python (Bottom-Up Approach)
```python
def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

str1 = "sunday"
str2 = "saturday"
print(f"Edit Distance between '{str1}' and '{str2}' is {edit_distance(str1, str2)}.")
# Output: Edit Distance between 'sunday' and 'saturday' is 3.
```
## **Complexity Analysis:**
- **Time Complexity:** O(m * n) where m and n are the lengths of string 1 and string 2 respectively
- **Space Complexity:** O(m * n) for both top-down and bottom-up approaches

</br>
<hr>
</br>

# 5. Matrix Chain Multiplication

The Matrix Chain Multiplication finds the optimal way to multiply a sequence of matrices to minimize the number of scalar multiplications.

**Algorithm Overview:**
- **Base Cases:** The cost of multiplying one matrix is zero.
- **Memoization:** Store the results of previously computed matrix chain orders to avoid redundant computations.
- **Recurrence Relation:** Compute the optimal cost by splitting the product at different points and choosing the minimum cost.
  
## Matrix Chain Multiplication Code in Python (Top-Down Approach with Memoization)
```python
def matrix_chain_order(p, memo={}):
    n = len(p) - 1
    def compute_cost(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == j:
            return 0
        memo[(i, j)] = float('inf')
        for k in range(i, j):
            q = compute_cost(i, k) + compute_cost(k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < memo[(i, j)]:
                memo[(i, j)] = q
        return memo[(i, j)]
    return compute_cost(1, n)

p = [1, 2, 3, 4]
print(f"Minimum number of multiplications is {matrix_chain_order(p)}.")
# Output: Minimum number of multiplications is 18.
```
## Matrix Chain Multiplication Code in Python (Bottom-Up Approach)
```python
def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][n - 1]

p = [1, 2, 3, 4]
print(f"Minimum number of multiplications is {matrix_chain_order(p)}.")
# Output: Minimum number of multiplications is 18.
```
## **Complexity Analysis:**
- **Time Complexity:** O(n^3) where n is the number of matrices in the chain. For an `array p` of dimensions representing the matrices such that the `i-th matrix` has dimensions `p[i-1] x p[i]`, n is `len(p) - 1`
- **Space Complexity:**  O(n^2) for both top-down and bottom-up approaches

</br>
<hr>
</br>

# 6. Optimal Binary Search Tree

The Matrix Chain Multiplication finds the optimal way to multiply a sequence of matrices to minimize the number of scalar multiplications.

**Algorithm Overview:**
- **Base Cases:** The cost of a single key is its frequency.
- **Memoization:** Store the results of previously computed subproblems to avoid redundant computations.
- **Recurrence Relation:** Compute the optimal cost by trying each key as the root and choosing the minimum cost.
  
## Optimal Binary Search Tree Code in Python (Top-Down Approach with Memoization)
```python
def optimal_bst(keys, freq, memo={}):
    n = len(keys)
    def compute_cost(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return 0
        if i == j:
            return freq[i]
        memo[(i, j)] = float('inf')
        total_freq = sum(freq[i:j+1])
        for r in range(i, j + 1):
            cost = (compute_cost(i, r - 1) + 
                    compute_cost(r + 1, j) + 
                    total_freq)
            if cost < memo[(i, j)]:
                memo[(i, j)] = cost
        return memo[(i, j)]
    return compute_cost(0, n - 1)

keys = [10, 12, 20]
freq = [34, 8, 50]
print(f"Cost of Optimal BST is {optimal_bst(keys, freq)}.")
# Output: Cost of Optimal BST is 142.
```
## Optimal Binary Search Tree Code in Python (Bottom-Up Approach)
```python
def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')
            total_freq = sum(freq[i:j+1])
            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + \
                    (cost[r + 1][j] if r < j else 0) + \
                    total_freq
                if c < cost[i][j]:
                    cost[i][j] = c

    return cost[0][n - 1]

keys = [10, 12, 20]
freq = [34, 8, 50]
print(f"Cost of Optimal BST is {optimal_bst(keys, freq)}.")
# Output: Cost of Optimal BST is 142.
```
## **Complexity Analysis:**
- **Time Complexity:** O(n^3) where n is the number of keys in the binary search tree.
- **Space Complexity:** O(n^2) for both top-down and bottom-up approaches

</br>
<hr>
</br>

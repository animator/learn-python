# Dynamic Programming

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems and solving each subproblem only once. It stores the solutions to subproblems to avoid redundant computations, making it particularly useful for optimization problems where the solution can be obtained by combining solutions to smaller subproblems.

## Real-Life Examples of Dynamic Programming
- **Fibonacci Sequence:** Computing the nth Fibonacci number efficiently.
- **Shortest Path:** Finding the shortest path in a graph from a source to a destination.
- **String Edit Distance:** Calculating the minimum number of operations required to transform one string into another.
- **Knapsack Problem:** Maximizing the value of items in a knapsack without exceeding its weight capacity.

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
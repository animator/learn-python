# Introduction to Recursions

When a function calls itself to solve smaller instances of the same problem until a specified condition is fulfilled is called recursion. It is used for tasks that can be divided into smaller sub-tasks.

# How Recursion Works

To solve a problem using recursion we must define:
- Base condition :- The condition under which recursion ends.
- Recursive case :- The part of function which calls itself to solve a smaller instance of problem.

Steps of Recursion

When a recursive function is called, the following sequence of events occurs:
- Function Call: The function is invoked with a specific argument.
- Base Condition Check: The function checks if the argument satisfies the base case.
- Recursive Call: If the base case is not met, the function performs some operations and makes a recursive call with a modified argument.
- Stack Management: Each recursive call is placed on the call stack. The stack keeps track of each function call, its argument, and the point to return to once the call completes.
- Unwinding the Stack: When the base case is eventually met, the function returns a value, and the stack starts unwinding, returning values to previous function calls until the initial call is resolved.

# What is Stack Overflow in Recursion

Stack overflow is an error that occurs when the call stack memory limit is exceeded. During execution of recursion calls they are simultaneously stored in a recursion stack waiting for the recursive function to be completed. Without a base case, the function would call itself indefinitely, leading to a stack overflow.

# Example

- Factorial of a Number

   The factorial of i natural numbers is nth integer multiplied by factorial of (i-1) numbers. The base case is if i=0 we return 1 as factorial of 0 is 1.
   
```python
def factorial(i):
  #base case
  if i==0 :
    return 1
  #recursive case
  else :
    return i * factorial(i-1)
i = 6
print("Factorial of i is :", factorial(i))  # Output- Factorial of i is :720 
```
# What is Backtracking

Backtracking is a recursive algorithmic technique used to solve problems by exploring all possible solutions and discarding those that do not meet the problem's constraints. It is particularly useful for problems involving combinations, permutations, and finding paths in a grid.

# How Backtracking Works

- Incremental Solution Building: Solutions are built one step at a time.
- Feasibility Check: At each step, a check is made to see if the current partial solution is valid.
- Backtracking: If a partial solution is found to be invalid, the algorithm backtracks by removing the last added part of the solution and trying the next possibility.
- Exploration of All Possibilities: The process continues recursively, exploring all possible paths, until a solution is found or all possibilities are exhausted.

# Example

- Word Search

   Given a 2D grid of characters and a word, determine if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Algorithm for Solving the Word Search Problem with Backtracking:
- Start at each cell: Attempt to find the word starting from each cell.
- Check all Directions: From each cell, try all four possible directions (up, down, left, right).
- Mark Visited Cells: Use a temporary marker to indicate cells that are part of the current path to avoid revisiting.
- Backtrack: If a path does not lead to a solution, backtrack by unmarking the visited cell and trying the next possibility.
    
```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, suffix):
        if not suffix:
            return True
        
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != suffix[0]:
            return False

        # Mark the cell as visited by replacing its character with a placeholder
        ret = False
        board[r][c], temp = '#', board[r][c]

        # Explore the four possible directions
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = backtrack(r + row_offset, c + col_offset, suffix[1:])
            if ret:
                break

        # Restore the cell's original value
        board[r][c] = temp
        return ret

    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, word):
                return True

    return False

# Test case
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCES"
print(exist(board, word))  # Output: True
```


   

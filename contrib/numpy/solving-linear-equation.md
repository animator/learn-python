# Solving Linear Systems: 2 variables

- Using `NumPy` linear algebra package to find the solutions of the system of linear equations
- We will be finding the solution for the system of linear equations using elimination method
- We will evaluate the determinant of the matrix and examine the relationship between matrix singularity and number of solutions of the linear system

# Table of Contents

- [ 1 - Representing and Solving System of Linear Equations using Matrices](#1)
  - [ 1.1 - System of Linear Equations](#1.1)
  - [ 1.2 - Solving Systems of Linear Equations using Matrices](#1.2)
  - [ 1.3 - Evaluating Determinant of a Matrix](#1.3)
- [ 2 - Solving System of Linear Equations using Elimination Method](#2)
  - [ 2.1 - Elimination Method](#2.1)
  - [ 2.2 - Preparation for the Implementation of Elimination Method in the Code](#2.2)
  - [ 2.3 - Implementation of Elimination Method](#2.3)
  - [ 2.4 - Graphical Representation of the Solution](#2.4)
- [ 3 - System of Linear Equations with No Solutions](#3)
- [ 4 - System of Linear Equations with Infinite Number of Solutions](#4)

## Packages

Load the `NumPy` package to access its functions.

import numpy as np

## 1 - Representing and Solving System of Linear Equations using Matrices

### 1.1 - System of Linear Equations

A **system of linear equations** (or **linear system**) is a collection of one or more linear equations involving the same variables. For example:


$$\begin{cases} 
-x_1+3x_2=7, \\ 3x_1+2x_2=1, \end{cases}\tag{1}$$

is a system of two equations with two unknown variables $x_1$, $x_2$. **To solve** a system of linear equations means to find such values 
of the variables $x_1$, $x_2$, that all of its equations are simultaneously satisfied.

A linear system is **inconsistent** if it has no solution, and otherwise it is said to be **consistent**. Consistent system can have one 
or infinite number of solutions.


### 1.2 - Solving Systems of Linear Equations using Matrices

Linear systems with two equations are easy to solve manually, but preparing for more complicated cases, we will investigate some solution 
techniques. 

`NumPy` linear algebra package provides quick and reliable way to solve the system of linear equations using function `np.linalg.solve(A, b)`. 
Here $A$ is a matrix, each row of which represents one equation in the system and each column corresponds to the variable $x_1$, $x_2$. 
And $b$ is a 1-D array of the free (right side) coefficients. More information about the `np.linalg.solve()` function can be found in [documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html).

Given the system of linear equations $(1)$, you can set matrix $A$ and 1-D array $b$ as:

A = np.array([
        [-1, 3],
        [3, 2]
    ], dtype=np.dtype(float))

b = np.array([7, 1], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

print(f"Shape of A: {A.shape}")
print(f"Shape of b: {b.shape}")

# print(f"Shape of A: {np.shape(A)}")
# print(f"Shape of A: {np.shape(b)}")


Now simply use `np.linalg.solve(A, b)` function to find the solution of the system $(1)$. The result will be saved in the 1-D array $x$. 
The elements will correspond to the values of $x_1$ and $x_2$:


x = np.linalg.solve(A, b)

print(f"Solution: {x}")

d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")

A_system = np.hstack((A, b.reshape((2, 1))))

print(A_system)


print(A_system[1])

# Function .copy() is used to keep the original matrix without any changes.
A_system_res = A_system.copy()

A_system_res[1] = 3 * A_system_res[0] + A_system_res[1]

print(A_system_res)


A_system_res[1] = 1/11 * A_system_res[1]

print(A_system_res)

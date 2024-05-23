## Pattern 
**1. Semi-Pyramid**
``` 

1 
1 2 
1 2 3 
1 2 3 4
```

**Code**
``` python
n = 4
for n in range(1, n + 1):
    for m in range(1, n + 1):
        print(m, end=’ ‘)
    print(“”)
```

**2. Printing Numbers Using Inverted Pyramid**
```
1 1 1 1 
2 2 2 
3 3 
4
```

**Code**
```python

n = 4
m = 0
for k in range(n, 0, -1):
    m += 1
    for n in range(1, k + 1):
        print(m, end=' ')
    print('\r')
```


**3. Inverted Pyramid With Same Digit**
```
4 4 4 4 
4 4 4 
4 4 
4 
```
**Code**
```python

n = 4
digit = n
for k in range(n, 0, -1):
    for m in range(0, k):
        print(digit, end=' ')
    print("\r")
```

**4. Numbers in a Reverse Semi-pyramid**
```
1 
2 1 
3 2 1 
4 3 2 1
```
**Code**
```python
n = 5
for r in range(1, n):
    for m in range(r, 0, -1):
        print(m, end=' ')
    print(" ")
```


**5. Printing a Horizontal Table Using a Pyramid**
```
0 
0 1 
0 2 4 
0 3 6 9 
0 4 8 12 16 
0 5 10 15 20 25
```

**Code**
```python

n = 6
for k in range(0, n):
    for m in range(0, k + 1):
        print(k * m, end=' ')
    print()
```

**6. star pyramid**
```
    *
   ***
  *****
 *******
*********
```

**Code**
```python

def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
```

**7. alphabet pyramid**
```
      A 
     A B 
    A B C 
   A B C D 
  A B C D E 
```
  **Code**
```python

n = 5
alph = 65
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()
```

**8. Inverted half hollow pyramid**
```
*****
*   *
*  *
* *
**
```

**Code**
```python

def print_hollow_inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(i):
            if j == 0 or j == i - 1 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()
num_rows = 5
print_hollow_inverted_half_pyramid(num_rows)
```

**9. Inverted star pyramid**
```
* * * * *
* * * *
* * *
* *
*
```
**Code**
```v

def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")
n = 5
inverted_half_pyramid(n)
```


**10. Hollow pyramid**
```
      *    
   *     *   
  *       *  
 *          * 
*********
```
**Code**
```python

def hollow_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if j <= n - i or j >= n + i:
                print(" ", end="")
            else:
                print("*", end="")
        print()
rows = 5
hollow_pyramid(rows)
```


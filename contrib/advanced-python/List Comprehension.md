<h1>List Comprehension</h1><br>   

<h2>Topics Covered:</h2>
-What is a list comprehension<br>
-Advantages of using list comprehension<br>
-Types of list comprehension with examples<br><br>

<h3>1.What is a list comprehension</h3><br>
It is used to create a new list by applying an operation on each item in an existing list.<br>
List comprehension in python is widely used for performing various tasks.<br><br>
<h3>2.Advantages of using list comprehension</h3>
<h4>-Consiseness:</h4>It reduces number of lines of code compared to traditional loops<br>
<h4>-Readability:</h4>A clear and declarative syntax is followed in creation of lists<br>
<h4>-Versatility:</h4>It supports a wide range of expressions,operations,function calls,conditional statements.<br>
<br><br>
<h3>3.Types of list comprehension with examples</h3>

<h4>1.Basic List Comprehension:</h4>
-It is used to create a new list by applying a single expression to each item in an existing list.<br>
Syntax: [expression for item in iterable]<br>

```python
squares = [x**2 for x in range(5)]
print(squares)
```
Output:
```
[0, 1, 4, 9, 16]
```
<br>
<h4>2.Conditional List Comprehension:</h4>
-It includes conditional statements to filter elements from the original list based on a specified condition.<br>
Syntax: [expression for item in iterable if condition]<br>

```python
five_numbers = [x for x in range(10) if x<5]
```
Output:
```
[0, 1, 2, 3, 4]
```
<br>
<h4>3.Nested List Comprehension:</h4>
-It involves using multiple iterations and conditions within nested comprehensions to create lists of lists.<br>
Syntax: [[expression for item in iterable] for item in iterable]<br>

```python
matrix = [[i*j for j in range(3)] for i in range(3)]
```
Output:
```
[[0, 0, 0],
 [0, 1, 2],
 [0, 2, 4]]
```
<br>
<h4>4.Multiple Iterables in List Comprehension:</h4>
-It uses multiple iterables within a single list comprehension, iterating over them in parallel to create a new list.<br>
Syntax: [expression for item1 in iterable1 for item2 in iterable2]<br>

```python
pairs = [(x, y) for x in range(3) for y in range(3)]
```
Output:
```
[(0, 0), (0, 1), (0, 2),  (1, 0), (1, 1), (1, 2),  (2, 0), (2, 1), (2, 2)]
```
<br>
<h4>5.Using functions in list comprehensions</h4>
-It applies functions or methods to elements of the original iterable within list comprehensions for transformation or filtering.<br>
Syntax: [function(item) for item in iterable]<br>

```python
words = ['hello', 'world', 'python']
capitalized_words = [word.upper() for word in words]
```
Output:
```
['HELLO', 'WORLD', 'PYTHON']
```


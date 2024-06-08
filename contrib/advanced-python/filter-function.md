# Filter Function

## Definition
The filter function is a built-in Python function used for constructing an iterator from elements of an iterable for which a function returns true.

**Syntax**:
 ```python
filter(function, iterable)
```
**Parameters**:<br>
*function*: A function that tests if each element of an iterable returns True or False.<br>
*iterable*: An iterable like sets, lists, tuples, etc., whose elements are to be filtered.<br>
*Returns* : An iterator that is already filtered.

## Basic Usage
**Example 1: Filtering a List of Numbers**:
```python
# Define a function that returns True for even numbers
def is_even(n):
    return n % 2 == 0

numbers = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]
```

**Example 2: Filtering with a Lambda Function**:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

print(list(odd_numbers))  # Output: [1, 3, 5, 7, 9]
```

**Example 3: Filtering Strings**:
```python
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape" , "python"]
long_words = filter(lambda word: len(word) > 5, words)

print(list(long_words))  # Output: ['banana', 'cherry', 'elderberry', 'python']
```

## Advanced Usage
**Example 4: Filtering Objects with Attributes**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person("Alice", 30),
    Person("Bob", 15),
    Person("Charlie", 25),
    Person("David", 35)
]

adults = filter(lambda person: person.age >= 18, people)
adult_names = map(lambda person: person.name, adults)

print(list(adult_names))  # Output: ['Alice', 'Charlie', 'David']
```

**Example 5: Using None as the Function**:
```python
numbers = [0, 1, 2, 3, 0, 4, 0, 5]
non_zero_numbers = filter(None, numbers)

print(list(non_zero_numbers))  # Output: [1, 2, 3, 4, 5]
```
**NOTE**: When None is passed as the function, filter removes all items that are false.

## Time Complexity:
- The time complexity of filter() depends on two factors:
    1. The time complexity of the filtering function (the one you provide as an argument).
    2. The size of the iterable being filtered.
- If the filtering function has a constant time complexity (e.g., O(1)), the overall time complexity of filter() is   linear (O(n)), where ‘n’ is the number of elements in the iterable.

## Space Complexity:
- The space complexity of filter() is also influenced by the filtering function and the size of the iterable.
- Since filter() returns an iterator, it doesn’t create a new list in memory. Instead, it generates filtered elements on-the-fly as you iterate over it. Therefore, the space complexity is O(1).

## Conclusion:
Python’s filter() allows you to perform filtering operations on iterables. This kind of operation consists of applying a Boolean function to the items in an iterable and keeping only those values for which the function returns a true result. In general, you can use filter() to process existing iterables and produce new iterables containing the values that you currently need.Both versions of Python support filter(), but Python 3’s approach is more memory-efficient due to the use of iterators.
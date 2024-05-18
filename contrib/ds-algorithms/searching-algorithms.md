# Searching Algorithms

In computer science, searching algorithms are methods for finding elements within a data structure. They aim to determine whether a particular element is present in the given data structure and, if so, locate its position or perform some other action.

## Real Life Example of Searching
- Finding a book in a library by its title
- Searching for a specific item in a grocery store
- Looking for a contact in a phonebook, etc.

# Some Common Searching Techniques

# 1. Linear Search

Linear search, also known as sequential search, is a simple searching algorithm that checks every element in the list sequentially until the desired element is found or the end of the list is reached. It is easy to implement and suitable for small lists, but inefficient for large datasets.

**Algorithm Overview:**
- **Starting from the Beginning:** The algorithm starts searching from the beginning of the list.
- **Sequential Comparison:** It compares each element in the list with the target element.
- **Termination Conditions:** The search terminates when either the target element is found or the end of the list is reached.

## Linear Search Code in Python

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if target is found
    return -1  # Return -1 if target is not found

arr = [5, 3, 8, 1, 2]
target = 8
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
```

## Complexity Analysis

- **Time Complexity**: `O(n)` where n is the number of elements in the list. In the worst-case scenario, the algorithm may need to examine every element in the list.
- **Space Complexity**: `O(1)` as the algorithm requires only a constant amount of additional space regardless of the input size.

</br>
<hr>
</br>

# 2. Binary Search

Binary search is a fast and efficient searching algorithm used on sorted lists or arrays. It works by repeatedly dividing the search interval in half until the target element is found or the interval becomes empty. Binary search is significantly faster than linear search but requires the input to be sorted beforehand.

**Algorithm Overview:**
- **Initial State:** Binary search requires a sorted list as input.
- **Divide and Conquer:** It repeatedly divides the search interval in half and narrows down the possible locations of the target element.
- **Comparison with the Midpoint:** It compares the target element with the middle element of the current interval and decides whether to continue searching in the left or right half.
- **Termination Conditions:** The search terminates when the target element is found or the interval becomes empty.

## Binary Search Code in Python (Iterative)

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if target is not found

arr = [1, 2, 3, 5, 8]
target = 3
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
```

## Binary Search Code in Python (Recursive)

```python
def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1  # Return -1 if target is not found

arr = [1, 2, 3, 5, 8]
target = 3
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
```

## Complexity Analysis

- **Time Complexity**: `O(log n)` where n is the number of elements in the list. Binary search halves the search interval in each step, resulting in a logarithmic time complexity.
- **Space Complexity**: `O(1)` for the iterative version and `O(log n)` for the recursive version due to function call stack space.

</br>
<hr>
</br>

# 3. Interpolation Search

Interpolation search is an improvement over binary search for uniformly distributed datasets. It calculates the probable position of the target element based on the distribution of values in the dataset. Interpolation search can be more efficient than binary search in certain scenarios, especially when the data is evenly distributed.

**Algorithm Overview:**
- **Initial State:** Interpolation search requires a sorted list as input.
- **Calculation of Probable Position:** It uses interpolation formulae to calculate the probable position of the target element based on the values of endpoints and their indices.
- **Comparison with the Probable Position:** It compares the target element with the value at the probable position and decides whether to continue searching in the left or right half.
- **Termination Conditions:** The search terminates when the target element is found or the interval becomes empty.

## Interpolation Search Code in Python

```python
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

arr = [1, 2, 3, 5, 8]
target = 3
result = interpolation_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
```

## Complexity Analysis

- **Time Complexity**: Average-case time complexity is `O(log log n)` when elements are uniformly distributed. In the worst case, it can degrade to `O(n)` when the dataset is not uniformly distributed.
- **Space Complexity**: `O(1)` as the algorithm requires only a constant amount of additional


# Searching Algorithms

## Real Life Example of Searching
- Finding a book in a library
- Searching for a specific word in a dictionary
- Looking for a contact in a phone book, etc.

# Some common searching techniques

# 1. Linear Search

Linear search, also known as sequential search, is a straightforward searching algorithm that sequentially checks each element of the list until it finds the target element or reaches the end of the list.

**Algorithm Overview:**
- **Sequential Scanning:** The algorithm starts from the beginning of the list and compares each element with the target element.
- **Termination:** If the target element is found, the search terminates, and the index of the target element is returned. If the end of the list is reached without finding the target element, the search terminates unsuccessfully.

## Linear Search Code in Python

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target not found

arr = [5, 3, 8, 1, 2]
target = 8
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
```

## Complexity Analysis
- **Time Complexity:** `O(n)` where n is the number of elements in the list. In the worst-case scenario, the algorithm may need to scan through all elements.
- **Space Complexity:** `O(1)`. Linear search requires only a constant amount of additional space for storing loop variables.

</br>
<hr>
</br>

# 2. Binary Search

Binary search is an efficient searching algorithm that works on sorted lists by repeatedly dividing the search interval in half. It compares the target value with the middle element of the list and decides whether to continue searching in the left or right half based on the comparison.

**Algorithm Overview:**
- **Divide and Conquer:** Binary search divides the search interval in half at each step, reducing the search space by half in each iteration.
- **Comparison with the Middle Element:** It compares the target value with the middle element of the list.
- **Refining the Search Interval:** Depending on the comparison result, the algorithm either continues the search in the left half (if the target is smaller) or the right half (if the target is larger) of the list.
- **Termination:** The search terminates when the target element is found, or the search interval becomes empty.

## Binary Search Code in Python

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

arr = [1, 2, 3, 5, 8]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
```

## Complexity Analysis
- **Time Complexity:** `O(log n)` where n is the number of elements in the list. Binary search repeatedly divides the search interval in half, leading to logarithmic time complexity.
- **Space Complexity:** `O(1)`. Binary search requires only a constant amount of additional space for storing variables.

</br>
<hr>
</br>

# 3. Interpolation Search

Interpolation search is an improved version of binary search, particularly useful for uniformly distributed sorted arrays. It calculates the probable position of the target element based on its value and the range of elements in the array.

**Algorithm Overview:**
- **Calculation of Probable Position:** Interpolation search calculates the probable position of the target element using a formula that takes into account the range of values in the array.
- **Comparison with Probable Position:** It compares the target value with the element at the calculated position.
- **Refining the Search Interval:** Based on the comparison result, the algorithm adjusts the search interval to continue the search in the appropriate direction.
- **Termination:** The search terminates when the target element is found, or the search interval becomes empty.

## Interpolation Search Code in Python

```python
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Calculate the probable position
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # Target not found

arr = [1, 2, 3, 5, 8]
target = 5
result = interpolation_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
```

## Complexity Analysis
- **Time Complexity:** `O(log log n)` on average, where n is the number of elements in the list. Interpolation search can be significantly faster than binary search for large datasets with uniformly distributed elements.
- **Worst Case Time Complexity:** `O(n)` in scenarios where the elements are not uniformly distributed, or when the target element is located at one end of the array.
- **Space Complexity:** `O(1)`. Interpolation search requires only a constant amount of additional space for storing variables.

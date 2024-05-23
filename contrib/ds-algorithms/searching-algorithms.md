# Searching Algorithms

Searching algorithms are techniques used to locate specific items within a collection of data. These algorithms are fundamental in computer science and are employed in various applications, from databases to web search engines.

## Real Life Example of Searching
- Searching for a word in a dictionary
- Searching for a specific book in a library
- Searching for a contact in your phone's address book
- Searching for a file on your computer, etc.

# Some common searching techniques

# 1. Linear Search

Linear search, also known as sequential search, is a straightforward searching algorithm that checks each element in a collection until the target element is found or the entire collection has been traversed. It is simple to implement but becomes inefficient for large datasets.

**Algorithm Overview:**
- **Sequential Checking:** The algorithm iterates through each element in the collection, starting from the first element.
- **Comparing Elements:** At each iteration, it compares the current element with the target element.
- **Finding the Target:** If the current element matches the target, the search terminates, and the index of the element is returned.
- **Completing the Search:** If the entire collection is traversed without finding the target, the algorithm indicates that the element is not present.

## Linear Search Code in Python

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 8, 1, 2]
target = 8
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
```

## Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

</br>
<hr>
</br>

# 2. Binary Search

Binary search is an efficient searching algorithm that works on sorted collections. It repeatedly divides the search interval in half until the target element is found or the interval is empty. Binary search is significantly faster than linear search but requires the collection to be sorted beforehand.

**Algorithm Overview:**
- **Initial State:** Binary search starts with the entire collection as the search interval.
- **Divide and Conquer:** At each step, it calculates the middle element of the current interval and compares it with the target.
- **Narrowing Down the Interval:** If the middle element is equal to the target, the search terminates successfully. Otherwise, it discards half of the search interval based on the comparison result.
- **Repeating the Process:** The algorithm repeats this process on the remaining half of the interval until the target is found or the interval is empty.

## Binary Search Code in Python (Iterative)

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
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
```

## Binary Search Code in Python (Recursive)

```python
def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
```

## Complexity Analysis
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1) (Iterative), O(log n) (Recursive)

</br>
<hr>
</br>

# 3. Interpolation Search

Interpolation search is an improved version of binary search, especially useful when the elements in the collection are uniformly distributed. Instead of always dividing the search interval in half, interpolation search estimates the position of the target element based on its value and the values of the endpoints of the search interval.

**Algorithm Overview:**
- **Estimating Position:** Interpolation search calculates an approximate position of the target element within the search interval based on its value and the values of the endpoints.
- **Refining the Estimate:** It adjusts the estimated position based on whether the target value is likely to be closer to the beginning or end of the search interval.
- **Updating the Interval:** Using the refined estimate, it narrows down the search interval iteratively until the target is found or the interval becomes empty.

## Interpolation Search Code in Python

```python
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
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

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 60
result = interpolation_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
```

## Complexity Analysis
- **Time Complexity**: O(log log n) (Average)
- **Space Complexity**: O(1)

</br>
<hr>
</br>


# Sorting Algorithms

In computer science, a sorting algorithm takes a collection of items and arranges them in a specific order. This order is usually determined by comparing the items using a defined rule.

Real Life Example of Sorting

- Sorting a deck of cards
- Sorting names in alphabetical order
- Sorting a list of items, etc.

Some common sorting techniques:

## 1. Bubble Sort

Bubble sort is a basic sorting technique that iteratively steps through a list, comparing neighboring elements. If elements are out of order, it swaps them. While easy to understand, bubble sort becomes inefficient for large datasets due to its slow execution time.

**Algorithm Overview:**
- **Pass by Pass:** During each pass, the algorithm iterates through the list.
- **Comparing Neighbors:** In each iteration, it compares adjacent elements in the list.
- **Swapping for Order:** If the elements are in the wrong order (typically, the first being larger than the second), it swaps their positions.
- **Bubbling Up the Largest:** This swapping process effectively pushes the largest element encountered in a pass towards the end of the list, like a bubble rising in water.
- **Repeating Until Sorted:** The algorithm continues making passes through the list until no more swaps are needed. This indicates the entire list is sorted.


### Bubble Sort Code in Python

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 3, 8, 1, 2]
bubble_sort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 5, 8]
```

### Example with Visualization

Let's sort the list `[5, 3, 8, 1, 2]` using bubble sort.

1. **Pass 1:**
   - Comparing neighbors: `[3, 5, 1, 2, 8]`
   - Swapping: `[3, 5, 1, 2, 8]` → `[3, 1, 5, 2, 8]` → `[3, 1, 2, 5, 8]`
   - Result: `[3, 1, 2, 5, 8]`

2. **Pass 2:**
   - Comparing neighbors: `[1, 3, 2, 5, 8]`
   - Swapping: `[1, 3, 2, 5, 8]` → `[1, 2, 3, 5, 8]`
   - Result: `[1, 2, 3, 5, 8]`

3. **Pass 3:**
   - Comparing neighbors: `[1, 2, 3, 5, 8]`
   - No swapping needed, the list is already sorted.

### Complexity Analysis

- **Worst Case:** `O(n^2)` comparisons and swaps. This happens when the list is in reverse order, and we need to make maximum swaps.
- **Best Case:** `O(n)` comparisons. This occurs when the list is already sorted, but we still need O(n^2) swaps because of the nested loops.
- **Average Case:** `O(n^2)` comparisons and swaps. This is the expected number of comparisons and swaps over all possible input sequences.

## 2. Selection Sort

Selection sort is a simple sorting algorithm that divides the input list into two parts: a sorted sublist and an unsorted sublist. The algorithm repeatedly finds the smallest (or largest, depending on sorting order) element from the unsorted sublist and moves it to the sorted sublist. It's not efficient for large datasets but performs better than bubble sort due to fewer swaps.

**Algorithm Overview:**
- **Initial State:** The entire list is considered unsorted initially.
- **Selecting the Minimum:** The algorithm repeatedly selects the smallest element from the unsorted sublist and moves it to the sorted sublist.
- **Expanding the Sorted Sublist:** As elements are moved to the sorted sublist, it expands until all elements are sorted.
- **Repeating Until Sorted:** The process continues until the entire list is sorted.

### Example with Visualization

Let's sort the list `[5, 3, 8, 1, 2]` using selection sort.

1. **Pass 1:**
   - Initial list: `[5, 3, 8, 1, 2]`
   - Find the minimum: `1`
   - Swap with the first element: `[1, 3, 8, 5, 2]`

2. **Pass 2:**
   - Initial list: `[1, 3, 8, 5, 2]`
   - Find the minimum: `2`
   - Swap with the second element: `[1, 2, 8, 5, 3]`

3. **Pass 3:**
   - Initial list: `[1, 2, 8, 5, 3]`
   - Find the minimum: `3`
   - Swap with the third element: `[1, 2, 3, 5, 8]`

4. **Pass 4:**
   - Initial list: `[1, 2, 3, 5, 8]`
   - Find the minimum: `5`
   - No swapping needed, the list is already sorted.

### Selection Sort Code in Python

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [5, 3, 8, 1, 2]
selection_sort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 5, 8]
```

### Complexity Analysis

- **Worst Case**: `O(n^2)` comparisons and O(n) swaps. This occurs when the list is in reverse order, and we need to make maximum comparisons and swaps.
- **Best Case**: `O(n^2)` comparisons and O(n) swaps. This happens when the list is in sorted order, but the algorithm still needs to iterate through all elements for comparisons.
- **Average Case**: `O(n^2)` comparisons and O(n) swaps. This is the expected number of comparisons and swaps over all possible input sequences.

## 3. Quick Sort
Quick sort is a popular divide-and-conquer sorting algorithm known for its efficiency on average. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.

**Algorithm Overview:**
- **Pivot Selection:** Choose a pivot element from the array. Common strategies include selecting the first, last, middle, or a randomly chosen element.
- **Partitioning:** Rearrange the array so that all elements less than the pivot are on its left, and all elements greater than the pivot are on its right. This step ensures that the pivot element is placed in its correct sorted position.
- **Recursion:** Apply the above steps recursively to the sub-arrays formed by partitioning until the base case is reached. The base case is usually when the size of the sub-array becomes 0 or 1, indicating it is already sorted.
- **Base Case:** If the sub-array size becomes 0 or 1, it is already sorted.

### Example with Visualization

Let's sort the list `[5, 3, 8, 1, 2]` using quick sort.

1. **Initial Array:** `[5, 3, 8, 1, 2]`
2. **Choose Pivot:** Let's choose the last element, `2`, as the pivot.
3. **Partitioning:**
   - We'll partition the array around the pivot `2`. All elements less than `2` will be placed to its left, and all elements greater than `2` will be placed to its right.
   - After partitioning, the array becomes `[1, 2, 5, 3, 8]`. The pivot element, `2`, is now in its correct sorted position.
4. **Recursion:**
   - Now, we recursively sort the sub-arrays `[1]` and `[5, 3, 8]`.
     - For the sub-array `[5, 3, 8]`, we choose `8` as the pivot and partition it.
     - After partitioning, the sub-array becomes `[3, 5, 8]`. The pivot element, `8`, is now in its correct sorted position.
5. **Concatenation:**
   - Concatenating the sorted sub-arrays `[1]`, `[2]`, `[3, 5, 8]`, we get the final sorted array `[1, 2, 3, 5, 8]`.

### Quick Sort Code in Python (Iterative)

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_iterative(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort_iterative(arr)
print("Sorted array:", arr)  # Output: [3, 9, 10, 27, 38, 43, 82]

```

### Quick Sort Code in Python (Recursive)

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

arr = [5, 3, 8, 1, 2]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)  # Output: [1, 2, 3, 5, 8]
```

### Complexity Analysis

- **Worst Case**: The worst-case time complexity of quick sort is `O(n^2)`. This occurs when the pivot selection consistently results in unbalanced partitioning, such as choosing the smallest or largest element as the pivot.
-**Best Case**: The best-case time complexity is `O(n log n)`. This happens when the pivot selection leads to well-balanced partitioning, halving the array size in each recursive call.
- **Average Case**: The average-case time complexity is `O(n log n)`. This is the expected time complexity when the pivot selection results in reasonably balanced partitioning across recursive calls.
- **Space Complexity**: Quick sort has an `O(log n)` space complexity for the recursion stack, as it recursively sorts sub-arrays.

## 4. Merge Sort

Merge sort is a divide-and-conquer algorithm that recursively divides the input list into smaller sublists until each sublist contains only one element. Then, it repeatedly merges adjacent sublists while maintaining the sorted order until there is only one sublist remaining, which represents the sorted list.

**Algorithm Overview:**
- **Divide:** Split the input list into smaller sublists recursively until each sublist contains only one element.
- **Merge:** Repeatedly merge adjacent sublists while maintaining the sorted order until there is only one sublist remaining, which represents the sorted list.

### Example with Visualization

Let's sort the list `[38, 27, 43, 3, 9, 82, 10]` using merge sort.

1. **Initial Division:**
   - Divide the list into sublists: `[38, 27, 43, 3, 9, 82, 10]`
   - Visually it looks like
   `[38], [27], [43], [3], [9], [82], [10]`

2. **Merge Passes:**
   - Merge adjacent sublists while maintaining sorted order:
     - Pass 1: `[27, 38]`, `[3, 43]`, `[9, 82]`, `[10]`
     - Pass 2: `[3, 27, 38, 43]`, `[9, 10, 82]`
     - Pass 3: `[3, 9, 10, 27, 38, 43, 82]`


3. **Final Sorted List:**
   - `[3, 9, 10, 27, 38, 43, 82]`

### Merge Sort Code in Python (Iterative)

```python
def merge_sort_iterative(arr):
    n = len(arr)
    curr_size = 1
    while curr_size < n:
        left = 0
        while left < n - 1:
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)
            merge(arr, left, mid, right)
            left += 2 * curr_size
        curr_size *= 2

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_iterative(arr)
print("Sorted array:", arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
```

### Merge Sort Code in Python (Recursive)

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements are remaining in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any elements are remaining in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
```

### Complexity Analysis
- **Time Complexity**: `O(n log n)` for all cases. Merge sort always divides the list into halves until each sublist contains only one element, and then merges them back together, resulting in O(n log n) time complexity.
- **Space Complexity**: `O(n)` auxiliary space. In the iterative version, merge sort uses additional space for creating temporary sublists during merging operations.

## 5. Insertion Sort

Insertion sort is a straightforward and efficient sorting algorithm for small datasets. It builds the final sorted array one element at a time. It is much like sorting playing cards in your hands: you take one card at a time and insert it into its correct position among the already sorted cards.

**Algorithm Overview:**
- **Start from the Second Element:** Begin with the second element, assuming the first element is already sorted.
- **Compare with Sorted Subarray:** Take the current element and compare it with elements in the sorted subarray (the part of the array before the current element).
- **Insert in Correct Position:** Shift all elements in the sorted subarray that are greater than the current element to one position ahead. Insert the current element into its correct position.
- **Repeat Until End:** Repeat this process for all elements in the array.

### Example with Visualization
Let's sort the list `[5, 3, 8, 1, 2]` using insertion sort.

**Step-by-Step Visualization:**
**Initial List:** `[5, 3, 8, 1, 2]`

1. **Pass 1:**
   - Current element: 3
   - Compare 3 with 5, move 5 to the right: `[5, 5, 8, 1, 2]`
   - Insert 3 in its correct position: `[3, 5, 8, 1, 2]`

2. **Pass 2:**
   - Current element: 8
   - 8 is already in the correct position: `[3, 5, 8, 1, 2]`
    
3. **Pass 3:**
   - Current element: 1
   - Compare 1 with 8, move 8 to the right: `[3, 5, 8, 8, 2]`
   - Compare 1 with 5, move 5 to the right: `[3, 5, 5, 8, 2]`
   - Compare 1 with 3, move 3 to the right: `[3, 3, 5, 8, 2]`
   - Insert 1 in its correct position: `[1, 3, 5, 8, 2]`
    
4. **Pass 4:**
   - Current element: 2
   - Compare 2 with 8, move 8 to the right: `[1, 3, 5, 8, 8]`
   - Compare 2 with 5, move 5 to the right: `[1, 3, 5, 5, 8]`
   - Compare 2 with 3, move 3 to the right: `[1, 3, 3, 5, 8]`
   - Insert 2 in its correct position: `[1, 2, 3, 5, 8]`

### Insertion Sort Code in Python


```python

def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [5, 3, 8, 1, 2]
insertion_sort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 5, 8]
```

### Complexity Analysis
  - **Worst Case:** `𝑂(𝑛^2)` comparisons and swaps. This occurs when the array is in reverse order.
  - **Best Case:** `𝑂(𝑛)` comparisons and `𝑂(1)` swaps. This happens when the array is already sorted.
  - **Average Case:** `𝑂(𝑛^2)` comparisons and swaps. This is the expected number of comparisons and swaps over all possible input sequences.

## 6. Heap Sort

Heap Sort is an efficient comparison-based sorting algorithm that uses a binary heap data structure. It divides its input into a sorted and an unsorted region and iteratively shrinks the unsorted region by extracting the largest (or smallest) element and moving it to the sorted region.

**Algorithm Overview:**
- **Build a Max Heap:** Convert the array into a max heap, a complete binary tree where the value of each node is greater than or equal to the values of its children.
- **Heapify:** Ensure that the subtree rooted at each node satisfies the max heap property. This process is called heapify.
- **Extract Maximum:** Swap the root (the maximum element) with the last element of the heap and reduce the heap size by one. Restore the max heap property by heapifying the root.
- **Repeat:** Continue extracting the maximum element and heapifying until the entire array is sorted.

### Example with Visualization

Let's sort the list `[5, 3, 8, 1, 2]` using heap sort.

1. **Build Max Heap:**
   - Initial array: `[5, 3, 8, 1, 2]`
   - Start heapifying from the last non-leaf node.
   - Heapify at index 1: `[5, 3, 8, 1, 2]` (no change, children are already less than the parent)
   - Heapify at index 0: `[8, 3, 5, 1, 2]` (swap 5 and 8 to make 8 the root)

2. **Heapify Process:**
   - Heapify at index 0: `[8, 3, 5, 1, 2]` (no change needed, already a max heap)

3. **Extract Maximum:**
   - Swap root with the last element: `[2, 3, 5, 1, 8]`
   - Heapify at index 0: `[5, 3, 2, 1, 8]` (swap 2 and 5)
     
4. **Repeat Extraction:**
   - Swap root with the second last element: `[1, 3, 2, 5, 8]`
   - Heapify at index 0: `[3, 1, 2, 5, 8]` (swap 1 and 3)
   - Swap root with the third last element: `[2, 1, 3, 5, 8]`
   - Heapify at index 0: `[2, 1, 3, 5, 8]` (no change needed)
   - Swap root with the fourth last element: `[1, 2, 3, 5, 8]`

After all extractions, the array is sorted: `[1, 2, 3, 5, 8]`.

### Heap Sort Code in Python

```python
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # See if left child of root exists and is greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Example usage
arr = [5, 3, 8, 1, 2]
heap_sort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 5, 8]
```

### Complexity Analysis
 - **Worst Case:** `𝑂(𝑛log𝑛)`. Building the heap takes `𝑂(𝑛)` time, and each of the 𝑛 element extractions takes `𝑂(log𝑛)` time.
 - **Best Case:** `𝑂(𝑛log𝑛)`. Even if the array is already sorted, heap sort will still build the heap and perform the extractions.
 - **Average Case:** `𝑂(𝑛log𝑛)`. Similar to the worst-case, the overall complexity remains `𝑂(𝑛log𝑛)` because each insertion and deletion in a heap takes `𝑂(log𝑛)` time, and these operations are performed 𝑛 times.

 ## 7. Radix Sort
Radix Sort is a non-comparative integer sorting algorithm that sorts numbers by processing individual digits. It processes digits from the least significant digit (LSD) to the most significant digit (MSD) or vice versa. This algorithm is efficient for sorting numbers with a fixed number of digits.

**Algorithm Overview:**
- **Digit by Digit sorting:** Radix sort processes the digits of the numbers starting from either the least significant digit (LSD) or the most significant digit (MSD). Typically, LSD is used.
- **Stable Sort:** A stable sorting algorithm like Counting Sort or Bucket Sort is used as an intermediate sorting technique. Radix Sort relies on this stability to maintain the relative order of numbers with the same digit value.
- **Multiple passes:**  The algorithm performs multiple passes over the numbers, one for each digit, from the least significant to the most significant.

### Radix Sort Code in Python

```python
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)
```

### Complexity Analysis
 - **Time Complexity:** O(d * (n + k)) for all cases. Radix Sort always processes each digit of every number in the array.
 - **Space Complexity:** O(n + k). This is due to the space required for:
- The output array used in Counting Sort, which is of size n.
- The count array used in Counting Sort, which is of size k.

## 8. Counting Sort
Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then do some arithmetic to calculate the position of each object in the output sequence. 

**Algorithm Overview:**
- Convert the input string into a list of characters.
- Count the occurrence of each character in the list using the collections.Counter() method.
- Sort the keys of the resulting Counter object to get the unique characters in the list in sorted order.
- For each character in the sorted list of keys, create a list of repeated characters using the corresponding count from the Counter object.
- Concatenate the lists of repeated characters to form the sorted output list.


### Counting Sort Code in Python using counter method.

```python
from collections import Counter

def counting_sort(arr):
	count = Counter(arr)
	output = []
	for c in sorted(count.keys()):
		output +=  * count
	return output

arr = "geeksforgeeks"
arr = list(arr)
arr = counting_sort(arr)
output = ''.join(arr)
print("Sorted character array is", output)

```
### Counting Sort Code in Python using sorted() and reduce():

```python
from functools import reduce
string = "geeksforgeeks"
sorted_str = reduce(lambda x, y: x+y, sorted(string))
print("Sorted string:", sorted_str)
```

### Complexity Analysis
 - **Time Complexity:** O(n+k) for all cases.No matter how the elements are placed in the array, the algorithm goes through n+k times
 - **Space Complexity:** O(max). Larger the range of elements, larger is the space complexity.

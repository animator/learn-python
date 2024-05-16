# Sorting Algorithms

## Overview

Sorting algorithms are used to reorder elements in a list or array so that they follow a particular sequence, typically ascending or descending order. Below are several common sorting algorithms, each with a description and code example.

---

## 1. Bubble Sort

### Description
Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

### Code
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
arr = list(map(int,input().split(","))
print("Sorted array is:", bubble_sort(arr))
```
### Time Complexity of Bubble Sort



Bubble Sort has the following time complexity:

- **Best Case**: O(n)
  - The best-case scenario occurs when the input array is already sorted. In this case, Bubble Sort requires only one pass through the array to verify that it is sorted, resulting in linear time complexity.

- **Average Case**: O(n^2)
  - In the average case, Bubble Sort compares each pair of adjacent elements and performs swaps as necessary. This results in quadratic time complexity, making it inefficient for large datasets.

- **Worst Case**: O(n^2)
  - The worst-case scenario occurs when the input array is sorted in reverse order. In this case, Bubble Sort requires the maximum number of passes through the array and comparisons, resulting in quadratic time complexity.

### Conclusion

Bubble Sort's time complexity makes it inefficient for large datasets, especially in comparison to more efficient sorting algorithms like Merge Sort or Quick Sort. However, it remains a simple and easy-to-understand algorithm, often used for educational purposes or for sorting small datasets where performance is not critical.

## 2. Selection Sort

### Description

Selection Sort divides the input list into two parts: a sorted sublist of items which is built up from left to right and a sublist of the remaining unsorted items. It repeatedly selects the smallest (or largest) element from the unsorted sublist, swapping it with the leftmost unsorted element.

### Code

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
print("Sorted array is:", selection_sort(arr))
```
### Time Complexity of Selection Sort


Selection Sort has the following time complexity:

- **Best Case**: O(n^2)
  - In the best-case scenario, Selection Sort still needs to iterate through the entire array to find the smallest element in each pass, resulting in quadratic time complexity.

- **Average Case**: O(n^2)
  - Similarly, in the average case, Selection Sort requires nested loops to compare each element with the remaining elements, resulting in quadratic time complexity.

- **Worst Case**: O(n^2)
  - The worst-case scenario for Selection Sort also involves nested loops and requires the maximum number of comparisons and swaps, resulting in quadratic time complexity.

### Conclusion

Selection Sort's time complexity makes it inefficient for large datasets, especially in comparison to more efficient sorting algorithms like Merge Sort or Quick Sort. It's primarily used for educational purposes or for sorting small datasets where performance is not critical due to its simplicity and ease of implementation.

## 3. Insertion Sort

### Description

Insertion Sort builds the sorted array one item at a time, with the final sorted array being built in-place. It picks an element and inserts it into its correct position in the sorted part of the array.

### Code

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
print("Sorted array is:", insertion_sort(arr))
```
### Time Complexity of Insertion Sort

Insertion Sort has the following time complexity:

- **Best Case**: O(n)
  - In the best-case scenario, Insertion Sort requires only one pass through the array to verify that it is already sorted. Since no swaps are needed, the time complexity is linear.

- **Average Case**: O(n^2)
  - In the average case, Insertion Sort compares each element with the elements to its left and performs swaps as necessary. This results in quadratic time complexity.

- **Worst Case**: O(n^2)
  - The worst-case scenario occurs when the input array is sorted in reverse order. In this case, Insertion Sort requires the maximum number of comparisons and swaps, resulting in quadratic time complexity.

### Conclusion

Insertion Sort's time complexity makes it inefficient for large datasets, especially in comparison to more efficient sorting algorithms like Merge Sort or Quick Sort. However, it remains a simple and easy-to-understand algorithm, often used for educational purposes or for sorting small datasets where performance is not critical.

## 4. Merge Sort

### Description

Merge Sort is a divide-and-conquer algorithm that splits the list into equal halves until each sublist contains a single element. Then it merges those sublists to produce sorted sublists until it gets a single sorted list.

### Code

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Sorted array is:", merge_sort(arr))
```
### Time Complexity of Merge Sort


Merge Sort has the following time complexity:

- **Best Case**: O(n log n)
  - In the best-case scenario, Merge Sort divides the array into equal halves until each sublist contains a single element. Then it merges the sublists in a way that requires logarithmic time complexity for each level of recursion, resulting in a total time complexity of O(n log n).

- **Average Case**: O(n log n)
  - Similarly, in the average case, Merge Sort's divide-and-conquer approach results in logarithmic time complexity for each level of recursion, leading to O(n log n) overall.

- **Worst Case**: O(n log n)
  - The worst-case scenario for Merge Sort also involves logarithmic time complexity for each level of recursion, resulting in O(n log n) time complexity. This remains true regardless of the input data's initial order.

### Conclusion

Merge Sort's time complexity of O(n log n) makes it efficient for sorting large datasets, making it suitable for various applications where sorting speed is crucial. It's a stable and predictable algorithm, widely used in practice due to its efficiency and stability.

## 5. Quick Sort

### Description

Quick Sort is a divide-and-conquer algorithm that picks an element as a pivot and partitions the array around the pivot, ensuring that elements on the left are less than the pivot and elements on the right are greater than the pivot.

### Code

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
print("Sorted array is:", quick_sort(arr))
```
### Time Complexity of Quick Sort


Quick Sort has the following time complexity:

- **Best Case**: O(n log n)
  - In the best-case scenario, Quick Sort divides the array into nearly equal halves at each step, resulting in logarithmic time complexity for each level of recursion. Therefore, the overall time complexity is O(n log n).

- **Average Case**: O(n log n)
  - Similarly, in the average case, Quick Sort's divide-and-conquer approach results in logarithmic time complexity for each level of recursion, leading to O(n log n) overall.

- **Worst Case**: O(n^2)
  - The worst-case scenario for Quick Sort occurs when the chosen pivot is either the smallest or largest element in the array, leading to highly unbalanced partitions. This results in quadratic time complexity of O(n^2).

### Conclusion

Quick Sort's average time complexity of O(n log n) makes it efficient for sorting large datasets, making it suitable for various applications where sorting speed is crucial. However, its worst-case time complexity of O(n^2) is a concern, although this can be mitigated by using randomized or median-of-three pivot selection strategies.

## 6. Heap Sort

### Description

Heap Sort involves building a heap from the input list and then repeatedly extracting the maximum element from the heap and reconstructing the heap until all elements are sorted.

### Code

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Sorted array is:", heap_sort(arr))
```
### Time Complexity of Heap Sort


Heap Sort has the following time complexity:

- **Best Case**: O(n log n)
  - In the best-case scenario, Heap Sort constructs a heap from the input array in linear time, followed by logarithmic time complexity for each extraction of the maximum element and reconstruction of the heap. Therefore, the overall time complexity is O(n log n).

- **Average Case**: O(n log n)
  - Similarly, in the average case, Heap Sort's heap construction and extraction operations result in logarithmic time complexity, leading to O(n log n) overall.

- **Worst Case**: O(n log n)
  - The worst-case scenario for Heap Sort occurs when the input array is already sorted in reverse order. In this case, building the heap still takes linear time, but each extraction and heap reconstruction may require the maximum number of comparisons, resulting in O(n log n) time complexity.

### Conclusion

Heap Sort's time complexity of O(n log n) makes it efficient for sorting large datasets, making it suitable for various applications where sorting speed is crucial. It's a stable and predictable algorithm, widely used in practice due to its efficiency and space efficiency.


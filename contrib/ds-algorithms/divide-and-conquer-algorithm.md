# Divide and Conquer Algorithms

Divide and Conquer is a paradigm for solving problems that involves breaking a problem into smaller sub-problems, solving the sub-problems recursively, and then combining their solutions to solve the original problem.

## Merge Sort

Merge Sort is a popular sorting algorithm that follows the divide and conquer strategy. It divides the input array into two halves, recursively sorts the halves, and then merges them.

**Algorithm Overview:**
- **Divide:** Divide the unsorted list into two sublists of about half the size.
- **Conquer:** Recursively sort each sublist.
- **Combine:** Merge the sorted sublists back into one sorted list.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr)
```

## Complexity Analysis
- **Time Complexity:** O(n log n) in all cases
- **Space Complexity:** O(n) additional space for the merge operation
  
## Examples
### 1. Count inversions in an array

An inversion in an array is a situation where two elements a[i]a[i] and a[j]a[j] form an inversion if a[i] > a[j] and i < j.Counting the number of inversions in an array can be efficiently done using a modified merge sort algorithm. 

**Algorithm:**
- **Initialization:** We start by initializing a temporary array temp_arr of the same size as the input array arr. This temporary array is used during the merge process.
- **Recursive Division (Merge Sort):** The main function count_inversions calls merge_sort, which recursively splits the array into two halves until each subarray contains a single element.
- **Merge and Count:** Once the subarrays are reduced to single elements, the merge function merges the subarrays back together while counting inversions.
  
```python
def merge(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0

    # Conditions to ensure that i doesn't exceed mid and j doesn't exceed right
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There are mid - i inversions, because all the remaining elements in the left subarray (arr[i], arr[i+1], ..., arr[mid]) are greater than arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2

        inv_count += merge_sort(arr, temp_arr, left, mid)
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)

        inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count

def count_inversions(arr):
    temp_arr = [0]*len(arr)
    return merge_sort(arr, temp_arr, 0, len(arr) - 1)

# Test case
arr = [1, 20, 6, 4, 5]
result = count_inversions(arr)
print("Number of inversions are:", result) #output- Number of inversions are: 5
```
### 2. Count Reverse Pairs

Given an array of numbers, return the count of reverse pairs. Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].

**Algorithm:**
- **Divide the Array:** Recursively divide the array into two halves until each subarray contains a single element.
- **Count Reverse Pairs:** For each split, count the reverse pairs where arr[i]>2*arr[j] and i<j. This counting is done before merging the two halves.
- **Merge and Sort:** Merge the two sorted halves back together.

```python
def merge(arr, temp_arr, left, mid, right):
    j = mid + 1
    inv_count = 0

    # Count reverse pairs
    for i in range(left, mid + 1):
        while j <= right and arr[i] > 2 * arr[j]:
            j += 1
        inv_count += (j - (mid + 1))

    # Merge step
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into Original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort(arr, temp_arr, left, mid)
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)

        inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count

def count_reverse_pairs(arr):
    temp_arr = [0] * len(arr)
    return merge_sort(arr, temp_arr, 0, len(arr) - 1)

#Test case
arr = [3, 2, 1, 4]
count = count_reverse_pairs(arr)
print("The number of reverse pair:", count) #output- Number of reverse pair: 1
```

### 3. Merge Overlapping Sub-intervals

Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.

**Algorithm:**
- **Sort the Intervals:** Sort the intervals based on the starting point. If two intervals have the same starting point, sort them by the ending point.
- **Initialize the Merged Intervals List:** Start with the first interval and add it to the merged intervals list.
- **Iterate and Merge:** Iterate through each interval and compare it with the last interval in the merged list.If the current interval overlaps with the last merged interval, merge them by updating the end of the last merged interval.If the current interval does not overlap, add it to the merged list as a new interval.

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the starting point
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If merged list is empty or current interval does not overlap with the last merged interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap, so merge the current interval with the last interval in merged list
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Test case:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(intervals)
print(f"Merged intervals: {result}") # output- [[1, 6], [8, 10], [15, 18]]
```
---



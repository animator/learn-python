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

---

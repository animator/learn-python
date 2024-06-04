# Two-Pointer Technique

---

- The two-pointer technique is a popular algorithmic strategy used to solve various problems efficiently. This technique involves using two pointers (or indices) to traverse through data structures such as arrays or linked lists. 
- The pointers can move in different directions, allowing for efficient processing of elements to achieve the desired results.

## Common Use Cases

1. **Finding pairs in a sorted array that sum to a target**: One pointer starts at the beginning and the other at the end.
2. **Reversing a linked list**: One pointer starts at the head, and the other at the next node, progressing through the list.
3. **Removing duplicates from a sorted array**: One pointer keeps track of the unique elements, and the other traverses the array.
4. **Merging two sorted arrays**: Two pointers are used to iterate through the arrays and merge them.

## Example 1: Finding Pairs with a Given Sum

### Problem Statement

Given a sorted array of integers and a target sum, find all pairs in the array that sum up to the target.

### Approach

1. Initialize two pointers: one at the beginning (`left`) and one at the end (`right`) of the array.
2. Calculate the sum of the elements at the `left` and `right` pointers.
3. If the sum is equal to the target, record the pair and move both pointers inward.
4. If the sum is less than the target, move the `left` pointer to the right to increase the sum.
5. If the sum is greater than the target, move the `right` pointer to the left to decrease the sum.
6. Repeat the process until the `left` pointer is not less than the `right` pointer.

### Example Code

```python
def find_pairs_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
result = find_pairs_with_sum(arr, target)
print("Pairs with sum", target, "are:", result)
 ```

## Example 2: Removing Duplicates from a Sorted Array

### Problem Statement
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length of the array.

### Approach
1. If the array is empty, return 0.
2. Initialize a slow pointer at the beginning of the array.
3. Use a fast pointer to traverse through the array.
4. Whenever the element at the fast pointer is different from the element at the slow pointer, increment the slow pointer and update the element at the slow pointer with the element at the fast pointer.
5. Continue this process until the fast pointer reaches the end of the array.
6. The slow pointer will indicate the position of the last unique element.

### Example Code

```python
def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1

# Example usage
arr = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(arr)
print("Array after removing duplicates:", arr[:new_length])
print("New length of array:", new_length)
```
# Advantages of the Two-Pointer Technique

Here are some key benefits of using the two-pointer technique:

## 1. **Improved Time Complexity**

It often reduces the time complexity from O(n^2) to O(n), making it significantly faster for many problems.

### Example
- **Finding pairs with a given sum**: Efficiently finds pairs in O(n) time.

## 2. **Simplicity**

The implementation is straightforward, using basic operations like incrementing or decrementing pointers.

### Example
- **Removing duplicates from a sorted array**: Easy to implement and understand.

## 3. **In-Place Solutions**

Many problems can be solved in place, requiring no extra space beyond the input data.

### Example
- **Reversing a linked list**: Adjusts pointers within the existing nodes.

## 4. **Versatility**

Applicable to a wide range of problems, from arrays and strings to linked lists.

### Example
- **Merging two sorted arrays**: Efficiently merges using two pointers.

## 5. **Efficiency**

Minimizes redundant operations and enhances performance, especially with large data sets.

### Example
- **Partitioning problems**: Efficiently partitions elements with minimal operations.


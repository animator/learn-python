###Kadane's Algorithm

###Theory:

**Kadane's Algorithm** is a dynamic programming technique used to find the maximum subarray sum in an array of numbers. It helps us find the maximum sum of numbers that are next to each other in a list of numbers. It handles both positive and negative numbers and is known for its linear time complexity.

The algorithm maintains two variables: **max_current** represents the maximum sum ending at the current position, and **max_global** represents the maximum subarray sum encountered so far. 

###Algorithm:

1. **Initialization**:
   Initialize two variables: 'max_current' to store the maximum sum of the subarray ending at the current position, and 'max_global' to store the maximum sum found so far across all subarrays.
   
3. **Iteration**:
   For each element in the array:
     - Update max_current to be the maximum of the current element itself or the sum of max_current and the current element (this decides whether to start a new subarray or to continue the existing one).
     - Update max_global to be the maximum of max_global and max_current.
       
4. **Result**:
   After iterating through the array, **max_global** will hold the maximum sum of any contiguous subarray.

###Time Complexity

O(n): The algorithm runs in linear time because it makes a single pass through the array.

###Space Complexity

O(1): The algorithm uses only a constant amount of extra space.

###Code

```python
def kadane(arr):
    max_current = arr[0]
    max_global = arr[0]
    
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    
    return max_global
```

### Example usage:

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Maximum sum of contiguous subarray:", kadane(arr))  # Output: 6

**Example Explanation**

Given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4], 
Kadane's Algorithm will find that the subarray [4, -1, 2, 1] has the maximum sum of 6.

###Computational Analysis

**Time Complexity**: O(n), where n is the number of elements in the array.

**Space Complexity**: O(1), since the algorithm uses a constant amount of extra space regardless of the input size.

###Applications

**Financial Data Analysis**: Finding maximum profit from daily stock prices.

**Image Processing**: Detecting regions with maximum brightness in images.

**Genomics**: Analyzing DNA sequences for regions with the highest similarity.

**Kadane's Algorithm** is widely used due to its simplicity and efficiency in solving the **maximum subarray sum** problem.

# Sliding Window Technique

The sliding window technique is a fundamental approach used to solve problems involving arrays, lists, or sequences. It's particularly useful when you need to calculate something over a subarray or sublist of fixed size that slides over the entire array.

In easy words, It is the transformation of the nested loops into the single loop 
## Concept

The sliding window technique involves creating a window (a subarray or sublist) that moves or "slides" across the entire array. This window can either be fixed in size or dynamically resized. By maintaining and updating this window as it moves, you can optimize certain computations, reducing time complexity.

## Types of Sliding Windows

1. **Fixed Size Window**: The window size remains constant as it slides from the start to the end of the array.
2. **Variable Size Window**: The window size can change based on certain conditions, such as the sum of elements within the window meeting a specified target.

## Steps to Implement a Sliding Window

1. **Initialize the Window**: Set the initial position of the window and any required variables (like sum, count, etc.).
2. **Expand the Window**: Add the next element to the window and update the relevant variables.
3. **Shrink the Window**: If needed, remove elements from the start of the window and update the variables.
4. **Slide the Window**: Move the window one position to the right by including the next element and possibly excluding the first element.
5. **Repeat**: Continue expanding, shrinking, and sliding the window until you reach the end of the array.

## Example Problems

### 1. Maximum Sum Subarray of Fixed Size K

Given an array of integers and an integer k, find the maximum sum of a subarray of size k.

**Steps:**

1. Initialize the sum of the first k elements.
2. Slide the window from the start of the array to the end, updating the sum by subtracting the element that is left behind and adding the new element.
3. Track the maximum sum encountered.

**Python Code:**

```python
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None
    
    # Compute the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window from start to end
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage:
arr = [1, 3, 2, 5, 1, 1, 6, 2, 8, 5]
k = 3
print(max_sum_subarray(arr, k))  # Output: 16
```

### 2. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

**Steps:**

1. Use two pointers to represent the current window.
2. Use a set to track characters in the current window.
3. Expand the window by moving the right pointer.
4. If a duplicate character is found, shrink the window by moving the left pointer until the duplicate is removed.

**Python Code:**

```python
def longest_unique_substring(s):
    n = len(s)
    char_set = set()
    left = 0
    max_length = 0

    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage:
s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3
```
## 3. Minimum Size Subarray Sum

Given an array of positive integers and a positive integer `s`, find the minimal length of a contiguous subarray of which the sum is at least `s`. If there isn't one, return 0 instead.

### Steps:
1. Use two pointers, `left` and `right`, to define the current window.
2. Expand the window by moving `right` and adding `arr[right]` to `current_sum`.
3. If `current_sum` is greater than or equal to `s`, update `min_length` and shrink the window from the left by moving `left` and subtracting `arr[left]` from `current_sum`.
4. Repeat until `right` has traversed the array.

### Python Code:
```python
def min_subarray_len(s, arr):
    n = len(arr)
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += arr[right]

        while current_sum >= s:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0

# Example usage:
arr = [2, 3, 1, 2, 4, 3]
s = 7
print(min_subarray_len(s, arr))  # Output: 2 (subarray [4, 3])
```

## 4. Longest Substring with At Most K Distinct Characters

Given a string `s` and an integer `k`, find the length of the longest substring that contains at most `k` distinct characters.

### Steps:
1. Use two pointers, `left` and `right`, to define the current window.
2. Use a dictionary `char_count` to count characters in the window.
3. Expand the window by moving `right` and updating `char_count`.
4. If `char_count` has more than `k` distinct characters, shrink the window from the left by moving `left` and updating `char_count`.
5. Keep track of the maximum length of the window with at most `k` distinct characters.

### Python Code:
```python
def longest_substring_k_distinct(s, k):
    n = len(s)
    char_count = {}
    left = 0
    max_length = 0

    for right in range(n):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
s = "eceba"
k = 2
print(longest_substring_k_distinct(s, k))  # Output: 3 (substring "ece")
```

## 5. Maximum Number of Vowels in a Substring of Given Length

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

### Steps:
1. Use a sliding window of size `k`.
2. Keep track of the number of vowels in the current window.
3. Expand the window by adding the next character and update the count if it's a vowel.
4. If the window size exceeds `k`, remove the leftmost character and update the count if it's a vowel.
5. Track the maximum number of vowels found in any window of size `k`.

### Python Code:
```python
def max_vowels(s, k):
    vowels = set('aeiou')
    max_vowel_count = 0
    current_vowel_count = 0

    for i in range(len(s)):
        if s[i] in vowels:
            current_vowel_count += 1
        if i >= k:
            if s[i - k] in vowels:
                current_vowel_count -= 1
        max_vowel_count = max(max_vowel_count, current_vowel_count)

    return max_vowel_count

# Example usage:
s = "abciiidef"
k = 3
print(max_vowels(s, k))  # Output: 3 (substring "iii")
```

## 6. Subarray Product Less Than K

Given an array of positive integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is less than `k`.

### Steps:
1. Use two pointers, `left` and `right`, to define the current window.
2. Expand the window by moving `right` and multiplying `product` by `nums[right]`.
3. If `product` is greater than or equal to `k`, shrink the window from the left by moving `left` and dividing `product` by `nums[left]`.
4. For each position of `right`, the number of valid subarray ending at `right` is `right - left + 1`.
5. Sum these counts to get the total number of subarray with product less than `k`.

### Python Code:
```python
def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    
    product = 1
    left = 0
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product /= nums[left]
            left += 1

        count += right - left + 1

    return count

# Example usage:
nums = [10, 5, 2, 6]
k = 100
print(num_subarray_product_less_than_k(nums, k))  # Output: 8
```

## Advantages

- **Efficiency**: Reduces the time complexity from O(n^2) to O(n) for many problems.
- **Simplicity**: Provides a straightforward way to manage subarrays/substrings with overlapping elements.

## Applications

- Finding the maximum or minimum sum of subarrays of fixed size.
- Detecting unique elements in a sequence.
- Solving problems related to dynamic programming with fixed constraints.
- Efficiently managing and processing streaming data or real-time analytics.

By using the sliding window technique, you can tackle a wide range of problems in a more efficient manner.

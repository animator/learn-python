# Deque in Python

## Definition
A deque, short for double-ended queue, is an ordered collection of items that allows rapid insertion and deletion at both ends.

## Syntax
In Python, deques are implemented in the collections module:

```py
from collections import deque

# Creating a deque
d = deque(iterable)  # Create deque from iterable (optional)
```

## Operations
1. **Appending Elements**:

    - append(x): Adds element x to the right end of the deque.
    - appendleft(x): Adds element x to the left end of the deque.

2. **Removing Elements**:

    - pop(): Removes and returns the rightmost element.
    - popleft(): Removes and returns the leftmost element.

3. **Accessing Elements**:

    - deque[index]: Accesses element at index.

4. **Other Operations**:

    - extend(iterable): Extends deque by appending elements from iterable.
    - extendleft(iterable): Extends deque by appending elements from iterable to the left.
    - rotate(n): Rotates deque n steps to the right (negative n rotates left).

## Example

### 1. showing all the operations
```py
from collections import deque

# Initialize a deque
d = deque([1, 2, 3, 4, 5])
print("Initial deque:", d)

# Append elements
d.append(6)
print("After append(6):", d)

# Append left
d.appendleft(0)
print("After appendleft(0):", d)

# Pop from the right end
rightmost = d.pop()
print("Popped from right end:", rightmost)
print("Deque after pop():", d)

# Pop from the left end
leftmost = d.popleft()
print("Popped from left end:", leftmost)
print("Deque after popleft():", d)

# Accessing elements
print("Element at index 2:", d[2])

# Extend deque
d.extend([6, 7, 8])
print("After extend([6, 7, 8]):", d)

# Extend left
d.extendleft([-1, 0])
print("After extendleft([-1, 0]):", d)

# Rotate deque
d.rotate(2)
print("After rotate(2):", d)

# Rotate left
d.rotate(-3)
print("After rotate(-3):", d)
```
Output 
```py
Initial deque: deque([1, 2, 3, 4, 5])
After append(6): deque([1, 2, 3, 4, 5, 6])
After appendleft(0): deque([0, 1, 2, 3, 4, 5, 6])
Popped from right end: 6
Deque after pop(): deque([0, 1, 2, 3, 4, 5])
Popped from left end: 0
Deque after popleft(): deque([1, 2, 3, 4, 5])
Element at index 2: 3
After extend([6, 7, 8]): deque([1, 2, 3, 4, 5, 6, 7, 8])
After extendleft([-1, 0]): deque([0, -1, 1, 2, 3, 4, 5, 6, 7, 8])
After rotate(2): deque([7, 8, 0, -1, 1, 2, 3, 4, 5, 6])
After rotate(-3): deque([1, 2, 3, 4, 5, 6, 7, 8, 0, -1])

```

### 2. Finding Maximum in Sliding Window
```py
from collections import deque

def max_sliding_window(nums, k):
    if not nums:
        return []
    
    d = deque()
    result = []
    
    for i, num in enumerate(nums):
        # Remove elements from deque that are out of the current window
        if d and d[0] <= i - k:
            d.popleft()
        
        # Remove elements from deque smaller than the current element
        while d and nums[d[-1]] <= num:
            d.pop()
        
        d.append(i)
        
        # Add maximum for current window
        if i >= k - 1:
            result.append(nums[d[0]])
    
    return result

# Example usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print("Maximums in sliding window of size", k, "are:", max_sliding_window(nums, k))

```

Output 
```py
Maximums in sliding window of size 3 are: [3, 3, 5, 5, 6, 7]
```


## Applications
- **Efficient Queues and Stacks**: Deques allow fast O(1) append and pop operations from both ends, 
making them ideal for implementing queues and stacks.
- **Sliding Window Maximum/Minimum**: Used in algorithms that require efficient windowed 
computations.


## Advantages
- Efficiency: O(1) time complexity for append and pop operations from both ends.
- Versatility: Can function both as a queue and as a stack.
- Flexible: Supports rotation and slicing operations efficiently.


## Disadvantages
- Memory Usage: Requires more memory compared to simple lists due to overhead in managing linked 
nodes.

## Conclusion
- Deques in Python, provided by the collections.deque module, offer efficient double-ended queue 
operations with O(1) time complexity for append and pop operations on both ends. They are versatile 
data structures suitable for implementing queues, stacks, and more complex algorithms requiring 
efficient manipulation of elements at both ends.

- While deques excel in scenarios requiring fast append and pop operations from either end, they do 
consume more memory compared to simple lists due to their implementation using doubly-linked lists. 
However, their flexibility and efficiency make them invaluable for various programming tasks and 
algorithmic solutions.
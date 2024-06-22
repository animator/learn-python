# Heaps

## Definition: 
Heaps are a crucial data structure that support efficient priority queue operations. They come in two main types: min heaps and max heaps. Python's heapq module provides a robust implementation for min heaps, and with some minor adjustments, it can also be used to implement max heaps.

## Overview:
A heap is a specialized binary tree-based data structure that satisfies the heap property:

- **Min Heap:** The key at the root must be the minimum among all keys present in the Binary Heap. This property must be recursively true for all nodes in the Binary Tree.

- **Max Heap:** The key at the root must be the maximum among all keys present in the Binary Heap. This property must be recursively true for all nodes in the Binary Tree.

## Python heapq Module:
The heapq module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

- **Min Heap:** In a min heap, the smallest element is always at the root. Here's how to use heapq to create and manipulate a min heap:

 ```python
 import heapq

# Create an empty heap
min_heap = []

# Adding elements to the heap

heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 12)
print("Min Heap:", min_heap)

# Pop the smallest element
smallest = heapq.heappop(min_heap)
print("Smallest element:", smallest)
print("Min Heap after pop:", min_heap)
```

**Output:** 

 ```
Min Heap: [3, 5, 10, 12]
Smallest element: 3
Min Heap after pop: [5, 12, 10]
```

- **Max Heap:** To create a max heap, we can store negative values.

```python
import heapq

# Create an empty heap
max_heap = []

# Adding elements to the heap by pushing negative values
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -12)

# Convert back to positive values for display
print("Max Heap:", [-x for x in max_heap])

# Pop the largest element
largest = -heapq.heappop(max_heap)
print("Largest element:", largest)
print("Max Heap after pop:", [-x for x in max_heap])

```

**Output:**

```
Max Heap: [12, 10, 3, 5]
Largest element: 12
Max Heap after pop: [10, 5, 3]
```

## Heap Operations:
1. **Push Operation:** Adds an element to the heap, maintaining the heap property.  
```python
heapq.heappush(heap, item)
```
2. **Pop Operation:** Removes and returns the smallest element from the heap.  
```python
smallest = heapq.heappop(heap)
```
3. **Heapify Operation:** Converts a list into a heap in-place.  
```python
heapq.heapify(list)
```
4. **Peek Operation:** To get the smallest element without popping it (not directly available, but can be done by accessing the first element).
```python
smallest = heap[0]
```

## Example:
```python
# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [15, 77, 90, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))

```

Output:
```
The created heap is : [1, 3, 15, 77, 90]
The modified heap after push is : [1, 3, 4, 15, 77, 90]
The popped and smallest element is : 1
```

## Advantages and Disadvantages of Heaps:

## Advantages:

**Efficient:** Heap queues, implemented in Python's heapq module, offer remarkable efficiency in managing priority queues and heaps. With logarithmic time complexity for key operations, they are widely favored in various applications for their performance.

**Space-efficient:** Leveraging an array-based representation, heap queues optimize memory usage compared to node-based structures like linked lists. This design minimizes overhead, enhancing efficiency in memory management.

**Ease of Use:** Python's heap queues boast a user-friendly API, simplifying fundamental operations such as insertion, deletion, and retrieval. This simplicity contributes to rapid development and code maintenance.

**Flexibility:** Beyond their primary use in priority queues and heaps, Python's heap queues lend themselves to diverse applications. They can be adapted to implement various data structures, including binary trees, showcasing their versatility and broad utility across different domains.

## Disadvantages:

**Limited functionality:** Heap queues are primarily designed for managing priority queues and heaps, and may not be suitable for more complex data structures and algorithms.

**No random access:** Heap queues do not support random access to elements, making it difficult to access elements in the middle of the heap or modify elements that are not at the top of the heap.

**No sorting:** Heap queues do not support sorting, so if you need to sort elements in a specific order, you will need to use a different data structure or algorithm.

**Not thread-safe:** Heap queues are not thread-safe, meaning that they may not be suitable for use in multi-threaded applications where data synchronization is critical.

## Real-Life Examples of Heaps:

1. **Priority Queues:** 
Heaps are commonly used to implement priority queues, which are used in various algorithms like Dijkstra's shortest path algorithm and Prim's minimum spanning tree algorithm.

2. **Scheduling Algorithms:**
Heaps are used in job scheduling algorithms where tasks with the highest priority need to be processed first.

3. **Merge K Sorted Lists:**
Heaps can be used to efficiently merge multiple sorted lists into a single sorted list.

4. **Real-Time Event Simulation:**
Heaps are used in event-driven simulators to manage events scheduled to occur at future times.

5. **Median Finding Algorithm:**
Heaps can be used to maintain a dynamic set of numbers to find the median efficiently.

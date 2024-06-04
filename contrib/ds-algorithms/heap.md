## Introduction - What are heaps?
<p align="justify">Heap is a binary-tree based data structure that satisfies two properties -
  
- It is an almost complete binary tree.
- <p align="justify">It exhibits parent dominance property where the parent holds a constant property of either greater dominance or lesser dominance than the child nodes.

<p align="justify">Heaps are commonly used to implement priority queues where a certain element has to be removed or accessed periodically based on the property of the next smallest or next 
largest element. This can be done as the largest or the smallest element of the set of elements is always the root of the tree depending on the type of heap as discussed below. 
By removing the root and heapifying the elements again, the root holds the next smallest/largest element.

## Types of Heaps
- <p align="justify">Min Heap - Min heaps are heaps where the parent dominance property is such that the parent always exhibits lesser dominance than the child. This means that the key value of the parent will always be lesser than that of the child.
- <p align="justify">Max Heap - Max heaps are heaps where the parent dominance property is such that the parent always exhibits greater dominance than the child. This means that the key value of the parent will always be greater than that of the child.

The two types of heaps are illustrated below (left - max heap, right - min heap)

![max-min](https://github.com/Arya-Hari/learn-python/assets/84255987/61220f21-4150-4064-b930-9737cee8dd31)

## Methods of Constructing a Heap
There are two methods of constructing a heap - 
- <p align="justify">Bottom-up approach - Construct a binary tree by filling the nodes in level-order fashion. Then starting from the bottom, compare the values of the last parent node with its children and switch the parent node with any of the child nodes if the nodes are greater or smaller than the parent and the other child node (if it exists) for the case of max heap and min heap respectively. Then, move onto the next parent node and continue the process until you reach the root node and the root node holds the largest and smallest key value for the case of max heap and min heap respectively.
- <p align="justify">Top-down approach - In the top-down approach, add each node in level order fashion. But, rather than making changes once the entire binary tree is constructed, make the necessary changes while adding the node to the tree, switching between the parent and child nodes to satisfy the property of max heap and min heap, based on what you are constructing.

In the below figure, the bottom-up approach has been used to construct a max heap.

![max](https://github.com/Arya-Hari/learn-python/assets/84255987/22640a59-4700-4573-8f6b-5e4e9efe3a63)

In the below figure, top-down approach has been used to construct a min heap.

![Blank diagram (1)](https://github.com/Arya-Hari/learn-python/assets/84255987/c175ab50-a593-4e89-a70f-c3ee6d659871)

## Constructing a Heap in Python

<p align="justify">Python provides a very convenient library for constructing heaps, called the <b>heapq</b> module. It, by default, creates a min heap with the smallest element at the root. Given
below is a code snippet that illustrates how to create a heap from a list of elements using Python.

```python
# Import necessary libraries
import heapq

# Create and initialize a list
l = [83,16,57,25,43];

# Heapify it using the in-built library functions
heapq.heapify(l)

# Print the list after heapifying
print(l);

```


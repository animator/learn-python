# Data Structures: Hash Tables, Hash Sets, and Hash Maps

## Table of Contents
- [Introduction](#introduction)
- [Hash Tables](#hash-tables)
  - [Overview](#overview)
  - [Operations](#operations)
- [Hash Sets](#hash-sets)
  - [Overview](#overview-1)
  - [Operations](#operations-1)
- [Hash Maps](#hash-maps)
  - [Overview](#overview-2)
  - [Operations](#operations-2)
- [Conclusion](#conclusion)

## Introduction
This document provides an overview of three fundamental data structures in computer science: hash tables, hash sets, and hash maps. These structures are widely used for efficient data storage and retrieval operations.

## Hash Tables

### Overview
A **hash table** is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

### Operations
1. **Insertion**: Add a new key-value pair to the hash table.
2. **Deletion**: Remove a key-value pair from the hash table.
3. **Search**: Find the value associated with a given key.
4. **Update**: Modify the value associated with a given key.

**Example Code (Python):**
```python
class Node: 
	def __init__(self, key, value): 
		self.key = key 
		self.value = value 
		self.next = None


class HashTable: 
	def __init__(self, capacity): 
		self.capacity = capacity 
		self.size = 0
		self.table = [None] * capacity 

	def _hash(self, key): 
		return hash(key) % self.capacity 

	def insert(self, key, value): 
		index = self._hash(key) 

		if self.table[index] is None: 
			self.table[index] = Node(key, value) 
			self.size += 1
		else: 
			current = self.table[index] 
			while current: 
				if current.key == key: 
					current.value = value 
					return
				current = current.next
			new_node = Node(key, value) 
			new_node.next = self.table[index] 
			self.table[index] = new_node 
			self.size += 1

	def search(self, key): 
		index = self._hash(key) 

		current = self.table[index] 
		while current: 
			if current.key == key: 
				return current.value 
			current = current.next

		raise KeyError(key) 

	def remove(self, key): 
		index = self._hash(key) 

		previous = None
		current = self.table[index] 

		while current: 
			if current.key == key: 
				if previous: 
					previous.next = current.next
				else: 
					self.table[index] = current.next
				self.size -= 1
				return
			previous = current 
			current = current.next

		raise KeyError(key) 

	def __len__(self): 
		return self.size 

	def __contains__(self, key): 
		try: 
			self.search(key) 
			return True
		except KeyError: 
			return False


# Driver code 
if __name__ == '__main__': 
 
	ht = HashTable(5) 

	ht.insert("apple", 3) 
	ht.insert("banana", 2) 
	ht.insert("cherry", 5) 


	print("apple" in ht) 
	print("durian" in ht) 

	print(ht.search("banana")) 

	ht.insert("banana", 4) 
	print(ht.search("banana")) # 4 

	ht.remove("apple") 

	print(len(ht)) # 3 
```

# Insert elements
hash_table["key1"] = "value1"
hash_table["key2"] = "value2"

# Search for an element
value = hash_table.get("key1")

# Delete an element
del hash_table["key2"]

# Update an element
hash_table["key1"] = "new_value1"

## Hash Sets

### Overview
A **hash set** is a collection of unique elements. It is implemented using a hash table where each bucket can store only one element.

### Operations
1. **Insertion**: Add a new element to the set.
2. **Deletion**: Remove an element from the set.
3. **Search**: Check if an element exists in the set.
4. **Union**: Combine two sets to form a new set with elements from both.
5. **Intersection**: Find common elements between two sets.
6. **Difference**: Find elements present in one set but not in the other.

**Example Code (Python):**
```python
# Create a hash set
hash_set = set()

# Insert elements
hash_set.add("element1")
hash_set.add("element2")

# Search for an element
exists = "element1" in hash_set

# Delete an element
hash_set.remove("element2")

# Union of sets
another_set = {"element3", "element4"}
union_set = hash_set.union(another_set)

# Intersection of sets
intersection_set = hash_set.intersection(another_set)

# Difference of sets
difference_set = hash_set.difference(another_set)
```
## Hash Maps

### Overview
A **hash map** is similar to a hash table but often provides additional functionalities and more user-friendly interfaces for developers. It is a collection of key-value pairs where each key is unique.

### Operations
1. **Insertion**: Add a new key-value pair to the hash map.
2. **Deletion**: Remove a key-value pair from the hash map.
3. **Search**: Retrieve the value associated with a given key.
4. **Update**: Change the value associated with a given key.

**Example Code (Python):**
```python
# Create a hash map
hash_map = {}

# Insert elements
hash_map["key1"] = "value1"
hash_map["key2"] = "value2"

# Search for an element
value = hash_map.get("key1")

# Delete an element
del hash_map["key2"]

# Update an element
hash_map["key1"] = "new_value1"

```
## Conclusion
Hash tables, hash sets, and hash maps are powerful data structures that provide efficient means of storing and retrieving data. Understanding these structures and their operations is crucial for developing optimized algorithms and applications.
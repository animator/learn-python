# Hashing

Hashing is a technique used to uniquely identify a specific object from a group of similar objects. 
It involves transforming input data into a fixed-size value or key, typically through a hash function, which is used to index data for efficient retrieval.

## Algorithm Overview:

1. **Hash Function:** A function that converts input data into a fixed-size hash code. The hash function should distribute the keys uniformly across the hash table to minimize collisions.
2. **Hash Table:** A data structure that stores key-value pairs. The key is used to compute an index into an array where the value is stored.
3. **Handling Collisions:** When two keys hash to the same index, a collision occurs. Common methods to handle collisions include chaining and open addressing.

## Key Concepts:
  - **Hash Function:** Converts input (key) into an integer (hash code).
  - **Hash Table:** An array where the key-value pairs are stored.
  - **Collision Handling:**
       - **Chaining:** Each array index points to a list of entries that map to the same index.
       - **Open Addressing:** Finds the next available index using methods like linear probing, quadratic probing, or double hashing.

## Hashing Algorithms in Python

## Simple Hash Table with Chaining
```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

# Example usage
ht = HashTable(10)
ht.insert("apple", 1)
ht.insert("banana", 2)
print(ht.search("apple"))  # Output: 1
ht.delete("apple")
print(ht.search("apple"))  # Output: None
```

## Example with Visualization

Let's insert and search key-value pairs in the hash table.

1. Insert "apple" with value 1:
     - Compute hash: hash("apple") % 10
     - Insert into the computed index.
       
2. Insert "banana" with value 2:
     - Compute hash: hash("banana") % 10
     - Insert into the computed index.
       
3. Search for "apple":
     - Compute hash: hash("apple") % 10
     - Retrieve the value from the computed index.
       
4. Delete "apple":
     - Compute hash: hash("apple") % 10
     - Remove the key-value pair from the computed index.


## Complexity Analysis
   - **Insertion:** Average case 𝑂(1), worst case 𝑂(𝑛) in case of collisions.
   - **Search:** Average case 𝑂(1), worst case 𝑂(𝑛) in case of collisions.
   - **Deletion:** Average case 𝑂(1), worst case 𝑂(𝑛) in case of collisions.

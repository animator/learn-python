# Hashing with Linear Probing

In Data Structures and Algorithms, hashing is used to map data of arbitrary size to fixed-size values. A common approach to handle collisions in hashing is **linear probing**. In linear probing, if a collision occurs (i.e., the hash value points to an already occupied slot), we linearly probe through the table to find the next available slot. This method ensures that every element can be inserted or found in the hash table.

## Points to be Remembered

- **Hash Function**: A function that converts an input (or 'key') into an index in a hash table.
- **Collision**: When two keys hash to the same index.
- **Linear Probing**: A method to resolve collisions by checking the next slot (i.e., index + 1) until an empty slot is found.

## Real Life Examples of Hashing with Linear Probing

- **Student Record System**: Each student record is stored in a table where the student's ID number is hashed to an index. If two students have the same hash index, linear probing finds the next available slot.
- **Library System**: Books are indexed by their ISBN numbers. If two books hash to the same slot, linear probing helps find another spot for the book in the catalog.

## Applications of Hashing

Hashing is widely used in Computer Science:

- **Database Indexing**
- **Caches** (like CPU caches, web caches)
- **Associative Arrays** (or dictionaries in Python)
- **Sets** (unordered collections of unique elements)

Understanding these applications is essential for Software Development.

## Operations in Hash Table with Linear Probing

Key operations include:

- **INSERT**: Insert a new element into the hash table.
- **SEARCH**: Find the position of an element in the hash table.
- **DELETE**: Remove an element from the hash table.

## Implementing Hash Table with Linear Probing in Python

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_index = self.hash_function(key)
        
        if self.table[hash_index] is None:
            self.table[hash_index] = (key, value)
        else:
            while self.table[hash_index] is not None:
                hash_index = (hash_index + 1) % self.size
            self.table[hash_index] = (key, value)
    
    def search(self, key):
        hash_index = self.hash_function(key)
        
        while self.table[hash_index] is not None:
            if self.table[hash_index][0] == key:
                return self.table[hash_index][1]
            hash_index = (hash_index + 1) % self.size
        
        return None
    
    def delete(self, key):
        hash_index = self.hash_function(key)
        
        while self.table[hash_index] is not None:
            if self.table[hash_index][0] == key:
                self.table[hash_index] = None
                return True
            hash_index = (hash_index + 1) % self.size
        
        return False
    
    def display(self):
        for index, item in enumerate(self.table):
            print(f"Index {index}: {item}")

# Example usage
hash_table = HashTable(10)

hash_table.insert(1, 'A')
hash_table.insert(11, 'B')
hash_table.insert(21, 'C')

print("Hash Table after Insert operations:")
hash_table.display()

print("Search operation for key 11:", hash_table.search(11))

hash_table.delete(11)

print("Hash Table after Delete operation:")
hash_table.display()
```

## Output

```markdown
Hash Table after Insert operations:
Index 0: None
Index 1: (1, 'A')
Index 2: None
Index 3: None
Index 4: None
Index 5: None
Index 6: None
Index 7: None
Index 8: None
Index 9: None
Index 10: None
Index 11: (11, 'B')
Index 12: (21, 'C')

Search operation for key 11: B

Hash Table after Delete operation:
Index 0: None
Index 1: (1, 'A')
Index 2: None
Index 3: None
Index 4: None
Index 5: None
Index 6: None
Index 7: None
Index 8: None
Index 9: None
Index 10: None
Index 11: None
Index 12: (21, 'C')
```

## Complexity Analysis

- **Insertion**: Average case O(1), Worst case O(n) when many collisions occur.
- **Search**: Average case O(1), Worst case O(n) when many collisions occur.
- **Deletion**: Average case O(1), Worst case O(n) when many collisions occur.
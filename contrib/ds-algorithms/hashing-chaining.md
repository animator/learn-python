# Hashing with Chaining

In Data Structures and Algorithms, hashing is used to map data of arbitrary size to fixed-size values. A common approach to handle collisions in hashing is **chaining**. In chaining, each slot of the hash table contains a linked list, and all elements that hash to the same slot are stored in that list.

## Points to be Remembered

- **Hash Function**: A function that converts an input (or 'key') into an index in a hash table.
- **Collision**: When two keys hash to the same index.
- **Chaining**: A method to resolve collisions by maintaining a linked list for each hash table slot.

## Real Life Examples of Hashing with Chaining

- **Phone Directory**: Contacts are stored in a hash table where the contact's name is hashed to an index. If multiple names hash to the same index, they are stored in a linked list at that index.
- **Library Catalog**: Books are indexed by their titles. If multiple books have titles that hash to the same index, they are stored in a linked list at that index.

## Applications of Hashing

Hashing is widely used in Computer Science:

- **Database Indexing**
- **Caches** (like CPU caches, web caches)
- **Associative Arrays** (or dictionaries in Python)
- **Sets** (unordered collections of unique elements)

Understanding these applications is essential for Software Development.

## Operations in Hash Table with Chaining

Key operations include:

- **INSERT**: Insert a new element into the hash table.
- **SEARCH**: Find the position of an element in the hash table.
- **DELETE**: Remove an element from the hash table.

## Implementing Hash Table with Chaining in Python

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_index = self.hash_function(key)
        new_node = Node(key, value)
        
        if self.table[hash_index] is None:
            self.table[hash_index] = new_node
        else:
            current = self.table[hash_index]
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def search(self, key):
        hash_index = self.hash_function(key)
        current = self.table[hash_index]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def delete(self, key):
        hash_index = self.hash_function(key)
        current = self.table[hash_index]
        prev = None
        
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[hash_index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        
        return False
    
    def display(self):
        for index, item in enumerate(self.table):
            print(f"Index {index}:", end=" ")
            current = item
            while current is not None:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")

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
Index 1: (1, 'A') -> (11, 'B') -> (21, 'C') -> None
Index 2: None
Index 3: None
Index 4: None
Index 5: None
Index 6: None
Index 7: None
Index 8: None
Index 9: None

Search operation for key 11: B

Hash Table after Delete operation:
Index 0: None
Index 1: (1, 'A') -> (21, 'C') -> None
Index 2: None
Index 3: None
Index 4: None
Index 5: None
Index 6: None
Index 7: None
Index 8: None
Index 9: None
```

## Complexity Analysis

- **Insertion**: Average case O(1), Worst case O(n) when many elements hash to the same slot.
- **Search**: Average case O(1), Worst case O(n) when many elements hash to the same slot.
- **Deletion**: Average case O(1), Worst case O(n) when many elements hash to the same slot.
# Collision Handling Techniques for Hash Tables

When working with hash tables, collisions can occur when multiple keys map to the same slot in the table. To handle collisions effectively, we use specific techniques. Let's explore three common approaches:

## 1. Separate Chaining

- Each bucket in the hash table holds a linked list (or another data structure) to handle collisions.
- Colliding elements are stored in these data structures at the same index.
- Advantages:
  - Simple to implement.
  - Hash table never fills up; we can always add more elements to the chain.
  - Less sensitive to the hash function or load factors.
- Disadvantages:
  - Cache performance is not optimal due to linked list storage.
  - Wastage of space (unused parts of the hash table).
  - Search time can become O(n) if the chain becomes long.

##  Chaining Implemetation

Below is the code in java:

```markdown
import java.util.LinkedList;
import java.util.List;

class Hash {
    private int BUCKET; // Number of buckets
    private List<Integer>[] table; // Array of lists for chaining

    // Constructor
    public Hash(int b) {
        this.BUCKET = b;
        table = new LinkedList[b];
        for (int i = 0; i < b; i++) {
            table[i] = new LinkedList<>();
        }
    }

    // Inserts a key into the hash table
    public void insertItem(int key) {
        int index = hashFunction(key);
        table[index].add(key);
    }

    // Deletes a key from the hash table
    public void deleteItem(int key) {
        int index = hashFunction(key);
        table[index].remove((Integer) key);
    }

    // Hash function to map values to keys
    private int hashFunction(int x) {
        return x % BUCKET;
    }

    // Function to display the hash table
    public void displayHash() {
        for (int i = 0; i < BUCKET; i++) {
            System.out.print(i);
            for (int x : table[i]) {
                System.out.print(" --> " + x);
            }
            System.out.println();
        }
    }

    // Driver program
    public static void main(String[] args) {
        // Array that contains keys to be mapped
        int[] a = {16, 21, 29, 11, 9};
        int n = a.length;

        // Insert the keys into the hash table
        Hash h = new Hash(7); // 7 is the count of buckets in the hash table
        for (int i = 0; i < n; i++) {
            h.insertItem(a[i]);
        }

        // Delete 12 from the hash table
        h.deleteItem(12);

        // Display the hash table
        h.displayHash();
    }
}
```

## 2. Open Addressing

- All elements are stored directly within the hash table, without using external data structures.
- When a collision occurs, the algorithm probes for an alternative empty slot in the table.
- Advantages:
  - Better cache performance (everything stored in the same table).
  - Avoids memory overhead.
- Disadvantages:
  - Can suffer from clustering (consecutive occupied slots).
  - Degraded performance.


## Open Addressing

Open addressing is a collision resolution method used in hash tables. In open addressing, all elements are stored directly in the hash table itself. The table size must be greater than or equal to the total number of keys (note that we can increase the table size by copying old data if needed).

### Important Operations

1. **Insert(k):** Keep probing until an empty slot is found, then insert key `k`.
2. **Search(k):** Keep probing until the slot's key doesn't match `k` or an empty slot is reached.
3. **Delete(k):** Mark slots of deleted keys as "deleted." Insertion can use deleted slots, but search doesn't stop at deleted slots.

### Open Addressing Methods

1. **Linear Probing:**
   - Linearly probe for the next slot (typical gap of 1).
   - If slot `hash(x) % S` is full, try `(hash(x) + 1) % S`, `(hash(x) + 2) % S`, etc.
   - Clustering is a problem.

2. **Quadratic Probing:**
   - Look for `i^2`-th slot in the `i`-th iteration.
   - If slot `hash(x) % S` is full, try `(hash(x) + 1^2) % S`, `(hash(x) + 2^2) % S`, etc.
   - Balances cache performance and clustering.

3. **Double Hashing:**
   - Use another hash function `hash2(x)` and look for `i * hash2(x)` slot.
   - If slot `hash(x) % S` is full, try `(hash(x) + 1 * hash2(x)) % S`, `(hash(x) + 2 * hash2(x)) % S`, etc.
   - No clustering, but poor cache performance due to extra computation.



## Open Addressing Implementaion 

Below is the code in java:

```markdown
import java.util.Arrays;

class HashNode {
  int key;
  int value;

  HashNode(int key, int value) {
    this.key = key;
    this.value = value;
  }
}

public class Solution {
  private static final int capacity = 20;
  private int size = 0;

  private HashNode[] arr;
  private HashNode dummy;

  public Solution() {
    arr = new HashNode[capacity];
    dummy = new HashNode(-1, -1);
  }

  // Function to add key value pair
  public void insert(int key, int value) {
    HashNode temp = new HashNode(key, value);
    int hashIndex = key % capacity;

    while (arr[hashIndex] != null && arr[hashIndex].key != key && arr[hashIndex].key != -1) {
      hashIndex++;
      hashIndex %= capacity;
    }

    if (arr[hashIndex] == null || arr[hashIndex].key == -1) {
      size++;
    }

    arr[hashIndex] = temp;
  }

  // Function to delete a key value pair
  public boolean deleteKey(int key) {
    int hashIndex = key % capacity;

    while (arr[hashIndex] != null) {
      if (arr[hashIndex].key == key) {
        arr[hashIndex] = dummy;
        size--;
        return true;
      }
      hashIndex++;
      hashIndex %= capacity;
    }

    return false;
  }

  // Function to search the value for a given key
  public int find(int key) {
    int hashIndex = key % capacity;
    int counter = 0;

    while (arr[hashIndex] != null) {
      if (counter++ > capacity)
        break;

      if (arr[hashIndex].key == key) {
        return arr[hashIndex].value;
      }
      hashIndex++;
      hashIndex %= capacity;
    }

    return -1;
  }

  // Driver Code
  public static void main(String[] args) {
    Solution ht = new Solution();

    ht.insert(1, 23);
    ht.insert(2, 88);
    ht.insert(3, 98);
    ht.insert(4, 24);

    if (ht.find(4) != -1) {
      System.out.println("Value of Key 1 = " + ht.find(1));
    } else {
      System.out.println("Key 1 does not exist");
    }

    if (ht.deleteKey(1)) {
      System.out.println("Node value of key 1 is deleted successfully");
    } else {
      System.out.println("Key does not exist");
    }

    if (ht.find(1) != -1) {
      System.out.println("Value of Key 1 = " + ht.find(1));
    } else {
      System.out.println("Key 1 does not exist");
    }
  }
} 

```

## 3. Double Hashing

- A probing technique used in open addressing to resolve collisions.
- Utilizes a secondary hash function to calculate the interval between probes.
- Helps distribute elements more evenly, reducing clustering and improving performance compared to simpler probing techniques.

## Double Hashing Implementation

Below is the code in java:

```markdown
public class DoubleHashing {
    private int[] hashTable;
    private int capacity;
    private int size;

    // Constructor to initialize hash table
    public DoubleHashing(int capacity) {
        this.capacity = capacity;
        this.hashTable = new int[capacity];
        this.size = 0;

        // Initialize all positions as -1 indicating empty slots
        for (int i = 0; i < capacity; i++) {
            hashTable[i] = -1;
        }
    }

    // Primary hash function
    private int hash1(int key) {
        return key % capacity;
    }

    // Secondary hash function
    private int hash2(int key) {
        return 7 - (key % 7); // A prime number less than capacity
    }

    // Insert key into hash table
    public void insert(int key) {
        if (size == capacity) {
            System.out.println("Hash table is full");
            return;
        }

        int index = hash1(key);
        int stepSize = hash2(key);

        // Find the next available slot using double hashing
        while (hashTable[index] != -1 && hashTable[index] != -2) { // -2 indicates deleted slots
            index = (index + stepSize) % capacity;
        }

        hashTable[index] = key;
        size++;
    }

    // Delete key from hash table
    public void delete(int key) {
        int index = hash1(key);
        int stepSize = hash2(key);

        // Find the key to be deleted
        while (hashTable[index] != -1) {
            if (hashTable[index] == key) {
                hashTable[index] = -2; // Mark slot as deleted
                size--;
                return;
            }
            index = (index + stepSize) % capacity;
        }
        System.out.println("Key not found");
    }

    // Search for a key in the hash table
    public boolean search(int key) {
        int index = hash1(key);
        int stepSize = hash2(key);

        // Find the key
        while (hashTable[index] != -1) {
            if (hashTable[index] == key) {
                return true;
            }
            index = (index + stepSize) % capacity;
        }
        return false;
    }

    // Display the hash table
    public void display() {
        for (int i = 0; i < capacity; i++) {
            if (hashTable[i] == -1 || hashTable[i] == -2) {
                System.out.print("Empty ");
            } else {
                System.out.print(hashTable[i] + " ");
            }
        }
        System.out.println();
    }

    // Driver code
    public static void main(String[] args) {
        DoubleHashing dh = new DoubleHashing(13);

        dh.insert(78);
        dh.insert(47);
        dh.insert(98);
        dh.insert(69);
        dh.insert(63);

        dh.display();

        dh.delete(47);
        dh.display();

        if (dh.search(98)) {
            System.out.println("98 is present in hash table");
        } else {
            System.out.println("98 is not present in hash table");
        }

        if (dh.search(47)) {
            System.out.println("47 is present in hash table");
        } else {
            System.out.println("27 is not present in hash table");
        }
    }
}
```

### Comparison

- **Linear probing:** Best cache performance, easy to compute.
- **Quadratic probing:** Intermediate cache performance and clustering.
- **Double hashing:** No clustering, but requires more computation time.
# Prefix Matching 

Prefix matching is a method used in various algorithms and data structures to `check if a given string (called the prefix) matches the beginning part of another string`. 
This is commonly used in tasks like searching, autocomplete, and dictionary lookups.

Here is the Example:

```markdown
Prefix: "App"

Words List:
- "Apple"
- "Application"
- "Apply"
- "Banana"
- "Band"

Matching Words:
- "Apple"
- "Application"
- "Apply"

Explanation: All words starting with "App" are selected.
```
And `tries` excel at prefix matching, effectively locating all strings beginning with a specific prefix. Each `node` reflects the common prefix of all the strings below it.

As the previous section explains _what are the characteristics of Trie_
- Prefix Matching
- Space Efficiency
- Time Complexity

This section helps to understand _why are they the best features_

## Prefix Matching in Trie

To locate all strings with a specified prefix (Prefix Matching), we `traverse` the Trie till we reach the end of the prefix and gather all words from there.

>The primary goal of prefix matching is to `find` and `collect all` words in a trie that starts with a given prefix.

### Find Prefix

The `find_prefix` method initiates the process of prefix matching by traversing the trie structure according to the characters of the provided prefix. Here's a detailed breakdown of this method:

The method begins by setting the current node to the root of the trie, denoted as `self.root`.

1. **Traversal through the Prefix:** It iterates through each character in the prefix, starting from the first character. For each character, it computes the corresponding index in the `alphabets` array using the ASCII values.

2. **Handling Missing Prefix:** If, during traversal, the character at a particular index is not found in the `alphabets` array of the current node, it indicates that the prefix does not exist in the trie. In such cases, an empty list is returned, signifying the absence of words with the given prefix.

If the character is found, the traversal continues by updating the current node to the child node corresponding to the character.

3. **Invocation of Word Collection:** Once the entire prefix is traversed successfully, the method invokes the `_collect_all_words` function to gather all words that have the prefix as a substring, starting from the node reached after traversing the prefix.

Finally, the method returns the list of matching words obtained from the `_collect_all_words` function.

**Implementation of the `find_prefix` Method:**

```python
def find_prefix(self, prefix):
    node = self.root
    for char in prefix:
        index = ord(char) - ord('a')
        if not node.alphabets[index]:
            return []  # Prefix not found in trie
        node = node.alphabets[index]
    return self._collect_all_words(node, prefix)
```

### Collect All

The `_collect_all_words` method plays a role in gathering all words that share the specified prefix. Let's understand its functionality:

Firstly it initializes an empty list `words`, which will store the words found with the given prefix.

1. **Checking End of Word:** For the current node being traversed, if the `end_of_word` attribute is greater than 0, it indicates that a complete word exists up to this node. In such cases, the word with the current prefix is appended to the `words` list.

2. **Traversing Child Nodes:** Next, the method iterates over each child node of the current node. Since the trie typically contains characters 'a' to 'z', the loop runs from 0 to 25 (representing the ASCII values of these characters).

3. **Recursively Exploring Child Nodes:** For each non-empty child node, the method recursively calls itself, passing the child node and the updated prefix obtained by appending the corresponding character to the current prefix.

The words collected recursively from the child nodes are extended to the `words` list.

Finally, the method `returns` the list of words collected during the traversal, which includes all words that have the given prefix as a substring.

**Implementation of `_collect_all_words` Method:**

```python
def _collect_all_words(self, node, prefix):
    words = []
    if node.end_of_word > 0:
        words.append(prefix)  # Add a word with a prefix to the list
    for i in range(26):
        if node.alphabets[i]:
            char = chr(i + ord('a'))
            words.extend(self._collect_all_words(node.alphabets[i], prefix + char))
    return words
```
_______________________________________________________________________________________________________________________________________________________________

**Code to implement Prefix Matching `{ when the list & prefix is given }`:**
```python
class TrieNode:
    def __init__(self):
        self.alphabets = [None] * 26
        self.end_of_word = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.alphabets[index]:
                node.alphabets[index] = TrieNode()
            node = node.alphabets[index]
        node.end_of_word += 1

    def find_prefix(self, prefix):
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.alphabets[index]:
                return []  # Prefix not found in trie
            node = node.alphabets[index]
        return self._collect_all_words(node, prefix)

    def _collect_all_words(self, node, prefix):
        words = []
        if node.end_of_word > 0:
            words.append(prefix)  # Add word with prefix to the list
        for i in range(26):
            if node.alphabets[i]:
                char = chr(i + ord('a'))
                words.extend(self._collect_all_words(node.alphabets[i], prefix + char))
        return words

if __name__ == "__main__":
    trie = Trie()

    words = ["apple", "app", "apricot", "bat", "ball", "ban"]
    for word in words:
        trie.insert(word)

    prefix = "ap"
    matching_words = trie.find_prefix(prefix)
    print(matching_words)  # Output: ['apple', 'app', 'apricot']
```

**Code to implement Prefix Matching `{ when the list & prefix is not given }`:**

In the case of a user-inputted list & prefix, the whole code stays the same as previously; just the `main` function changes, as seen below:

```python
if __name__ == "__main__":
    trie = Trie()

    # Accepting user input for the list of words
    num_words = int(input("Enter the number of words: "))
    words = []
    for i in range(num_words):
        word = input("Enter word {}: ".format(i+1))
        words.append(word)

    # Inserting words into the trie
    for word in words:
        trie.insert(word)

    # Accepting user input for the prefix
    prefix = input("Enter the prefix to search for: ")

    # Searching for words with the specified prefix
    matching_words = trie.find_prefix(prefix)
    print("Words with prefix '{}':".format(prefix), matching_words)
```
## Space & Time Efficiency in Trie

>Before moving into a straight explanation, let's grasp it by creating prefix matching in different data structures, for example, hash tables.

### Hash Table Example

```python
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, word):
        self.table[word] = self.table.get(word, 0) + 1

    def search(self, word):
        return self.table.get(word, 0)

    def delete(self, word):
        if word in self.table:
            self.table[word] -= 1
            if self.table[word] == 0:
                del self.table[word]

    def find_prefix(self, prefix):
        return [word for word in self.table if word.startswith(prefix)]

if __name__ == "__main__":
    hash_table = HashTable()

    words = ["apple", "app", "apricot", "bat", "ball", "ban"]
    for word in words:
        hash_table.insert(word)

    prefix = "ap"
    matching_words = hash_table.find_prefix(prefix)
    print(matching_words)  # Output: ['apple', 'app', 'apricot']
```

### Time Complexity Analysis

#### Insertion:
- **Trie**: Each character of the word is added to the Trie, resulting in a time complexity of \( O(m) \), where \( m \) is the length of the word.
- **Hash Table**: Involves creating multiple keys for each prefix of the word, leading to a time complexity of \( O(m^2) \) for inserting all prefixes.

#### Search Prefix:
- **Trie**: Involves traversing the Trie for each character in the prefix and performing a depth-first search. The time complexity is \( O(m+k) \), where \( m \) is the length of the prefix and \( k \) is the number of nodes visited during the DFS.
- **Hash Table**: Retrieves the list of words with an average time complexity of \( O(1) \), but has a high space complexity due to storing all prefixes.

### Summary of Comparison

#### Trie:
- Efficient for prefix matching with \( O(m) \) time complexity for insertion and \( O(m+k) \) for prefix search.
- Trie Example:

>Consider the following words inserted into a Trie: "apple", "app", "apricot", "bat", "ball", "ban"

``` markdown
  - The word "apple" will create keys for "a", "ap", "app", "appl", "apple".
  - Similarly, "app" will create keys for "a" and "ap".
  - For "apricot", keys will be created for "a", "ap", "apr", "apri", "apric", "aprico", and "apricot".
```
>Searching for the prefix "ap" will return all words with that prefix: "apple", "app", "apricot".

#### Hash Table:
- Less efficient for prefix matching due to \( O(m^2) \) time complexity for insertion and \( O(1) \) for search, with higher space complexity.
- Hash Table Example:

>Consider the same words inserted into a Hash Table:

```python
hash_table = {"apple": 1, "app": 1, "apricot": 1, "bat": 1, "ball": 1, "ban": 1}
```

- **Insertion**:
  - Each word is inserted as a key-value pair in the hash table.

- **Search Prefix**:
  - To find all words with the prefix "ap", we need to iterate over all keys in the hash table and check if they start with "ap".

```python
matching_words = [word for word in hash_table if word.startswith("ap")]
print(matching_words)  # Output: ['apple', 'app', 'apricot']
```

>In this example, the hash table requires more time and space to store and retrieve the prefixes compared to the Trie.









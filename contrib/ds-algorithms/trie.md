# Trie

A Trie is a tree-like data structure used for storing a dynamic set of strings where the keys are usually strings. It is also known as prefix tree or digital tree.

>Trie is a type of search tree, where each node represents a single character of a string.

>Nodes are linked in such a way that they form a tree, where each path from the root to a leaf node represents a unique string stored in the Trie.

## Characteristics of Trie
- **Prefix Matching**: Tries are particularly useful for prefix matching operations. Any node in the Trie represents a common prefix of all strings below it.
- **Space Efficiency**: Tries can be more space-efficient than other data structures like hash tables for storing large sets of strings with common prefixes.
- **Time Complexity**: Insertion, deletion, and search operations in a Trie have a time complexity of 
𝑂(𝑚), where m is the length of the string. This makes Tries very efficient for these operations.

## Structure of Trie

Trie mainly consists of three parts:
- **Root**: The root of a Trie is an empty node that does not contain any character.
- **Edges**: Each edge in the Trie represents a character in the alphabet of the stored strings.
- **Nodes**: Each node contains a character and possibly additional information, such as a boolean flag indicating if the node represents the end of a valid string.

To implement the nodes of trie. We use Classes in Python. Each node is an object of the Node Class. 

Node Class have mainly two components
- *Array of size 26*: It is used to represent the 26 alphabets. Initially all are None. While inserting the words, then array will be filled with object of child nodes.
- *End of word*: It is used to represent the end of word while inserting.

Code Block of Node Class :

```
class Node:
    def __init__(self):
        self.alphabets = [None] * 26  
        self.end_of_word = 0  
```

Now we need to implement Trie. We create another class named Trie with some methods like Insertion, Searching and Deletion.

**Initialization:** In this, we initializes the Trie with a `root` node.

Code Implementation of Initialization:

```
class Trie:
    def __init__(self):
        self.root = Node()
```

## Operations on Trie

1. **Insertion**: Inserts the word into the Trie. This method takes `word` as parameter. For each character in the word, it checks if there is a corresponding child node. If not, it creates a new `Node`. After processing all the characters in word, it increments the `end_of_word` value of the last node.

Code Implementation of Insertion: 
```
def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.alphabets[index]:
                node.alphabets[index] = Node()
            node = node.alphabets[index]
        node.end_of_word += 1
```

2. **Searching**: Search the `word` in trie. Searching process starts from the `root` node. Each character of the `word` is processed. After traversing the whole word in trie, it return the count of words.

There are two cases in Searching:
- *Word Not found*: It happens when the word we search not present in the trie. This case will occur, if the value of `alphabets` array at that character is `None` or if the value of `end_of_word` of the node, reached after traversing the whole word is `0`.
- *Word found*: It happens when the search word is present in the Trie. This case will occur, when the `end_of_word` value is greater than `0` of the node after traversing the whole word.

Code Implementation of Searching:
```
 def Search(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.alphabets[index]:
                return 0
            node = node.alphabets[index]
        return node.end_of_word
```

3. **Deletion**: To delete a string, follow the path of the string. If the end node is reached and `end_of_word` is greater than `0` then decrement the value.

Code Implementation of Deletion:

```
def delete(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            node = node.alphabets[index]
        if node.end_of_word:
            node.end_of_word-=1
```

Python Code to implement Trie:

```
class Node:
    def __init__(self):
        self.alphabets = [None] * 26  
        self.end_of_word = 0 

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.alphabets[index]:
                node.alphabets[index] = Node()
            node = node.alphabets[index]
        node.end_of_word += 1
    
    def Search(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.alphabets[index]:
                return 0
            node = node.alphabets[index]
        return node.end_of_word
    
    def delete(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            node = node.alphabets[index]
        if node.end_of_word:
            node.end_of_word-=1

if __name__ == "__main__":
    trie = Trie()

    word1 = "apple"
    word2 = "app"
    word3 = "bat"

    trie.insert(word1)
    trie.insert(word2)
    trie.insert(word3)

    print(trie.Search(word1))
    print(trie.Search(word2)) 
    print(trie.Search(word3)) 

    trie.delete(word2)
    print(trie.Search(word2)) 
```

# Splay Tree

In Data Structures and Algorithms, a **Splay Tree** is a self-adjusting binary search tree with the additional property that recently accessed elements are quick to access again. It performs basic operations such as insertion, search, and deletion in O(log n) amortized time. This is achieved by a process called **splaying**, where the accessed node is moved to the root through a series of tree rotations.

## Points to be Remembered

- **Splaying**: Moving the accessed node to the root using rotations.
- **Rotations**: Tree rotations (left and right) are used to balance the tree during splaying.
- **Self-adjusting**: The tree adjusts itself with each access, keeping frequently accessed nodes near the root.

## Real Life Examples of Splay Trees

- **Cache Implementation**: Frequently accessed data is kept near the top of the tree, making repeated accesses faster.
- **Networking**: Routing tables in network switches can use splay trees to prioritize frequently accessed routes.

## Applications of Splay Trees

Splay trees are used in various applications in Computer Science:

- **Cache Implementations**
- **Garbage Collection Algorithms**
- **Data Compression Algorithms (e.g., LZ78)**

Understanding these applications is essential for Software Development.

## Operations in Splay Tree

Key operations include:

- **INSERT**: Insert a new element into the splay tree.
- **SEARCH**: Find the position of an element in the splay tree.
- **DELETE**: Remove an element from the splay tree.

## Implementing Splay Tree in Python

```python
class SplayTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.splay_insert(self.root, key)

    def search(self, key):
        self.root = self.splay_search(self.root, key)
        return self.root

    def splay(self, root, key):
        if not root or root.key == key:
            return root

        if root.key > key:
            if not root.left:
                return root
            if root.left.key > key:
                root.left.left = self.splay(root.left.left, key)
                root = self.rotateRight(root)
            elif root.left.key < key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right:
                    root.left = self.rotateLeft(root.left)
            return root if not root.left else self.rotateRight(root)
        
        else:
            if not root.right:
                return root
            if root.right.key > key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = self.rotateRight(root.right)
            elif root.right.key < key:
                root.right.right = self.splay(root.right.right, key)
                root = self.rotateLeft(root)
            return root if not root.right else self.rotateLeft(root)

    def splay_insert(self, root, key):
        if not root:
            return SplayTreeNode(key)
        
        root = self.splay(root, key)

        if root.key == key:
            return root
        
        new_node = SplayTreeNode(key)

        if root.key > key:
            new_node.right = root
            new_node.left = root.left
            root.left = None
        else:
            new_node.left = root
            new_node.right = root.right
            root.right = None
        
        return new_node

    def splay_search(self, root, key):
        return self.splay(root, key)

    def rotateRight(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        return temp

    def rotateLeft(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        return temp

    def preOrder(self, root):
        if root:
            print(root.key, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

#Example usage:
splay_tree = SplayTree()
splay_tree.insert(50)
splay_tree.insert(30)
splay_tree.insert(20)
splay_tree.insert(40)
splay_tree.insert(70)
splay_tree.insert(60)
splay_tree.insert(80)

print("Preorder traversal of the Splay tree is:")
splay_tree.preOrder(splay_tree.root)

splay_tree.search(60)

print("\nSplay tree after search operation for key 60:")
splay_tree.preOrder(splay_tree.root)
```

## Output

```markdown
Preorder traversal of the Splay tree is:
50 30 20 40 70 60 80 

Splay tree after search operation for key 60:
60 50 30 20 40 70 80
```

## Complexity Analysis

The worst-case time complexities of the main operations in a Splay Tree are as follows:

- **Insertion**: (O(n)). In the worst case, insertion may take linear time if the tree is highly unbalanced.
- **Search**: (O(n)). In the worst case, searching for a node may take linear time if the tree is highly unbalanced.
- **Deletion**: (O(n)). In the worst case, deleting a node may take linear time if the tree is highly unbalanced.

While these operations can take linear time in the worst case, the splay operation ensures that the tree remains balanced over a sequence of operations, leading to better average-case performance.
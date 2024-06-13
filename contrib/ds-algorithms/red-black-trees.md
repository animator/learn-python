# Red-Black Tree

In Data Structures and Algorithms, a **Red-Black Tree** is a self-balancing binary search tree (BST) where each node contains an extra bit for denoting the color of the node, either red or black. Ensuring the tree remains balanced, Red-Black Trees provide efficient search, insertion, and deletion operations.

## Properties of Red-Black Trees

1. **Root Property**: The root is always black.
2. **Red Property**: Red nodes cannot have red children (no two red nodes can be adjacent).
3. **Depth Property**: Every path from a node to its descendant leaves has the same number of black nodes.
4. **Leaf Property**: Every leaf (NIL node) is black.

## Real Life Examples of Red-Black Trees

- **Databases**: Red-Black Trees can be used to maintain large indexes for database tables, ensuring quick data retrieval.
- **File Systems**: Some file systems use Red-Black Trees to keep track of free and used memory blocks.

## Applications of Red-Black Trees

Red-Black Trees are used in various applications in Computer Science:

- **Database Indexing**
- **Memory Allocation**
- **Network Routing Algorithms**

Understanding these applications is essential for Software Development.

## Operations in Red-Black Tree

Key operations include:

- **INSERT**: Insert a new element into the Red-Black Tree.
- **SEARCH**: Find the position of an element in the Red-Black Tree.
- **DELETE**: Remove an element from the Red-Black Tree.

## Implementing Red-Black Tree in Python

```python
class RedBlackTreeNode:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = RedBlackTreeNode(0, color='black')
        self.root = self.TNULL

    def insert(self, key):
        node = RedBlackTreeNode(key)
        node.left = self.TNULL
        node.right = self.TNULL

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = 'red'
        self.fixInsert(node)

    def search(self, root, key):
        if root == self.TNULL or key == root.key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, key):
        node = self.search(self.root, key)
        if node == self.TNULL:
            return

        y = node
        y_original_color = y.color
        if node.left == self.TNULL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.TNULL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == 'black':
            self.fixDelete(x)

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def fixInsert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotateLeft(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotateRight(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotateRight(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotateLeft(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def fixDelete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.rotateLeft(x.parent)
                    s = x.parent.right

                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self.rotateRight(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self.rotateLeft(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.rotateRight(x.parent)
                    s = x.parent.left

                if s.right.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self.rotateLeft(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self.rotateRight(x.parent)
                    x = self.root
        x.color = 'black'

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def preOrder(self, node):
        if node != self.TNULL:
            print(node.key, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

# Example usage
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)
rb_tree.insert(15)

print("Preorder traversal of the Red-Black tree is:")
rb_tree.preOrder(rb_tree.root)
```

## Output
Preorder traversal of the Red-Black tree is:
20 10 15 30

## Complexity Analysis

- **Insertion**: O(logn). Inserting a node involves traversing the height of the tree, which is logarithmic due to the balancing property.
- **Search**: O(logn). Searching for a node involves traversing the height of the tree.
- **Deletion**: O(log⁡n). Deleting a node involves traversing and potentially rebalancing the tree, maintaining the logarithmic height.
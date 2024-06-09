# Binary Tree

A binary tree is a non-linear data structure in which each node can have atmost two children, known as the left and the right child. It is a heirarchial data structure represented in the following way:

```python
                                                 A...................Level 0
                                                / \
                                               B   C.................Level 1
                                              / \   \
                                             D   E   G...............Level 2
```

## Basic Terminologies

- **Root node:** The topmost node in a tree is the root node. The root node does not have any parent. In the above example, **A** is the root node.
- **Parent node:** The predecessor of a node is called the parent of that node. **A** is the parent of **B** and **C**, **B** is the parent of **D** and **E** and **C** is the parent of **G**.
- **Child node:** The successor of a node is called the child of that node. **B** and **C** are children of **A**, **D** and **E** are children of **B** and **G** is the right child of **C**.
- **Leaf node:** Nodes without any children are called the leaf nodes. **D**, **E** and **G** are the leaf nodes.
- **Ancestor node:** Predecessor nodes on the path from the root to that node are called ancestor nodes. **A** and **B** are the ancestors of **E**.
- **Descendant node:** Successor nodes on the path from the root to that node are called descendant nodes. **B** and **E** are descendants of **A**.
- **Sibling node:** Nodes having the same parent are called sibling nodes. **B** and **C** are sibling nodes and so are **D** and **E**.
- **Level (Depth) of a node:** Number of edges in the path from the root to that node is the level of that node. The root node is always at level 0. The depth of root node is the depth of the tree.
- **Height of a node:** Number of edges in the path from that node to the deepest leaf is the height of that node. The height of the root is the height of a tree. Height of node **A** is 2, nodes **B** and **C** is 1 and nodes **D**, **E** and **G** is 0.

## Types Of Binary Trees

- **Full Binary Tree:** A binary tree where each node has 0 or 2 children is a full binary tree.
```python
                                                 A
                                                / \
                                               B   C
                                              / \   
                                             D   E   
```
- **Complete Binary Tree:** A binary tree in which all levels are completely filled except the last level is a complete binary tree. Whenever new nodes are inserted, they are inserted from the left side.
```python
                                                  A
                                                 / \
                                                /   \
                                               B     C
                                              / \   / 
                                             D   E F   
```
- **Perfect Binary Tree:** A binary tree in which all nodes are completely filled, i.e., each node has two children is called a perfect binary tree.
```python
                                                  A
                                                 / \
                                                /   \
                                               B     C
                                              / \   / \
                                             D   E F   G
```
- **Skewed Binary Tree:** A binary tree in which each node has either 0 or 1 child is called a skewed binary tree. It is of two types - left skewed binary tree and right skewed binary tree.
```python
                           A                                             A
                            \                                           /
                             B                                         B
                              \                                       /
                               C                                     C
                     Right skewed binary tree             Left skewed binary tree
```
- **Balanced Binary Tree:** A binary tree in which the height difference between the left and right subtree is not more than one and the subtrees are also balanced is a balanced binary tree.
```python
                                                      A
                                                     / \
                                                    B   C
                                                   / \
                                                  D   E
```

## Real Life Applications Of Binary Tree

- **File Systems:** File systems employ binary trees to organize the folders and files, facilitating efficient search and access of files.
- **Decision Trees:** Decision tree, a supervised learning algorithm, utilizes binary trees, with each node representing a decision and its edges showing the possible outcomes.
- **Routing Algorithms:** In routing algorithms, binary trees are used to efficiently transfer data packets from the source to destination through a network of nodes.
- **Searching and sorting Algorithms:** Searching algorithms like binary search and sorting algorithms like heapsort heavily rely on binary trees.

## Implementation of Binary Tree

```python
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_tree:
    @staticmethod
    def insert(root, data):
        if root is None:
            return Node(data)
        q = deque()
        q.append(root)
        while q:
            temp = q.popleft()
            if temp.left is None:
                temp.left = Node(data)
                break
            else:
                q.append(temp.left)
            if temp.right is None:
                temp.right = Node(data)
                break
            else:
                q.append(temp.right)
        return root

    @staticmethod
    def inorder(root):
        if not root:
            return
        b.inorder(root.left)
        print(root.data, end=" ")
        b.inorder(root.right)
    
    @staticmethod
    def preorder(root):
        if not root:
            return
        print(root.data, end=" ")
        b.preorder(root.left)
        b.preorder(root.right)

    @staticmethod
    def postorder(root):
        if not root:
            return
        b.postorder(root.left)
        b.postorder(root.right)
        print(root.data, end=" ")

    @staticmethod
    def levelorder(root):
        if not root:
            return
        q = deque()
        q.append(root)
        while q:
            temp = q.popleft()
            print(temp.data, end=" ")
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
    
    @staticmethod
    def delete(root, value):
        q = deque()
        q.append(root)
        while q:
            temp = q.popleft()
            if temp is value:
                temp = None
                return
            if temp.right:
                if temp.right is value:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is value:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    @staticmethod
    def delete_value(root, value):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.data == value:
                return None
            else:
                return root
        x = None
        q = deque()
        q.append(root)
        temp = None
        while q:
            temp = q.popleft()
            if temp.data == value:
                x = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if x:
            y = temp.data
            x.data = y
            b.delete(root, temp)
        return root

b = Binary_tree()
root = None
root = b.insert(root, 10)
root = b.insert(root, 20)
root = b.insert(root, 30)
root = b.insert(root, 40)
root = b.insert(root, 50)
root = b.insert(root, 60)

print("Preorder traversal:", end=" ")
b.preorder(root)

print("\nInorder traversal:", end=" ")
b.inorder(root)

print("\nPostorder traversal:", end=" ")
b.postorder(root)

print("\nLevel order traversal:", end=" ")
b.levelorder(root)

root = b.delete_value(root, 20)
print("\nLevel order traversal after deletion:", end=" ")
b.levelorder(root)


'''
OUTPUT:
Preorder traversal: 10 20 40 50 30 60 
Inorder traversal: 40 20 50 10 60 30 
Postorder traversal: 40 50 20 60 30 10 
Level order traversal: 10 20 30 40 50 60 
Level order traversal after deletion: 10 60 30 40 50 
'''
```

# Binary Tree

A binary tree is a non-linear data structure in which each node can have atmost two children, known as the left and the right child.

```python
                                                 A...................Level 0
                                                / \
                                               B   C.................Level 1
                                              / \   \
                                             D   E   G...............Level 2
```

## Basic Terminologies

- **Root node:** The topmost node in a tree is the root node. The root node does not have any parent. In the example given above, **A** is the root node.
- **Parent node:** The predecessor of a node is called the parent of that node. **A** is the parent of **B** and **C**, **B** is the parent of **D** and **E** and **C** is the parent of **G**.
- **Child node:** The successor of a node is called the child of that node. **B** and **C** are children of **A**, **D** and **E** are children of **B** and **G** is the right child of **C**.
- **Leaf node:** Nodes without any children are called the leaf nodes. **D**, **E** and **G** are the leaf nodes.
- **Ancestor node:** Predecessor nodes on the path from the root to that node are called ancestor nodes. **A** and **B** are the ancestors of **E**.
- **Descendant node:** Successor nodes on the path from the root to that node are called descendant nodes. **B** and **E** are descendants of **A**.
- **Sibling node:** Nodes having the same parent are called sibling nodes. **B** and **C** are sibling nodes and so are **D** and **E**.
- **Level (Depth) of a node:** Number of edges in the path from the root to that node is the level of that node. The root node is always at level 0. The depth of root node is the depth of the tree. Nodes **D**, **E** and **G** are at level 2.
- **Height of a node:** Number of edges in the path from that node to the deepest leaf. The height of the root is the height of a tree. Height of nodes **B** and **C** are 1.

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

## Implementation of Binary Tree

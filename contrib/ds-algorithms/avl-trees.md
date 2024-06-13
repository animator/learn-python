    # AVL Tree

    In Data Structures and Algorithms, an **AVL Tree** is a self-balancing binary search tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes. It ensures that the tree remains balanced, providing efficient search, insertion, and deletion operations.

    ## Points to be Remembered

    - **Balance Factor**: The difference in heights between the left and right subtrees of a node. It should be -1, 0, or +1 for all nodes in an AVL tree.
    - **Rotations**: Tree rotations (left, right, left-right, right-left) are used to maintain the balance factor within the allowed range.

    ## Real Life Examples of AVL Trees

    - **Databases**: AVL trees can be used to maintain large indexes for database tables, ensuring quick data retrieval.
    - **File Systems**: Some file systems use AVL trees to keep track of free and used memory blocks.

    ## Applications of AVL Trees

    AVL trees are used in various applications in Computer Science:

    - **Database Indexing**
    - **Memory Allocation**
    - **Network Routing Algorithms**

    Understanding these applications is essential for Software Development.

    ## Operations in AVL Tree

    Key operations include:

    - **INSERT**: Insert a new element into the AVL tree.
    - **SEARCH**: Find the position of an element in the AVL tree.
    - **DELETE**: Remove an element from the AVL tree.

    ## Implementing AVL Tree in Python

    ```python
    class AVLTreeNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1

    class AVLTree:
        def insert(self, root, key):
            if not root:
                return AVLTreeNode(key)
            
            if key < root.key:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)

            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            balance = self.getBalance(root)

            if balance > 1 and key < root.left.key:
                return self.rotateRight(root)
            if balance < -1 and key > root.right.key:
                return self.rotateLeft(root)
            if balance > 1 and key > root.left.key:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)
            if balance < -1 and key < root.right.key:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

            return root

        def search(self, root, key):
            if not root or root.key == key:
                return root

            if key < root.key:
                return self.search(root.left, key)
            
            return self.search(root.right, key)

        def delete(self, root, key):
            if not root:
                return root

            if key < root.key:
                root.left = self.delete(root.left, key)
            elif key > root.key:
                root.right = self.delete(root.right, key)
            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp
                
                temp = self.getMinValueNode(root.right)
                root.key = temp.key
                root.right = self.delete(root.right, temp.key)

            if root is None:
                return root

            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            balance = self.getBalance(root)

            if balance > 1 and self.getBalance(root.left) >= 0:
                return self.rotateRight(root)
            if balance < -1 and self.getBalance(root.right) <= 0:
                return self.rotateLeft(root)
            if balance > 1 and self.getBalance(root.left) < 0:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)
            if balance < -1 and self.getBalance(root.right) > 0:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

            return root

        def rotateLeft(self, z):
            y = z.right
            T2 = y.left
            y.left = z
            z.right = T2
            z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
            y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
            return y

        def rotateRight(self, z):
            y = z.left
            T3 = y.right
            y.right = z
            z.left = T3
            z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
            y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
            return y

        def getHeight(self, root):
            if not root:
                return 0
            return root.height

        def getBalance(self, root):
            if not root:
                return 0
            return self.getHeight(root.left) - self.getHeight(root.right)

        def getMinValueNode(self, root):
            if root is None or root.left is None:
                return root
            return self.getMinValueNode(root.left)

        def preOrder(self, root):
            if not root:
                return
            print(root.key, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

    #Example usage
    avl_tree = AVLTree()
    root = None

    root = avl_tree.insert(root, 10)
    root = avl_tree.insert(root, 20)
    root = avl_tree.insert(root, 30)
    root = avl_tree.insert(root, 40)
    root = avl_tree.insert(root, 50)
    root = avl_tree.insert(root, 25)

    print("Preorder traversal of the AVL tree is:")
    avl_tree.preOrder(root)
    ```

    ## Output

    ```markdown
    Preorder traversal of the AVL tree is:
    30 20 10 25 40 50
    ```

    ## Complexity Analysis

    - **Insertion**: O(logn). Inserting a node involves traversing the height of the tree, which is logarithmic due to the balancing property.
    - **Search**: O(logn). Searching for a node involves traversing the height of the tree.
    - **Deletion**: O(log⁡n). Deleting a node involves traversing and potentially rebalancing the tree, maintaining the logarithmic height.
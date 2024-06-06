# Circular Linked List
In a circular linked list, the last node points back to the first node, forming a circle. This allows traversal from any node to any other node in the list.

## Creating a Circular Linked List Class
```python
class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
```

## The Node Class
The smallest unit in a linked list is the node. Here is the definition of a node:

```python
class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null 
```

## Inserting a New Node at the Beginning of a Circular Linked List
```python
def insertAtBeginning(self, new_data):
    new_node = Node(new_data)  # Create a new node
    if not self.head:
        self.head = new_node
        new_node.next = self.head
    else:
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node
```

## Inserting a New Node at the End of a Circular Linked List
```python
def insertAtEnd(self, new_data):
    new_node = Node(new_data)  # Create a new node
    if not self.head:
        self.head = new_node
        new_node.next = self.head
    else:
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
```

## Inserting a New Node at a Specific Position in a Circular Linked List
```python
def insertAtPosition(self, data, position):
    new_node = Node(data)
    if position <= 0:
        print("Position should be greater than 0")
        return
    if position == 1:
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node
        return
    current_node = self.head
    current_position = 1
    while current_node.next != self.head and current_position < position - 1:
        current_node = current_node.next
        current_position += 1
    if current_position != position - 1:
        print("Position is out of bounds")
        return
    new_node.next = current_node.next
    current_node.next = new_node
```

## Printing the Circular Linked List
```python
def printList(self):
    if not self.head:
        return
    temp = self.head  # Start from the head of the list
    while True:
        print(temp.data, end=' ')  # Print the data in the current node
        temp = temp.next  # Move to the next node
        if temp == self.head:
            break
    print()  # Ensures the output is followed by a new line
```

### Example Usage
```python
if __name__ == '__main__':
    cllist = CircularLinkedList()
    
    # Insert nodes at the beginning
    cllist.insertAtBeginning(4)  # <4>
    cllist.insertAtBeginning(3)  # <3> 4
    cllist.insertAtBeginning(2)  # <2> 3 4
    cllist.insertAtBeginning(1)  # <1> 2 3 4

    # Insert a node at the end
    cllist.insertAtEnd(10)  # 1 2 3 4 <10>
    cllist.insertAtEnd(7)   # 1 2 3 4 10 <7>

    # Insert a node at a specific position
    cllist.insertAtPosition(9, 4)  # 1 2 3 <9> 4 10 7
    cllist.insertAtPosition(56, 4) # 1 2 3 <56> 9 4 10 7

    # Print the list
    cllist.printList()
```

### Output:
```
1 2 3 56 9 4 10 7
```

## Deleting a Node from the Beginning of a Circular Linked List
```python
def deleteFromBeginning(self):
    if not self.head:
        return "The list is empty"
    if self.head.next == self.head:
        self.head = None
    else:
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next
```

## Deleting a Node from the End of a Circular Linked List
```python
def deleteFromEnd(self):
    if not self.head:
        return "The list is empty"
    if self.head.next == self.head:
        self.head = None
    else:
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head
```

## Searching in a Circular Linked List
```python
def search(self, value):
    if not self.head:
        return f"Value '{value}' not found in the list"
    current = self.head
    position = 0
    while True:
        if current.data == value:
            return f"Value '{value}' found at position {position}"
        current = current.next
        position += 1
        if current == self.head:
            break
    return f"Value '{value}' not found in the list"
```

### Example Usage with Deletion and Search
```python
if __name__ == '__main__':
    cllist = CircularLinkedList()
    
    # Insert nodes at the beginning
    cllist.insertAtBeginning(4)  # <4>
    cllist.insertAtBeginning(3)  # <3> 4
    cllist.insertAtBeginning(2)  # <2> 3 4
    cllist.insertAtBeginning(1)  # <1> 2 3 4

    # Insert a node at the end
    cllist.insertAtEnd(10)  # 1 2 3 4 <10>
    cllist.insertAtEnd(7)   # 1 2 3 4 10 <7>

    # Insert a node at a specific position
    cllist.insertAtPosition(9, 4)  # 1 2 3 <9> 4 10 7
    cllist.insertAtPosition(56, 4) # 1 2 3 <56> 9 4 10 7

    # Delete nodes
    cllist.deleteFromBeginning()  # 2 3 56 9 4 10 7
    cllist.deleteFromEnd()        # 2 3 56 9 4 10

    # Search in the list
    print(cllist.search(56))  # Output: Value '56' found at position 2
    print(cllist.search(100)) # Output: Value '100' not found in the list

    # Print the list
    cllist.printList()
```

### Output:
```
Value '56' found at position 2
Value '100' not found in the list
2 3 56 9 4 10
```

## Real-Life Uses of Circular Linked Lists
Here are a few practical applications of circular linked lists in various fields:

**Music Player**: In a music player, songs can be organized in a circular linked list, allowing the playlist to repeat indefinitely. When the last song finishes playing, the next song is the first one in the playlist, creating a continuous
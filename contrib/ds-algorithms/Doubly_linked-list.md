# Doubly Linked List

A doubly linked list is a sequence of nodes where each node contains three parts: the data, a pointer to the next node, and a pointer to the previous node. This allows traversal in both directions.

## Creating a Doubly Linked List Class
```python
class DoublyLinkedList:
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

## Inserting a New Node at the Beginning of a Doubly Linked List
```python
def insertAtBeginning(self, new_data):
    new_node = Node(new_data)  # Create a new node
    new_node.next = self.head  # Next for new node becomes the current head
    if self.head is not None:
        self.head.prev = new_node  # Update the previous head's previous pointer
    self.head = new_node  # Head now points to the new node
```

## Inserting a New Node at the End of a Doubly Linked List
```python
def insertAtEnd(self, new_data):
    new_node = Node(new_data)  # Create a new node
    if self.head is None:
        self.head = new_node  # If the list is empty, make the new node the head
        return
    last = self.head 
    while last.next:  # Traverse the list to find the last node
        last = last.next
    last.next = new_node  # Make the new node the next node of the last node
    new_node.prev = last  # Update the new node's previous pointer
```

## Inserting a New Node at a Specific Position in a Doubly Linked List
```python
def insertAtPosition(self, data, position):
    new_node = Node(data)
    if position <= 0:
        print("Position should be greater than 0")
        return
    if position == 1:
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        return
    current_node = self.head
    current_position = 1
    while current_node and current_position < position - 1:
        current_node = current_node.next
        current_position += 1
    if not current_node:
        print("Position is out of bounds")
        return
    new_node.next = current_node.next
    if current_node.next:
        current_node.next.prev = new_node
    current_node.next = new_node
    new_node.prev = current_node
```

## Printing the Doubly Linked List
```python
def printList(self):
    temp = self.head  # Start from the head of the list
    while temp:
        print(temp.data, end=' ')  # Print the data in the current node
        temp = temp.next  # Move to the next node
    print()  # Ensures the output is followed by a new line
```

### Example Usage
```python
if __name__ == '__main__':
    dllist = DoublyLinkedList()
    
    # Insert nodes at the beginning
    dllist.insertAtBeginning(4)  # <4>
    dllist.insertAtBeginning(3)  # <3> 4
    dllist.insertAtBeginning(2)  # <2> 3 4
    dllist.insertAtBeginning(1)  # <1> 2 3 4

    # Insert a node at the end
    dllist.insertAtEnd(10)  # 1 2 3 4 <10>
    dllist.insertAtEnd(7)   # 1 2 3 4 10 <7>

    # Insert a node at a specific position
    dllist.insertAtPosition(9, 4)  # 1 2 3 <9> 4 10 7
    dllist.insertAtPosition(56, 4) # 1 2 3 <56> 9 4 10 7

    # Print the list
    dllist.printList()
```
### Output:
```
1 2 3 56 9 4 10 7
```
## Deleting a Node from the Beginning of a Doubly Linked List
```python
def deleteFromBeginning(self):
    if self.head is None:
        return "The list is empty"  # If the list is empty, return this string
    self.head = self.head.next  # Remove the head by making the next node the new head
    if self.head:
        self.head.prev = None  # Update the new head's previous pointer
```

## Deleting a Node from the End of a Doubly Linked List
```python
def deleteFromEnd(self):
    if self.head is None:
        return "The list is empty" 
    if self.head.next is None:
        self.head = None  # If there's only one node, remove the head by making it None
        return
    last = self.head
    while last.next:
        last = last.next
    last.prev.next = None  # Remove the last node by updating the second-last node's next pointer
```

## Searching in a Doubly Linked List
```python
def search(self, value):
    current = self.head  # Start with the head of the list
    position = 0  # Counter to keep track of the position
    while current:  # Traverse the list
        if current.data == value:  # Compare the list's data to the search value
            return f"Value '{value}' found at position {position}"  # Return the position if a match is found
        current = current.next
        position += 1
    return f"Value '{value}' not found in the list"  # Value not found
```

### Example Usage with Deletion and Search
```python
if __name__ == '__main__':
    dllist = DoublyLinkedList()
    
    # Insert nodes at the beginning
    dllist.insertAtBeginning(4)  # <4>
    dllist.insertAtBeginning(3)  # <3> 4
    dllist.insertAtBeginning(2)  # <2> 3 4
    dllist.insertAtBeginning(1)  # <1> 2 3 4

    # Insert a node at the end
    dllist.insertAtEnd(10)  # 1 2 3 4 <10>
    dllist.insertAtEnd(7)   # 1 2 3 4 10 <7>

    # Insert a node at a specific position
    dllist.insertAtPosition(9, 4)  # 1 2 3 <9> 4 10 7
    dllist.insertAtPosition(56, 4) # 1 2 3 <56> 9 4 10 7

    # Delete nodes
    dllist.deleteFromBeginning()  # 2 3 56 9 4 10 7
    dllist.deleteFromEnd()        # 2 3 56 9 4 10

    # Search in the list
    print(dllist.search(56))  # Output: Value '56' found at position 2
    print(dllist.search(100)) # Output: Value '100' not found in the list

    # Print the list
    dllist.printList()
```
### Output:
```
Value '56' found at position 2
Value '100' not found in the list
2 3 56 9 4 10
```

## Real-Life Uses of Doubly Linked Lists

Here are a few practical applications of doubly linked lists in various fields:

**Music Player**: In a music player, songs are often linked to the previous and next tracks, allowing seamless navigation between songs. This is akin to a doubly linked list where each song node points to both the previous and next songs, enhancing the flexibility of song selection.

**Browser History**: Web browsers use doubly linked lists to manage the history of visited web pages. Each page is a node, and you can move forward and backward through the history using the previous and next pointers.

**Task Scheduling**: Operating systems use doubly linked lists to manage task scheduling. Each process waiting to be executed is represented as a node, with pointers to the previous and next processes, enabling efficient management and execution of tasks.

**Text Editors**: Text editors use doubly linked lists to manage the sequence of characters or lines. This allows for efficient insertion and deletion of text, as the pointers can be easily updated to reflect changes.

These examples illustrate how doubly linked lists provide a flexible, dynamic data structure that can be adapted to a wide range of practical applications, making them a valuable tool in both software development and real-world problem-solving.







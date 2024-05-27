# Linked List Data Structure

Link list is a linear data Structure which can be defined as collection of objects called nodes that are randomly stored in the memory.
A node contains two types of metadata i.e. data stored at that particular address and the pointer which contains the address of the next node in the memory. 

The last element in a linked list features a null pointer.

## Why use linked list over array?

From the beginning, we are using array data structure to organize the group of elements that are stored individually in the memory. 
However, there are some advantage and disadvantage of array which should be known to decide which data structure will used throughout the program.

limitations

1. Before an array can be utilized in a program, its size must be established in advance.
2. Expanding an array's size is a lengthy process and is almost impossible to achieve during runtime.
3. Array elements must be stored in contiguous memory locations. To insert an element, all subsequent elements must be shifted

So we introduce a new data structure to overcome these limitations.

Linked list is used because,
1. Dynamic Memory Management: Linked lists allocate memory dynamically, meaning nodes can be located anywhere in memory and are connected through pointers, rather than being stored contiguously.
2. Adaptive Sizing: There is no need to predefine the size of a linked list. It can expand or contract during runtime, adapting to the program's requirements within the constraints of the available memory.

Let's code something

The smallest Unit: Node

```python
    class Node:
        def __init__(self, data):
            self.data = data  # Assigns the given data to the node
            self.next = None  # Initialize the next attribute to null 
```

Now, we will see the types of linked list.
 
There are mainly four types of linked list,
1. Singly Link list
2. Doubly link list 
3. Circular link list
4. Doubly circular link list


## 1. Singly linked list.

Simply think it is a chain of nodes in which each node remember(contains) the addresses of it next node.

### Creating a linked list class
```python
    class LinkedList:
        def __init__(self):
            self.head = None  # Initialize head as None
```

### Inserting a new node at the beginning of a linked list

```python
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node
```

### Inserting a new node at the end of a linked list

```python    
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node
```
### Inserting a new node at the middle of a linked list 

```python
    def insertAtPosition(self, data, position):
        new_node = Node(data)
        if position <= 0: #check if position is valid or not
            print("Position should be greater than 0")
            return
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_position = 1
        while current_node and current_position < position - 1:   #Iterating to behind of the postion.
            current_node = current_node.next
            current_position += 1
        if not current_node:            #Check if Position is out of bound or not 
            print("Position is out of bounds")
            return
        new_node.next = current_node.next  #connect the intermediate node
        current_node.next = new_node
```
### Printing the Linked list 

```python
    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line
```

Lets complete the code and create a linked list.

Connect all the code.

```python
    if __name__ == '__main__':
        llist = LinkedList()
        
        # Insert words at the beginning
        llist.insertAtBeginning(4) # <4>
        llist.insertAtBeginning(3) # <3> 4
        llist.insertAtBeginning(2) # <2> 3 4
        llist.insertAtBeginning(1) # <1> 2 3 4
    
        # Insert a word at the end
        llist.insertAtEnd(10)  # 1 2 3 4 <10>
        llist.insertAtEnd(7)   # 1 2 3 4 10 <7>
    
        #Insert at a random position 
        llist.insertAtPosition(9,4)  ## 1 2 3 <9> 4 10 7
        # Print the list
        llist.printList()
```    
    
## output:
1 2 3 9 4 10 7


### Deleting a node from the beginning of a linked list
check the list is empty otherwise shift the head to next node.
```python
    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty" # If the list is empty, return this string
        self.head = self.head.next  # Otherwise, remove the head by making the next node the new head
```
### Deleting a node from the end of a linked list

```python
    def deleteFromEnd(self):
        if self.head is None:
            return "The list is empty" 
        if self.head.next is None:
            self.head = None  # If there's only one node, remove the head by making it None
            return
        temp = self.head
        while temp.next.next:  # Otherwise, go to the second-last node
            temp = temp.next
        temp.next = None  # Remove the last node by setting the next pointer of the second-last node to None
```


### Search in a linked list 
```python
    def search(self, value):
        current = self.head  # Start with the head of the list
        position = 0  # Counter to keep track of the position
        while current: # Traverse the list
            if current.data == value: # Compare the list's data to the search value
                return f"Value '{value}' found at position {position}" # Print the value if a match is found
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list" 
```

```python
    if __name__ == '__main__':
        llist = LinkedList()
        
        # Insert words at the beginning
        llist.insertAtBeginning(4) # <4>
        llist.insertAtBeginning(3) # <3> 4
        llist.insertAtBeginning(2) # <2> 3 4
        llist.insertAtBeginning(1) # <1> 2 3 4
    
        # Insert a word at the end
        llist.insertAtEnd(10)  # 1 2 3 4 <10>
        llist.insertAtEnd(7)   # 1 2 3 4 10 <7>
    
        #Insert at a random position 
        llist.insertAtPosition(9,4)  # 1 2 3 <9> 4 10 7
        llist.insertAtPositon(56,4)  # 1 2 3 <56> 9 4 10 7

        #delete at the beginning 
        llist.deleteFromBeginning()  # 2 3 56 9 4 10 7

        #delete at the end
        llist.deleteFromEnd()  # 2 3 56 9 4 10
        # Print the list
        llist.printList()
``` 
## Output:

2 3 56 9 4 10 



## Real Life uses of Linked List


Here are a few practical applications of linked lists in various fields:

1. **Music Player**: In a music player, songs are often linked to the previous and next tracks. This allows for seamless navigation between songs, enabling you to play tracks either from the beginning or the end of the playlist. This is akin to a doubly linked list where each song node points to both the previous and the next song, enhancing the flexibility of song selection.

2. **GPS Navigation Systems**: Linked lists can be highly effective for managing lists of locations and routes in GPS navigation systems. Each location or waypoint can be represented as a node, making it easy to add or remove destinations and to navigate smoothly from one location to another. This is similar to how you might plan a road trip, plotting stops along the way in a flexible, dynamic manner.

3. **Task Scheduling**: Operating systems utilize linked lists to manage task scheduling. Each process waiting to be executed is represented as a node in a linked list. This organization allows the system to efficiently keep track of which processes need to be run, enabling fair and systematic scheduling of tasks. Think of it like a to-do list where each task is a node, and the system executes tasks in a structured order.

4. **Speech Recognition**: Speech recognition software uses linked lists to represent possible phonetic pronunciations of words. Each potential pronunciation is a node, allowing the software to dynamically explore different pronunciation paths as it processes spoken input. This method helps in accurately recognizing and understanding speech by considering multiple possibilities in a flexible manner, much like evaluating various potential meanings in a conversation.

These examples illustrate how linked lists provide a flexible, dynamic data structure that can be adapted to a wide range of practical applications, making them a valuable tool in both software development and real-world problem-solving.

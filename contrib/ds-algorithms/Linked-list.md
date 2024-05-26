# Linked List Data Structure

Link list is a linear data Structure which can be defined as collection of objects called nodes that are randomly stored in the memory.
A node contains two types of metadata i.e. data stored at that particular address and the pointer which contains the address of the next node in the memory. 
The last node of the list contains pointer to the null.

## Why use linked list over array?

From the beginning, we are using array data structure to organize the group of elements that are stored individually in the memory. 
However, there are some advantage and disadvantage of array which should be known to decide which data structure will used throughout the program.

limitations

1. The size of array must be known in advance before using it in the program.
2. Increasing size of the array is a time taking process. It is almost impossible to expand the size of the array at run time.
3. All the elements in the array need to be contiguously stored in the memory. Inserting any element in the array needs shifting of all its predecessors.

So we introduce a new data structure to overcome these limitations.

Linked list is used because,
1. It allocates the memory dynamically. All the nodes of linked list are non-contiguously stored in the memory and linked together with the help of pointers.
2. Sizing is no longer a problem since we do not need to define its size at the time of declaration. List grows as per the program's demand and limited to the available memory space.

Let's code something

The smallest Unit: Node

    class Node:
        def __init__(self, data):
            self.data = data  # Assigns the given data to the node
            self.next = None  # Initialize the next attribute to null 

Now, we will see the types of linked list.
 
There are mainly four types of linked list,
1. Singly Link list
2. Doubly link list 
3. Circular link list
4. Doubly circular link list


## 1. Singly linked list.

Simply think it is a chain of nodes in which each node remember(contains) the addresses of it next node.

### Creating a linked list class

    class LinkedList:
        def __init__(self):
            self.head = None  # Initialize head as None

### Inserting a new node at the beginning of a linked list

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node

### Inserting a new node at the end of a linked list

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node

### Inserting a new node at the middle of a linked list 

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

### Printing the Linked list 

    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line


Lets complete the code and create a linked list.

Connect all the code.

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
    
    
## output:
1 2 3 9 4 10 7


### Deleting a node from the beginning of a linked list
check the list is empty otherwise shift the head to next node.

    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty" # If the list is empty, return this string
        self.head = self.head.next  # Otherwise, remove the head by making the next node the new head

### Deleting a node from the end of a linked list

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


### Search in a linked list 

    def search(self, value):
        current = self.head  # Start with the head of the list
        position = 0  # Counter to keep track of the position
        while current: # Traverse the list
            if current.data == value: # Compare the list's data to the search value
                return f"Value '{value}' found at position {position}" # Print the value if a match is found
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list" 
    


















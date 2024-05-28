# Queue

A queue is a linear data structure that follows the **First In, First Out (FIFO)** principle where the first element inserted is the first one to be removed.

In a queue, insertion is done at the end, called the **rear** and deletion is done from the beginning called the **front**.

The functioning of a queue is similar to a group of people standing in a line: new individuals join at the rear of the line, and those who have been waiting the longest leave from the front.

## Real-Life Applications of Queue

- **Operating Systems:** OS use queue for scheduling task. For example, OS maintains a ready queue, having processes that are ready to be executed and are  waiting for CPU time.
- **Networking Devices:** Queues are used for packet management in networking devices such as routers and switches. They use queues to temporaily store packets if the outgoing links are too busy.
- **Printer Queues:** Queues are used to manage the order of printing jobs. As the jobs are submitted, they are added to the queue. The first added job is printed first, the second job is printed second and so on.
- **Breadth First Search Algorithm:** The BFS algorithm is used for level-by-level traversal of a graph. It starts at a particular node, adds its neighbour to the queue and then visits each neighbour.

## Basic Operations in a Queue

- **Enqueue:** Inserting an element at the rear end of a queue
- **Dequeue:** Deleting at element from the front end of a queue
- **Peek:** Displaying the element at the front
- **isFull:** Checking if the queue is full
- **isEmpty:** Checking if the queue is empty

## Implementation of a Queue

There are two ways to implement a queue:

- Array Implementation
- Linked List Implementation

### Array Implementation

When a queue is implemented using an array, the maximum size of the array is declared first. A queue cannot hold more elements than this maximum size. Since the size of an array, once declared, cannot be changed, it is common practice to declare an array of large size.

**Code**
```python
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = self.rear = -1

    # Inserting an element in the queue    
    def enqueue(self, item):
        if self.rear==self.size-1:
            print("Queue Overflow")
            return
        if self.front==-1:
            self.front=0
        self.rear+=1
        self.queue[self.rear] = item

    # Deleting an element in the queue    
    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
            return None
        ele = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            for i in range(self.front, self.rear):
                self.queue[i] = self.queue[i + 1]
            self.rear -= 1
        return ele

    # Displaying the front element in the queue    
    def peek(self):
        if self.front == -1:
            print("Queue Underflow")
            return None
        return self.queue[self.front]

    # Checking if the queue is full  
    def isFull(self):
        return self.rear == self.size-1

    # Cheking if the queue is empty    
    def isEmpty(self):
        return self.front==-1

    # Printing the queue  
    def display(self):
        if self.front == -1:
            print("Queue Underflow")
            return
        else:
            for i in range(0, self.rear+1):
                print(self.queue[i], end="--")
            print("None")
            
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Original queue: ", end="")
q.display()
print("Is the queue full?", q.isFull())
print("Removed element:", q.dequeue())
print("Queue after removal: ", end="")
q.display()
print("Front element:", q.peek())
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print("Is the queue empty?", q.isEmpty())


'''
OUTPUT:
Original queue: 1--2--3--4--5--None
Is the queue full? True
Removed element: 1
Queue after removal: 2--3--4--5--None
Front element: 2
Is the queue empty? True
'''
```

**Detailed Explanation Of The Code:**

- **class Queue:** Defines the class `Queue`. It represents the queue data structure and manages all queue operations.

- **def __init__(self, size):** Constructor to the `Queue` class. It is called automatically when an instance of the class is created. It initializes the attributes of the object. It takes two parameters, `self` (an instance of the `Queue` class) and `size` (maximum size of the queue).
    - **self.size = size** Assigns value of parameter `size` to attribute `size`. This attribute stores the maximum number of items a queue can hold.
    - **self.queue = [None]\*size** Assigns the `queue` attribute with a list of `None` values with length equal to `size`.
    - **self.front = self.rear = -1** Initialize two attributes, `front` and `rear` and sets both of them to -1. `front` is used to track the index of the front element in a queue. `rear` is used to track the index of the rear (last) element of the queue. If both of them are set to -1. then it means that the queue is empty.

- **def enqueue(self, item):** Defines the `enqueue()` method which inserts a new element at the end (rear) of the queue. It takes two parameters - `self` (an instance of the `Queue` class) and `item` (the element to be inserted.)
    - **if self.rear==self.size-1:** Checks if the queue is full
        - **print("Queue Overflow")** Since there is no space for further insertion, prints `Queue Overflow` 
        - **return** Stops further execution as the queue is full.
    - **if self.front==-1:** This condition will be `True` only when adding the first element to the queue.
        - **self.front=0** Increments front by 1 to indicate the queue now has an element at the front.
    - **self.rear+=1** Increments rear by 1 to make room for the new element to be added.
    - **self.queue[self.rear] = item** Places the `item` at the index indicated by `rear`.

- **def dequeue(self):** Defines the `dequeue()` method which removes the front element of the queue. It takes one parameter, `self` (an instance of the `Queue` class).
    - **if self.front == -1:** Checks if the queue is empty
        - **print("Queue Underflow")** Prints Queue Underflow to indicate queue is empty and there are no items to be removed
        - **return None** Returns `None` as there is no need for further execution
    - **ele = self.queue[self.front]** Assigns first item of queue to variable `ele`
    - **if self.front == self.rear:** Checks if the queue has only one item
        - **self.front = self.rear = -1** If only one item is present in queue, both `front` and `rear` are set to -1 to indicate that the queue now empty after removal of the only item.
    - **else:** This block is executed of the queue has more than one items.
        - **for i in range(self.front, self.rear):** Starts a `for` loop from the `front` to the `rear` element of the queue
            - **self.queue[i] = self.queue[i + 1]** Moves each item in the queue one position to the left, effectively removing the front item
        - **self.rear -= 1** Decrements `rear` index by 1 to reflect the removal of the front item
    - **return ele** Finally, this method returns the item that was removed from the front of the queue, stored in `ele`.

- **def peek(self):** Defines a method `peek()` which retrives the front element of the queue without removing it.
    - **if self.front == -1:** Checks if the queue is empty
        - **print("Queue Underflow")** Prints `Queue Underflow` as the queue is empty
        - **return None** Return `None` as there are no elements in the queue
    - **return self.queue[self.front]** Returns the front element of the queue without removing it.

- **def isFull(self):** Defines a method `isFull()` which checks whether the queue is full.
    - **return self.rear == self.size-1** Checks if `rear` is equal to `size-1`. If true, then it means queue is full and there is no space for a new item. Returns `True` if queue is full, otherwise `False`.

- **def isEmpty(self):** Defines a method `isEmpty()` which checks if the queue is empty.
    - **return self.front==-1** Checks if `front` is equal to -1. If true, then it means that the queue does not have any elements. Returns `True` if the queue is empty, otherwise `False`.

- **def display(self):** Defines the `display()` method, which prints the elements in the queue.
    - **if self.front == -1:** Checks whether the queue is empty
        - **print("Queue Underflow")** Prints `Queue Underflow` to indicate there are no elements in the queue
        - **return** As there is no elements to display, the method returns early.
    - **else:** Executed if the queue is not empty
        - **for i in range(0, self.rear+1):** Runs a `for` loop from 0 (first element index) to `rear` (last element index) in the queue.
            - **print(self.queue[i], end="--")** Prints the ith element of the queue followed by "--"
        - **print("None")** Prints `None` to signify the end of queue


### Linked List Implementation

While using a linked list to implement a queue, there is no need to define a maximum size because linked lists are dynamic in nature. They can increase or decrease their size as per requirement.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None

    # Inserting an element in the queue    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # Deleting the an element in the queue        
    def dequeue(self):
        if self.head is None:
            print("Queue Underflow")
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    
    # Displaying the front element of the queue
    def peek(self):
        if self.head is None:
            print("Queue Underflow")
            return None
        return self.head.data

    # Checking if the queue is empty   
    def isEmpty(self):
        return self.head is None

    # Displaying the entire queue        
    def display(self):
        if self.head is None:
            print("Queue Underflow")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end="->")
                temp = temp.next
            print("None")
            
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Original Queue: ", end="")
q.display()
print("Removed element:", q.dequeue())
print("Queue after removal: ", end="")
q.display()
print("Front Element:", q.peek())
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print("Is the queue empty?", q.isEmpty())


'''
OUTPUT:
Original Queue: 1->2->3->4->5->None
Removed element: 1
Queue after removal: 2->3->4->5->None
Front Element: 2
Is the queue empty? True
'''
```

**Detailed Explanation Of The Code:**

- **class Node:** Defines a class `Node` which is used to create the nodes of the linked list
    - **def __init__(self, data):** Constructor to class `Node`. It is automatically called whenever an instance of the class is created. It takes two parameter - `self` (current instance of `Node` class) and `data` (the value to be stored in a node)
        - **self.data = data** Assigns value of `data` parameter to `data` attribute. 
        - **self.next = None** `next` attribute is used to store the address of the next node in a linked list. On creating a node, `next` is assigned `None` to indicate that it is not pointing to any node.

- **class Queue:** Defines the class `Queue`. It is used to implement the queue data structure.
    - **def __init__(self):** Constructor to class `Queue` having only one parameter, self (an instance of class `Queue`)
        - **self.head = None** Declares an instance variable `head` and assigns `None` to it. This means that whenever a queue is newly created, it starts off empty with no elements in it.

- **def enqueue(self, data):** Defines the `enqueue()` method which inserts an element at the rear end of the queue. It takes two parameter, `self` (an instance of the `Queue` class) and `data` (the value to be assigned to the node)
    - **new_node = Node(data)** A new node is created with the provided `data`
    - **if self.head is None:** Checks whether `head` is `None`
        - **self.head = new_node** If the condition is `True`, then the queue is empty. Hence, address of the new node is set as the `head` of the queue.
    - **else:** Executed when the `if` block is `False`
        -  **temp = self.head** Address of the first node is assigned to a variable `temp`
        - **while temp.next is not None:** The `while` loop is used to traverse to the end of the queue.
            - **temp = temp.next** The `temp` variable is moved forward node by node. This continue until the `next` attribute becomes `None`.
        - **temp.next = new_node** Address of the new node is assigned to the `next` attribute of the last node, thus creating a link between them.

- **def dequeue(self):** Defines the dequeue() method which deletes the front element of the queue. It takes one parameter, self (an instance of the `Queue` class)
    - **if self.head is None:** Checks if the queue is empty
        - **print("Queue Underflow")** If the condition is `True`, then prints `Queue Underflow`
        - **return None** Returns `None` as there are no elements in the queue
    - **else:** Executed when queue is not empty
        - **data = self.head.data** Stores the value of the front node in a variable `data`
        - **self.head = self.head.next** Assigns the address of second node to `head`, effectively removing the link between `head` and front item.
        - **return data** Returns the item stored that was removed from the queue, stored in `data`

- **def peek(self):** Defines a method `peek()` which displays the front element without removing it.
    - **if self.head is None:** Checks if the queue is empty
        - **print("Queue Underflow")** Prints `Queue Underflow` to show there are no elements in the queue.
        - **return None** Returns `None` as there are no elements to return
    - **return self.head.data** If the queue is not empty, then returns the data of the front node.


- **def isEmpty(self):** Defines the `isEmpty()` method which checks if the queue is empty or not.
    - **return self.head is None** If `head` is equal to `None`, then it means that the queue is empty. Hence, if the condition holds, the function returns `True`, otherwise `False`.


- **def display(self):** Defines the `display()` method which prints all the elements of the queue.
    - **if self.head is None:** Checks if the `head` is `None`
        - **print("Queue Underflow")** Prints `Queue Underflow` as the queue has no elements.
        - **return** Returns early as there is no point in further execution
    - **else:** Executed when the `if` block is `False`
        - **temp = self.head** Assigns the address the front node to variable `temp`
        - **while temp is not None:** Starts a `while` loop that runs until the address stored in `temp` is `None`.
            - **print(temp.data, end="->")** Prints the value stored at the node pointed to by `temp`
            - **temp = temp.next** Move the `temp` variable forward to point at the next node
        - **print("None")** Prints `None` to signify the end of the queue

## Complexity Analysis

Below is the table of time and space complexities of various queue operations using array:

| Method       | Time Complexity | Space Complexity |
|:------------:|:------------:|:------------:|
| `enqueue()`    |  O(1)  |  O(1)  |
| `dequeue()`    |  O(n)  |  O(1)  |
| `peek()`       |  O(1)  |  O(1)  |
| `isFull()`     |  O(1)  |  O(1)  |
| `isEmpty()`    |  O(1)  |  O(1)  |
| `display()`    |  O(n)  |  O(1)  |


This table given below shows the time and space complexities of various queue operations using linked list:

| Method     | Time Complexity | Space Complexity |
|:------------:|:------------:|:------------:|
| `enqueue()`  | O(n) | O(1)  |
| `dequeue()`  | O(n) | O(1)  |
| `peek()`     | O(1) | O(1)  |
| `isEmpty()`  | O(1) | O(1)  |
| `display()`  | O(n) | O(1)  |


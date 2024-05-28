# Queue

A queue is a linear data structure that follows the **First In, First Out (FIFO)** principle where the first element inserted is the first one to be removed.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>Front</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">4</div>
</div>
<div>3</div>
<div>Rear</div>
</div>

<svg class="arrow" width="100" height="50">
<line x1="0" y1="14" x2="100" y2="14" style="stroke:black;stroke-width:2" />
<polygon points="0,14 10,9 10,19" style="fill:black;"/>
<text x="50" y="10" text-anchor="middle" fill="black">Enqueue</text>
</svg>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">5</div>
</div>
<div></div>
</div>
</div>
<p>Inserting a New Element</p>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>Front</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">5</div>
</div>
<div>4</div>
<div>Rear</div>
</div>
</div>
<p>After Inserting the Element</p>
</div>
</div>

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

**Example 1:** Suppose the size of queue 5 and it is completely filled with elements.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>Front</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">5</div>
</div>
<div>4</div>
<div>Rear</div>
</div>
</div>
</div><br>

In this case, there is no space for more elements to be inserted. Hence, the function prints `Queue Overflow` and returns.

**Example 2:** If a new element is being inserted in an empty queue.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">1</div>
</div>
<div>0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
<div>front=-1</div>
<div>rear=-1</div>
</div><br>

First `front` and `rear` are incremented by 1. 

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">1</div>
</div>
<div>0</div>
<div>front=0</div>
<div>rear=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

Then the new item is inserted. Let the new item be 1.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
<div>rear=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>


**Example 3:** Suppose there is space in the queue for insertion of new element.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
<div>rear=2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

Let the new element be 4. In this scenario, the rear is incremented by 1 to point to the next empty space.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
<div>rear=3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

Then the new element, i.e. 4 is inserted.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>3</div>
<div>rear=3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

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

**Example 1:** If the queue is completely empty,

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">1</div>
</div>
<div>0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
<div>front=-1</div>
<div>rear=-1</div>
</div><br>

Since there are no elements to remove, the function prints `Queue Underflow` and returns.

**Example 2:** When the queue has some elements in it,

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>3</div>
<div>rear=3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

The front element is stored in a variable `ele`.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>3</div>
<div>rear=3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>ele</div>
<div>(variable)</div>
</div>
</div>
</div>
</div><br>

Then all items in the queue, except the front element are shifted to the left.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
<div>rear=3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>ele</div>
<div>(variable)</div>
</div>
</div>
</div>
</div><br>

Finally, the `rear` is decremented by 1 and the value stored in variable `ele` is returned. 

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>2</div>
<div>rear=2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>ele</div>
<div>(variable)</div>
</div>
</div>
</div>
</div><br>

**Example 3:** When the queue has only one element in it.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
<div>rear=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div>

The front item is stored in a variable `ele`.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
<div>rear=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>ele</div>
<div>(variable)</div>
<div style="color: white;">a</div>
</div>
</div>
</div>
</div><br>

Then the `front` and `rear` are set to -1.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
<p>front=-1, rear=-1</p>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>ele</div>
<div>(variable)</div>
<div style="color: white;">a</div>
</div>
</div>
</div>
</div><br>

**NOTE:** Here, the element is not phyisically removed from the queue. Instead:
- The values of `front` and `rear` are set to -1 to indicate the queue is empty. This simulates the removal of the element without actually removing it from the queue. 
- If a new item is inserted after this, `front` and `rear` are incremented by 1, and the corresponding array cell (`self.queue[front]`) is reassigned with the new item.
- Similarly, in **Example 2**, the front array cell was reassigned with a new value, i.e., the second item, effectively managing the queue state without physically removing elements.

<br>

- **def peek(self):** Defines a method `peek()` which retrives the front element of the queue without removing it.
    - **if self.front == -1:** Checks if the queue is empty
        - **print("Queue Underflow")** Prints `Queue Underflow` as the queue is empty
        - **return None** Return `None` as there are no elements in the queue
    - **return self.queue[self.front]** Returns the front element of the queue without removing it.

**Example 1:** If the queue is completely empty,

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">1</div>
</div>
<div>0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
<div>front=-1</div>
<div>rear=-1</div>
</div><br>

Since there is no front item, the function prints `Queue Underflow` and returns.

**Example 2:** When the queue has some elements in it,

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>3</div>
<div>rear=3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

Here, the function returns the front element i.e., 1.

- **def isFull(self):** Defines a method `isFull()` which checks whether the queue is full.
    - **return self.rear == self.size-1** Checks if `rear` is equal to `size-1`. If true, then it means queue is full and there is no space for a new item. Returns `True` if queue is full, otherwise `False`.

**Example 1:** Suppose the size of queue 5 and it is completely filled with elements.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">5</div>
</div>
<div>4</div>
<div>rear=4</div>
</div>
</div>
</div><br>

The function returns `True` only if the queue is like the one shown above. 

**Example 2:** In all other cases, like the ones shown below, the function returns `False`.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">1</div>
</div>
<div>0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
<div>front=-1, rear=-1</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
<div>rear=2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5">5</div>
</div>
<div>4</div>
</div>
</div>
</div>
</div><br>

- **def isEmpty(self):** Defines a method `isEmpty()` which checks if the queue is empty.
    - **return self.front==-1** Checks if `front` is equal to -1. If true, then it means that the queue does not have any elements. Returns `True` if the queue is empty, otherwise `False`.

**Example 1:** If the queue is completely empty, then the function returns `True`.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">1</div>
</div>
<div>0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
<div>front=-1, rear=-1</div>
</div>
</div>
</div><br>

**Example 2:** In all other cases like the ones shown below, the function returns `False`.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
<div>rear=2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5">5</div>
</div>
<div>4</div>
</div>
</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">5</div>
</div>
<div>4</div>
<div>rear=4</div>
</div>
</div>
</div>
</div><br>

- **def display(self):** Defines the `display()` method, which prints the elements in the queue.
    - **if self.front == -1:** Checks whether the queue is empty
        - **print("Queue Underflow")** Prints `Queue Underflow` to indicate there are no elements in the queue
        - **return** As there is no elements to display, the method returns early.
    - **else:** Executed if the queue is not empty
        - **for i in range(0, self.rear+1):** Runs a `for` loop from 0 (first element index) to `rear` (last element index) in the queue.
            - **print(self.queue[i], end="--")** Prints the ith element of the queue followed by "--"
        - **print("None")** Prints `None` to signify the end of queue

**Example 1:** If the queue is completely empty, like the one shown below, the function prints `Queue Underflow` and returns.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">1</div>
</div>
<div>0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">3</div>
</div>
<div>2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
<div>front=-1</div>
<div>rear=-1</div>
</div><br>


**Example 2:** If the queue contains elements like the one shown below, then a for loop is started that runs from the front item to the last item.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
<div>rear=2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

Here, i starts at 0 and goes up to 2, printing all the elements in the queue.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
<div>i=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
<div>rear=2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
<div>i=1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
<div>rear=2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>0</div>
<div>front=0</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
</div>
<div>1</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
</div>
<div>2</div>
<div>rear=2</div>
<div>i=2</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">4</div>
</div>
<div>3</div>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 48px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1; color: #DBE0E5;">5</div>
</div>
<div>4</div>
</div>
</div>
</div><br>

```python
OUTPUT: 1--2--3
```

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

**Example 1:** Suppose the queue is empty. So `head` will be `None`.

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="width:60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div>None</div>
</div>
<div>head</div>
</div>

First, a new node is created using the `Node` class. Let the data in the node be 1 and 100 be its memory address.

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">10</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>100</div>
</div>

Since, this is the first element in the queue, its address (100) is assigned to `head`, creating a link between them.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
<svg style="width: 30px; height: 30px;">
<line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
<polygon points="30,15 20,10 20,20" style="fill: black;" />
</svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">10</div>
<div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
<div style="flex: 1;">None</div>
</div>
<div>100</div>
</div>
</div>
</div><br>

**Example 2:** Suppose a queue has been already created.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>200</div>
</div>
</div>
</div><br>

First a new node is created with the desired value. Let that value be 3 and its memory address be 300.

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div><br>

Then a `temp` variable is created and assigned the address of front item.

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 50px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">100</div>
</div>
<div>temp</div>
</div><br>

The `temp` variable moves to the last node of the queue with the help of the `while` loop.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
<div>temp</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>200</div>
</div>
</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
<div>New Node</div>
</div>
</div>
</div>
</div><br>


<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>200</div>
<div>temp</div>
</div>
</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
<div>New Node</div>
</div>
</div>
</div>
</div><br>

When `temp` reaches the last node, address of the new node is assigned to `next` attribute of last node, creating a link between them.

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div>
</div>
</div><br>

- **def dequeue(self):** Defines the dequeue() method which deletes the front element of the queue. It takes one parameter, self (an instance of the `Queue` class)
    - **if self.head is None:** Checks if the queue is empty
        - **print("Queue Underflow")** If the condition is `True`, then prints `Queue Underflow`
        - **return None** Returns `None` as there are no elements in the queue
    - **else:** Executed when queue is not empty
        - **data = self.head.data** Stores the value of the front node in a variable `data`
        - **self.head = self.head.next** Assigns the address of second node to `head`, effectively removing the link between `head` and front item.
        - **return data** Returns the item stored that was removed from the queue, stored in `data`

**Example 1:** If the queue is empty, then `head` would be `None`. 

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="width:60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div>None</div>
</div>
<div>head</div>
</div><br>

Since, there are no elements to be deleted, the function prints `Queue Underflow` and returns.

**Example 2:** If the queue already contains elements,

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div>
</div>
</div><br>

First, the front element is stored in the `data` variable. Then, the address of the second element is assigned to `head`, breaking the link between `head` and the original front element.

<div style="display: flex; justify-content: space-evenly; align-items: center;">
<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">200</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div>
</div>
</div>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
</div>
<div>data</div>
</div>
</div>
</div>
</div><br>

Finally, the front item stored in `data` variable is returned.

- **def peek(self):** Defines a method `peek()` which displays the front element without removing it.
    - **if self.head is None:** Checks if the queue is empty
        - **print("Queue Underflow")** Prints `Queue Underflow` to show there are no elements in the queue.
        - **return None** Returns `None` as there are no elements to return
    - **return self.head.data** If the queue is not empty, then returns the data of the front node.

**Example 1:** If the queue is completely empty, `head` would be `None`.

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="width:60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div>None</div>
</div>
<div>head</div>
</div><br>

Since `head` is `None`, the function prints `Queue Underflow` and returns.

**Example 2:** If the queue is already created and has some elements in it,

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;"/>
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div>
</div>
</div><br>

Here, the function returns the front element, i.e, 1.

- **def isEmpty(self):** Defines the `isEmpty()` method which checks if the queue is empty or not.
    - **return self.head is None** If `head` is equal to `None`, then it means that the queue is empty. Hence, if the condition holds, the function returns `True`, otherwise `False`.

**Example 1:** If the queue is completely empty, `head` would be `None`.

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="width:60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div>None</div>
</div>
<div>head</div>
</div><br>

Since `head` is `None`, the function returns `True`.

**Example 2:** If the queue already has some elements in it,

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 40px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;"/>
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div>
</div>
</div><br>

Here, `head` is not `None`, hence, the function returns `False`.

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

**Example 1:** If the queue is completely empty, `head` would be `None`.

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="width:60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div>None</div>
</div>
<div>head</div>
</div><br>

Since `head` is `None`, the function prints `Queue Underflow` and returns.

**Example 2:** Let a queue be created as shown below

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
<svg style="width: 30px; height: 30px;">
<line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
<polygon points="30,15 20,10 20,20" style="fill: black;" />
</svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div>
</div>
</div><br>

A temporary variable `temp` is created and is assigned the value of `head`.

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">100</div>
</div>
<div>temp</div>
</div><br>

This `temp` variable keeps moving forward node by node, printing its data as it goes.


<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
<svg style="width: 30px; height: 30px;">
<line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
<polygon points="30,15 20,10 20,20" style="fill: black;" />
</svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
<div>temp</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div>
</div>
</div>

```python
OUTPUT: 1->
```
<br>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
<svg style="width: 30px; height: 30px;">
<line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
<polygon points="30,15 20,10 20,20" style="fill: black;" />
</svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
<div>temp</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
</div>
</div>
</div>

```python
OUTPUT: 1->2->
```
<br>

<div style="text-align:center;">
<div style="display:inline-flex;">
<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">100</div>
</div>
<div>head</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
<svg style="width: 30px; height: 30px;">
<line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
<polygon points="30,15 20,10 20,20" style="fill: black;" />
</svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">1</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">200</div>
</div>
<div>100</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">2</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">300</div>
</div>
<div>200</div>
</div>

<div style="height: 21px; display: inline-flex; justify-content: center; align-items: center;">
    <svg style="width: 30px; height: 30px;">
        <line x1="0" y1="15" x2="30" y2="15" style="stroke: black; stroke-width: 2;" />
        <polygon points="30,15 20,10 20,20" style="fill: black;" />
    </svg>
</div>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 65px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
    <div style="flex: 1;">3</div>
    <div style="width: 1px; height:21px; background-color: black; margin: 0 10px;"></div>
    <div style="flex: 1;">None</div>
</div>
<div>300</div>
<div>temp</div>
</div>
</div>
</div>

```python
OUTPUT: 1->2->3->
```
<br>

<div style="display:flex; flex-direction: column; align-items: center;">
<div style="position:relative; display:inline-flex; width: 60px; border: 1px solid black; background-color: #DBE0E5; text-align:center; line-height: 1.5;">
<div style="flex: 1;">None</div>
</div>
<div>temp</div>
</div>

```python
OUTPUT: 1->2->3->None
```


## Complexity Analysis

Below is the table of time and space complexities of various queue operations using array:

| Method       | Time Complexity | Space Complexity |
|:------------:|:------------:|:------------:|
| `enqueue`    |  O(1)  |  O(1)  |
| `dequeue`    |  O(n)  |  O(1)  |
| `peek`       |  O(1)  |  O(1)  |
| `isFull`     |  O(1)  |  O(1)  |
| `isEmpty`    |  O(1)  |  O(1)  |
| `display`    |  O(n)  |  O(1)  |


This table given below shows the time and space complexities of various queue operations using linked list:

| Method     | Time Complexity | Space Complexity |
|:------------:|:------------:|:------------:|
| `enqueue()`  | O(n) | O(1)  |
| `dequeue()`  | O(n) | O(1)  |
| `peek()`     | O(1) | O(1)  |
| `isEmpty()`  | O(1) | O(1)  |
| `display()`  | O(n) | O(1)  |


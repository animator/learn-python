# Queues in Python

A queue is a linear data structure where elements are added at the back (enqueue) and removed from the front (dequeue). Imagine a line at a coffee shop, the first in line (front) gets served first, and new customers join at the back. This FIFO approach ensures order and fairness in processing elements.

Queues offer efficient implementations for various scenarios. They are often used in:
- **Task Scheduling** - Operating systems utilize queues to manage processes waiting for CPU time.
- **Breadth-first search algorithms** - Traversing a tree or graph involves exploring neighbouring nodes level by level, often achieved using a queue.
- **Message passing** - Communication protocols leverage queues to buffer messages between applications for reliable delivery.

## Types of Queue

A queue can be classified into 4 types -

- **Simple Queue** - A simple queue is a queue, where we can only insert an element at the back and remove the element from the front of the queue, this type of queue follows the FIFO principle.
- **Double-Ended Queue (Dequeue)** - In this type of queue, insertions and deletions of elements can be performed from both ends of the queue.<br>
Double-ended queues can be classified into 2 types ->
    - **Input-Restricted Queue**
    - **Output-Restricted Queue**
- **Circular Queue** - It is a special type of queue where the back is connected to the front, where the operations follow the FIFO principle.
- **Priority Queue** - In this type of queue, elements are accessed based on their priority in the queue. <br>
Priority queues are of 2 types ->
    - **Ascending Priority Queue**
    - **Descending Priority Queue**

## Real Life Examples of Queues
- **Customer Service** - Consider how a customer service phone line works. Customers calling are put into a queue. The first customer to call is the first one to be served (FIFO). As more customers call, they are added to the end of the queue, and as customers are served, they are removed from the front. The entire process follows the queue data structure.

- **Printers** - Printers operate using a queue to manage print jobs. When a user sends a document to the printer, the job is added to the queue (enqueue). Once a job completes printing, it's removed from the queue (dequeue), and the next job in line starts. This sequential order of handling tasks perfectly exhibits the queue data structure.

- **Computer Memory** - Certain types of computer memory use a queue data structure to hold and process instructions. For example, in a computer's cache memory, the fetch-decode-execute cycle of an instruction follows a queue. The first instruction fetched is the first one to be decoded and executed, while new instructions fetched are added to the rear.

<hr>

# Important Terminologies in Queues

Understanding these terms is crucial for working with queues:

- **Enqueue** - Adding an element to the back of the queue.
- **Dequeue** - Removing the element at the front of the queue.
- **Front** - The first element in the queue, to be removed next.
- **Rear/Back** - The last element in the queue, where new elements are added.
- **Empty Queue** - A queue with no elements.
- **Overflow** - Attempting to enqueue an element when the queue is full.
- **Underflow** - Attempting to dequeue an element from an empty queue.

## Operations on a Queue

There are some key operations in a queue that include - 

- **isFULL** - This operation checks if a queue is full.
- **isEMPTY** - This operation checks if a queue is empty.
- **Display** - This operation displays the queue elements.
- **Peek** - This operation is the process of getting the front value of a queue, without removing it. (i.e., Value at the front).

<hr>

# Implementation of Queue

```python
def isEmpty(Qu):
    if Qu == []:
        return True
    else:
        return False
    
def Enqueue(Qu, item) :
    Qu.append(item)
    if len(Qu) == 1:
        front = rear = 0
    else:
        rear = len(Qu) - 1
    print(item, "enqueued to queue")
def Dequeue(Qu):
    if isEmpty(Qu):
         print("Underflow")
    else:
        item = Qu.pop(0)
    if len(Qu) == 0:              #if it was single-element queue
        front = rear = None
    print(item, "dequeued from queue")

def Peek(Qu):
    if isEmpty(Qu):
        print("Underflow")
    else:
        front = 0
        print("Frontmost item is :", Qu[front])

def Display(Qu):
    if isEmpty(Qu):
        print("Queue Empty!")
    elif len(Qu) == 1:
        print(Qu[0], "<== front, rear")
    else:
        front = 0
        rear = len(Qu) - 1
        print(Qu[front], "<-front")
        for a in range(1, rear):
            print(Qu[a])
        print(Qu[rear], "<-rear")

queue = []                  #initially queue is empty
front = None

# Example Usage
Enqueue(queue, 1)
Enqueue(queue, 2)
Enqueue(queue, 3)
Dequeue(queue)
Peek(queue)
Display(queue)
```

## Output

```
1 enqueued to queue
2 enqueued to queue
3 enqueued to queue
1 dequeued from queue
Frontmost item is : 2
2 <-front
3 <-rear
```

## Complexity Analysis

- **Worst case**: `O(n^2)` This occurs when the code performs lots of display operations.
- **Best case**: `O(n)` If the code mostly performs enqueue, dequeue and peek operations.
- **Average case**: `O(n^2)` It occurs when the number of operations in display are more than the operations in enqueue, dequeue and peek.

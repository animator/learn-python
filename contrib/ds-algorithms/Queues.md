# Introduction to Queues

A queue is a linear data structure where elements are added at the back (enqueue) and removed from the front (dequeue). Imagine a line at a coffee shop, the first in line (front) gets served first, and new customers join at the back. This FIFO approach ensures order and fairness in processing elements.

Queues offer efficient implementations for various scenarios. They are often used in:
- <b>Task Scheduling</b> - Operating systems utilize queues to manage processes waiting for CPU time.
- <b>Breadth-first search algorithms</b> - Traversing a tree or graph involves exploring neighbouring nodes level by level, often achieved using a queue.
- <b>Message passing</b> - Communication protocols leverage queues to buffer messages between applications for reliable delivery.

<hr>

<img width="500" alt="Screenshot 2024-05-18 at 10 16 30 PM" src="https://github.com/PilotAxis/learn-python/assets/109688855/e4be7297-d3a0-4fc3-a0f1-81262acc85d9">


## Real Life Examples of Queues
- <b>Customer Service</b> - Consider how a customer service phone line works. Customers calling are put into a queue. The first customer to call is the first one to be served (FIFO). As more customers call, they are added to the end of the queue, and as customers are served, they are removed from the front. The entire process follows the queue data structure.

- <b>Printers</b> - Printers operate using a queue to manage print jobs. When a user sends a document to the printer, the job is added to the queue (enqueue). Once a job completes printing, it's removed from the queue (dequeue), and the next job in line starts. This sequential order of handling tasks perfectly exhibits the queue data structure.

- <b>Computer Memory</b> - Certain types of computer memory use a queue data structure to hold and process instructions. For example, in a computer's cache memory, the fetch-decode-execute cycle of an instruction follows a queue. The first instruction fetched is the first one to be decoded and executed, while new instructions fetched are added to the rear.

<hr>

# Important Terminologies in Queues

Understanding these terms is crucial for working with queues:

- <b>Enqueue</b> - Adding an element to the back of the queue.
- <b>Dequeue</b> - Removing the element at the front of the queue.
- <b>Front</b> - The first element in the queue, to be removed next.
- <b>Rear/Back</b> - The last element in the queue, where new elements are added.
- <b>Empty Queue</b> - A queue with no elements.
- <b>Overflow</b> - Attempting to enqueue an element when the queue is full.
- <b>Underflow</b> - Attempting to dequeue an element from an empty queue.

<hr>

# Operations on a Queue

There are some key operations in a queue that include - 

- <b>isFULL</b> - This operation is used to check if a queue is full.
- <b>isEMPTY</b> - This operation is used to check if a queue is empty.
- <b>Display</b> - This operation is used to display the queue elements.
- <b>Peek</b> - This operation is the process of getting the front value of a queue, without removing it. (i.e., Value at the front).

<img width="587" alt="image" src="https://github.com/PilotAxis/learn-python/assets/109688855/f561382f-bc19-48f8-87a9-b411d3e3ef2f">

# Threading in Python
Threading is a sequence of instructions in a program that can be executed independently of the remaining process and 
Threads are like lightweight processes that share the same memory space but can execute independently. 
The process is an executable instance of a computer program. 
This guide provides an overview of the threading module and its key functionalities.

## Key Characteristics of Threads:
* Shared Memory: All threads within a process share the same memory space, which allows for efficient communication between threads.
* Independent Execution: Each thread can run independently and concurrently.
* Context Switching: The operating system can switch between threads, enabling concurrent execution.

## Threading Module
This module will allows you to create and manage threads easily. This module includes several functions and classes to work with threads.

**1. Creating Thread:**
To create a thread in Python, you can use the Thread class from the threading module.

Example:
```python
import threading
        
# Create a thread
thread = threading.Thread()

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Thread has finished execution.")
```
Output :
```
Thread has finished execution.
```
**2. Performing Task with Thread:**
We can also perform a specific task by thread by giving a function as target and its argument as arg ,as a parameter to Thread object.

Example:

```python
import threading

# Define a function that will be executed by the thread
def print_numbers(arg):
    for i in range(arg):
        print(f"Thread: {i}")        
# Create a thread
thread = threading.Thread(target=print_numbers,args=(5,))

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Thread has finished execution.")
```
Output :
```
Thread: 0
Thread: 1
Thread: 2
Thread: 3
Thread: 4
Thread has finished execution.
```
**3. Delaying a Task with Thread's Timer Function:**
We can set a time for which we want a thread to start. Timer function takes 4 arguments (interval,function,args,kwargs).

Example:
```python
import threading

# Define a function that will be executed by the thread
def print_numbers(arg):
    for i in range(arg):
        print(f"Thread: {i}")        
# Create a thread after 3 seconds
thread = threading.Timer(3,print_numbers,args=(5,))

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Thread has finished execution.")
```
Output :
```
# after three second output will be generated
Thread: 0
Thread: 1
Thread: 2
Thread: 3
Thread: 4
Thread has finished execution.
```
**4. Creating Multiple Threads**
We can create and manage multiple threads to achieve concurrent execution.

Example:
```python 
import threading

def print_numbers(thread_name):
    for i in range(5):
        print(f"{thread_name}: {i}")

# Create multiple threads
thread1 = threading.Thread(target=print_numbers, args=("Thread 1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution.")
```
Output :
```
Thread 1: 0
Thread 1: 1
Thread 2: 0
Thread 1: 2
Thread 1: 3
Thread 2: 1
Thread 2: 2
Thread 2: 3
Thread 2: 4
Thread 1: 4
Both threads have finished execution.
```

**5. Thread Synchronization**
When we create multiple threads and they access shared resources, there is a risk of race conditions and data corruption. To prevent this, you can use synchronization primitives such as locks.
A lock is a synchronization primitive that ensures that only one thread can access a shared resource at a time.

Example:
```Python
import threading

lock = threading.Lock()

def print_numbers(thread_name):
    for i in range(10):
        with lock:
            print(f"{thread_name}: {i}")

# Create multiple threads
thread1 = threading.Thread(target=print_numbers, args=("Thread 1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution.")
```
Output :
```
Thread 1: 0
Thread 1: 1
Thread 1: 2
Thread 1: 3
Thread 1: 4
Thread 1: 5
Thread 1: 6
Thread 1: 7
Thread 1: 8
Thread 1: 9
Thread 2: 0
Thread 2: 1
Thread 2: 2
Thread 2: 3
Thread 2: 4
Thread 2: 5
Thread 2: 6
Thread 2: 7
Thread 2: 8
Thread 2: 9
Both threads have finished execution.
```

A ```lock``` object is created using threading.Lock() and The ```with lock``` statement ensures that the lock is acquired before printing and released after printing. This prevents other threads from accessing the print statement simultaneously.

## Conclusion
Threading in Python is a powerful tool for achieving concurrency and improving the performance of I/O-bound tasks. By understanding and implementing threads using the threading module, you can enhance the efficiency of your programs. To prevent race situations and maintain data integrity, keep in mind that thread synchronization must be properly managed.

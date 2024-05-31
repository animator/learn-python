[1mdiff --git a/contrib/advanced-python/MultiThreadingg.md b/contrib/advanced-python/MultiThreadingg.md[m
[1mindex bb88345..b3fecc1 100644[m
[1m--- a/contrib/advanced-python/MultiThreadingg.md[m
[1m+++ b/contrib/advanced-python/MultiThreadingg.md[m
[36m@@ -1,23 +1,24 @@[m
[31m-             # MultiThreading in python[m
[32m+[m[32m                                                  # MultiThreading in python[m
 >> Introduction[m
[31m-Multithreading in Python allows you to run multiple threads (smaller units of a process) simultaneously, enabling concurrent execution of tasks. This can be particularly useful for I/O-bound operations or when you need to perform multiple operations at the same time.[m
[32m+[m[32m       Multithreading in Python allows you to run multiple threads (smaller units of a process) simultaneously, enabling concurrent execution of tasks. This can be particularly useful for I/O-bound operations or when you need to perform multiple operations at the same time.[m
 [m
 >> Why Use Multithreading?[m
[31m-Improved performance: Allows multiple tasks to run concurrently, which can lead to more efficient utilization of resources.[m
[31m-Responsive applications: Keeps your applications responsive, especially during long-running operations.[m
[31m-Better resource utilization: Makes better use of system resources, especially in I/O-bound applications.[m
[31m-Threading Module[m
[31m-Python's threading module provides a way to create and manage threads. It includes the Thread class, which represents an individual thread of execution.[m
[32m+[m[32m   1.Improved performance: Allows multiple tasks to run concurrently, which can lead to more efficient utilization of resources.[m
[32m+[m[32m   2.Responsive applications: Keeps your applications responsive, especially during long-running operations.[m
[32m+[m[32m   3.Better resource utilization: Makes better use of system resources, especially in I/O-bound applications.[m
 [m
[31m-**Creating a Thread**[m
[31m-To create a new thread, you can instantiate the Thread class and provide a target function to be executed by the thread.[m
[32m+[m[32m  - Threading Module[m
[32m+[m[32m    Python's threading module provides a way to create and manage threads. It includes the Thread class, which represents an individual thread of execution.[m
 [m
[32m+[m[32m **Creating a Thread**[m
[32m+[m[32m     To create a new thread, you can instantiate the Thread class and provide a target function to be executed by the thread.[m
 [m
[31m-import threading[m
 [m
[31m-def print_numbers():[m
[31m-    for i in range(1, 6):[m
[31m-        print(i)[m
[32m+[m[32m -import threading[m
[32m+[m
[32m+[m[32m     def print_numbers():[m
[32m+[m[32m         for i in range(1, 6):[m
[32m+[m[32m            print(i)[m
 [m
 # Create a thread[m
 thread = threading.Thread(target=print_numbers)[m
[36m@@ -27,19 +28,20 @@[m [mthread.start()[m
 [m
 # Wait for the thread to complete[m
 thread.join()[m
[31m-Synchronizing Threads[m
[31m-When multiple threads access shared resources, synchronization is necessary to avoid data corruption. The threading module provides synchronization primitives like Lock, RLock, Semaphore, and Condition.[m
 [m
[31m-Example using Lock[m
[32m+[m[32m - Synchronizing Threads[m
[32m+[m[32m     When multiple threads access shared resources, synchronization is necessary to avoid data corruption. The threading module provides synchronization primitives like Lock, RLock, Semaphore, and Condition.[m
 [m
[31m-import threading[m
[32m+[m[32m  - Example using Lock[m
 [m
[31m-lock = threading.Lock()[m
[32m+[m[32m    import threading[m
 [m
[31m-def print_numbers():[m
[31m-    with lock:[m
[31m-        for i in range(1, 6):[m
[31m-            print(i)[m
[32m+[m[32m    lock = threading.Lock()[m
[32m+[m
[32m+[m[32m    def print_numbers():[m
[32m+[m[32m        with lock:[m
[32m+[m[32m           for i in range(1, 6):[m
[32m+[m[32m             print(i)[m
 [m
 # Create multiple threads[m
 threads = [threading.Thread(target=print_numbers) for _ in range(3)][m
[36m@@ -51,21 +53,22 @@[m [mfor thread in threads:[m
 # Wait for all threads to complete[m
 for thread in threads:[m
     thread.join()[m
[31m-Thread Communication[m
[31m-Threads can communicate using shared variables, but this requires careful synchronization. Another approach is to use thread-safe data structures like Queue from the queue module.[m
 [m
[31m-** Example using Queue[m
[32m+[m[32m - Thread Communication[m
[32m+[m[32m   Threads can communicate using shared variables, but this requires careful synchronization. Another approach is to use thread-safe data structures like Queue from the queue module.[m
 [m
[31m-import threading[m
[31m-import queue[m
[32m+[m[32m ** Example using Queue[m
 [m
[31m-def worker(q):[m
[31m-    while not q.empty():[m
[31m-        item = q.get()[m
[31m-        print(f'Processing {item}')[m
[31m-        q.task_done()[m
[32m+[m[32m    import threading[m
[32m+[m[32m    import queue[m
 [m
[31m-q = queue.Queue()[m
[32m+[m[32m    def worker(q):[m
[32m+[m[32m       while not q.empty():[m
[32m+[m[32m         item = q.get()[m
[32m+[m[32m         print(f'Processing {item}')[m
[32m+[m[32m         q.task_done()[m
[32m+[m
[32m+[m[32m    q = queue.Queue()[m
 [m
 # Add items to the queue[m
 for item in range(1, 11):[m
[36m@@ -82,33 +85,33 @@[m [mq.join()[m
 Example: Multithreading in Python[m
 Let's create a more comprehensive example to demonstrate multithreading in a real-world scenario.[m
 [m
[31m-Example: Downloading Multiple URLs[m
[32m+[m[32m - Example: Downloading Multiple URLs[m
 [m
[31m-import threading[m
[31m-import requests[m
[32m+[m[32m   import threading[m
[32m+[m[32m   import requests[m
 [m
[31m-urls = [[m
[32m+[m[32m   urls = [[m
     'http://example.com',[m
     'http://example.org',[m
     'http://example.net',[m
[31m-][m
[32m+[m[32m   ][m
 [m
[31m-def download_url(url):[m
[31m-    response = requests.get(url)[m
[31m-    print(f'Downloaded {url} with status {response.status_code}')[m
[32m+[m[32m  def download_url(url):[m
[32m+[m[32m     response = requests.get(url)[m
[32m+[m[32m     print(f'Downloaded {url} with status {response.status_code}')[m
 [m
[31m-threads = [threading.Thread(target=download_url, args=(url,)) for url in urls][m
[32m+[m[32m  threads = [threading.Thread(target=download_url, args=(url,)) for url in urls][m
 [m
[31m-for thread in threads:[m
[32m+[m[32m  for thread in threads:[m
     thread.start()[m
 [m
[31m-for thread in threads:[m
[32m+[m[32m  for thread in threads:[m
     thread.join()[m
 [m
[31m- >> Common Pitfalls[m
[31m-Global Interpreter Lock (GIL): Python's GIL can limit the performance benefits of threading for CPU-bound tasks. Consider using multiprocessing for such tasks.[m
[31m-Race conditions: Ensure proper synchronization to avoid race conditions when accessing shared resources.[m
[32m+[m[32m     >> Common Pitfalls[m
[32m+[m[32m       1.Global Interpreter Lock (GIL): Python's GIL can limit the performance benefits of threading for CPU-bound tasks. Consider using multiprocessing for such tasks.[m
[32m+[m[32m       2.Race conditions: Ensure proper synchronization to avoid race conditions when accessing shared resources.[m
 Deadlocks: Be cautious of deadlocks when using multiple locks.[m
 [m
[31m- >> Conclusion[m
[31m-Multithreading in Python is a powerful tool for concurrent execution, especially for I/O-bound tasks. By understanding and correctly implementing threading, you can significantly improve the performance and responsiveness of your applications.[m
\ No newline at end of file[m
[32m+[m[32m  >> Conclusion[m
[32m+[m[32m    Multithreading in Python is a powerful tool for concurrent execution, especially for I/O-bound tasks. By understanding and correctly implementing threading, you can significantly improve the performance and responsiveness of your applications.[m
\ No newline at end of file[m

## Learning Searching Algorithms 
Searching algorithms are essential tools in computer science used to locate specific items within a collection of data. These algorithms are designed to efficiently navigate through data structures to find the desired information, making them fundamental in various applications such as databases, web search engines, and more.
**Searching** is the fundamental process of locating a specific element or item within a collection of data. This collection of data can take various forms, such as arrays, lists, trees, or other structured representations. The primary objective of searching is to determine whether the desired element exists within the data, and if so, to identify its precise location or retrieve it. It plays an important role in various computational tasks and real-world applications, including information retrieval, data analysis, decision-making processes, and more.


## 1. Linear Search

Linear Search is a method for searching an element in a collection of elements. In Linear Search, each element of the collection is visited one by one in a sequential fashion to find the desired element. Linear Search is also known as Sequential Search.

In Linear Search Algorithm, 

Every element is considered as a potential match for the key and checked for the same.
If any element is found equal to the key, the search is successful and the index of that element is returned.
If no element is found equal to the key, the search yields “No match found”.

```python
LinearSearch(list, key)  
  for each item in the list  
    if item == value  
      return its index position  
   return -1  
```
####Python Program
```python
def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  
```
######output
Element found at index:  4

## 2. Binary Search
Binary search is a search algorithm used to find the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half until the target value is found or the interval is empty. The search interval is halved by comparing the target element with the middle value of the search space.
####Conditions to apply Binary Search Algorithm in a Data Structure:
 To apply Binary Search algorithm:

- The data structure must be sorted.
-  Access to any element of the data structure takes constant time.

####In this algorithm, 


- Divide the search space into two halves by finding the middle index “mid”. 


- Compare the middle element of the search space with the key. 
- If the key is found at middle element, the process is terminated.
- If the key is not found at middle element, choose which half will be used as the next search space.
- If the key is larger than the middle element, then the right side is used for next search.

```python
# Python3 code to implement iterative Binary
# Search.


# It returns location of x in given array arr
def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

```
######Output
Element is present at index 3

## Binary Search Code in Python (Recursive)

```python
def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
```

## Complexity Analysis
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1) (Iterative), O(log n) (Recursive)

</br>
<hr>
</br>

# 3. Interpolation Search

Interpolation search is an improved version of binary search, especially useful when the elements in the collection are uniformly distributed. Instead of always dividing the search interval in half, interpolation search estimates the position of the target element based on its value and the values of the endpoints of the search interval.

**Algorithm Overview:**
- **Estimating Position:** Interpolation search calculates an approximate position of the target element within the search interval based on its value and the values of the endpoints.
- **Refining the Estimate:** It adjusts the estimated position based on whether the target value is likely to be closer to the beginning or end of the search interval.
- **Updating the Interval:** Using the refined estimate, it narrows down the search interval iteratively until the target is found or the interval becomes empty.

## Interpolation Search Code in Python

```python
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 60
result = interpolation_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
```

## Complexity Analysis
- **Time Complexity**: O(log log n) (Average)
- **Space Complexity**: O(1)

</br>
<hr>
</br>
# Summary
##Applications of Searching:##

Searching algorithms have numerous applications across various fields. Here are some common applications:

####Information Retrieval:
Search engines like Google, Bing, and Yahoo use sophisticated searching algorithms to retrieve relevant information from vast amounts of data on the web.
####Database Systems:
Searching is fundamental in database systems for retrieving specific data records based on user queries, improving efficiency in data retrieval.

####Networking: 
In networking, searching algorithms are used for routing packets efficiently through networks, finding optimal paths, and managing network resources.
####and a lot more......

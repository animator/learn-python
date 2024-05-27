# STACKS IN PYTHON
In Data Structures and Algorithms, a stack is a linear data structure that complies with the Last In, First Out (LIFO) rule. It works by use of two fundamental techniques: *PUSH* which inserts an element on top of the stack and *POP* which takes out the topmost element.This concept is similar to a stack of plates in a cafeteria. Stacks are usually used for handling function calls, expression evaluation, and parsing in programming. Indeed, they are efficient in managing memory as well as tracking program state. On top of that, stacks can be implemented either via arrays or linked lists. Their simplicity coupled with adaptability has made them an integral part of many Computer Science and Software Development applications across the globe.

**Points To Be Remembered :-**
- A stack is a collection of data items that can be accessed at only one end, called *TOP*.
- Items can be inserted and deleted in a stack only at the *TOP*.
- The last item inserted in a stack is the first one to be deleted.
- Therefore, a stack is called a **Last-In-First-Out (LIFO)** data structure.

## Real Life Examples Of Stacks

**Pile Of Books** - Suppose a set of books are placed one over the other in a pile. When you remove books from the pile, the topmost book will be removed first. Similarly, when you have to add a book to the pile, the book will be placed at the top of the file.

**Pile Of Plates** - The first plate begins the pile. The second plate is placed on the top of the first plate and the third plate is placed on the top of the second plate, and so on. In general, if you want to add a plate to the pile, you can keep it on the top of the pile. Similarly, if you want to remove a plate, you can remove the plate from the top of the pile.

**Bangles In A Hand** - When a person wears bangles, the last bangle worn is the first one to be removed.

## Applications Of A Stack

Stacks are widely used in Computer Science:
- *Function call* management
- Maintaining the *UNDO* list for the application
- Web browser *history management*
- Evaluating expressions
- Checking the nesting of parentheses in an expression
- *Backtracking* algorithms (Recursion)

Understanding these applications is essential for Software Development.

## Operations On A Stack

Key operations on a stack include:
- **PUSH** - It is the process of inserting a new element on the top of a stack.
- **OVERFLOW** - A situation when we are pushing an item in a stack that is full.
- **POP** - It is the process of deleting an element from the top of a stack.
- **UNDERFLOW** - A situation when we are popping item from an empty stack.
- **PEEK** - It is the process of getting the most recent value of stack *(i.e. the value at the top of the stack)*
- **ISEMPTY** - It is the function which return true if stack is empty else false.
- **SHOW** -Displaying stack items.
  
## IMPLEMENTING STACKS IN PYTHON

```python
def isEmpty(S):
    
    if len(S) == 0:
        return True
    
    else:
        
       return False

def Push(S, item):
    S.append(item)

def Pop(S):
    
    if isEmpty(S):
        return "Underflow"
    
    else:
        val = S.pop()
        return val

def Peek(S):
    
    if isEmpty(S):
        return "Underflow"
    
    else:
        top = len(S) - 1
        return S[top]

def Show(S):
    
    if isEmpty(S):
        print("Sorry, No items in Stack")
    
    else:
        print("(Top)", end=' ')
        t = len(S) - 1
        while t >= 0:
            print(S[t], "<", end=' ')
            t -= 1
        print()
```

This code defines a stack data structure along with functions to manipulate it. To provide output, we would need to use these functions to interact with the stack.

Here's an example:
```python
stack = []

Push(stack, 5)
Push(stack, 10)
Push(stack, 15)

print("Stack after Push operations:")
Show(stack)

print("Peek operation:", Peek(stack))

print("Pop operation:", Pop(stack))

print("Stack after Pop operation:")
Show(stack)
```

This would output:

```
Stack after Push operations:

(Top) 15 < 10 < 5 <

Peek operation: 15

Pop operation: 15

Stack after Pop operation:

(Top) 10 < 5 <
```



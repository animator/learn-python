# Exception Handling in Python

Exception Handling is a way of managing the errors that may occur during a program execution. Python's exception handling mechanism has been designed to avoid the unexpected termination of the program, and offer to either regain control after an error or display a meaningful message to the user.

- **Error** - An error is a mistake or an incorrect result produced by a program. It can be a syntax error, a logical error, or a runtime error. Errors are typically fatal, meaning they prevent the program from continuing to execute.
- **Exception** - An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. Exceptions are typically unexpected and can be handled by the program to prevent it from crashing or terminating abnormally. It can be runtime, input/output or system exceptions. Exceptions are designed to be handled by the program, allowing it to recover from the error and continue executing.

## Python Built-in Exceptions

There are plenty of built-in exceptions in Python that are raised when a corresponding error occur.
We can view all the built-in exceptions using the built-in `local()` function as follows:

```python
print(dir(locals()['__builtins__']))
```

|**S.No**|**Exception**|**Description**|
|---|---|---|
|1|SyntaxError|A syntax error occurs when the code we write violates the grammatical rules such as misspelled keywords, missing colon, mismatched parentheses etc.|
|2|TypeError|A type error occurs when we try to perform an operation or use a function with objects that are of incompatible data types.|
|3|NameError|A name error occurs when we try to use a variable, function, module or string without quotes that hasn't been defined or isn't used in a valid way.|
|4|IndexError|A index error occurs when we try to access an element in a sequence (like a list, tuple or string) using an index that's outside the valid range of indices for that sequence.|
|5|KeyError|A key error occurs when we try to access a key that doesn't exist in a dictionary. Attempting to retrieve a value using a non-existent key results this error.|
|6|ValueError|A value error occurs when we provide an argument or value that's inappropriate for a specific operation or function such as doing mathematical operations with incompatible types (e.g., dividing a string by an integer.)|
|7|AttributeError|An attribute error occurs when we try to access an attribute (like a variable or method) on an object that doesn't possess that attribute.|
|8|IOError|An IO (Input/Output) error occurs when an operation involving file or device interaction fails. It signifies that there's an issue during communication between your program and the external system.|
|9|ZeroDivisionError|A ZeroDivisionError occurs when we attempt to divide a number by zero. This operation is mathematically undefined, and Python raises this error to prevent nonsensical results.|
|10|ImportError|An import error occurs when we try to use a module or library that Python can't find or import succesfully.|

## Try and Except Statement - Catching Exception

The `try-except` statement allows us to anticipate potential errors during program execution and define what actions to take when those errors occur. This prevents the program from crashing unexpectedly and makes it more robust.

Here's an example to explain this:

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except:
    print("An error occured!")
```

Output

```markdown
An error occured!
```

In this example, the `try` block contains the code that you suspect might raise an exception. Python attempts to execute the code within this block. If an exception occurs, Python jumps to the `except` block and executes the code within it.

## Specific Exception Handling

You can specify the type of expection you want to catch using the `except` keyword followed by the exception class name. You can also have multiple `except` blocks to handle different exception types.

Here's an example:

```python
try:
    # Code that might raise ZeroDivisionError or NameError
    result = 10 / 0
    name = undefined_variable
except ZeroDivisionError:
    print("Oops! You tried to divide by zero.")
except NameError:
    print("There's a variable named 'undefined_variable' that hasn't been defined yet.")
```

Output

```markdown
Oops! You tried to divide by zero.
```

If you comment on the line `result = 10 / 0`, then the output will be:

```markdown
There's a variable named 'undefined_variable' that hasn't been defined yet.
```

## Important Note

In this code, the `except` block are specific to each type of expection. If you want to catch both exceptions with a single `except` block, you can use of tuple of exceptions, like this:

```python
try:
    # Code that might raise ZeroDivisionError or NameError
    result = 10 / 0
    name = undefined_variable
except (ZeroDivisionError, NameError):
    print("An error occured!")
```

Output

```markdown
An error occured!
```

## Try with Else Clause

The `else` clause in a Python `try-except` block provides a way to execute code only when the `try` block succeeds without raising any exceptions. It's like having a section of code that runs exclusively under the condition that no errors occur during the main operation in the `try` block.

Here's an example to understand this:

```python
def calculate_average(numbers):
    if len(numbers) == 0:  # Handle empty list case seperately (optional)
        return None
    try:
        total = sum(numbers)
        average = total / len(numbers)
    except ZeroDivisionError:
        print("Cannot calculate average for a list containing zero.")
    else:
        print("The average is:", average)
        return average  #Optionally return the average here

# Example usage
numbers = [10, 20, 30]
result = calculate_average(numbers)

if result is not None:  # Check if result is available (handles empty list case)
    print("Calculation succesfull!")
```

Output

```markdown
The average is: 20.0
```

## Finally Keyword in Python

The `finally` keyword in Python is used within `try-except` statements to execute a block of code **always**, regardless of whether an exception occurs in the `try` block or not.

To understand this, let us take an example:

```python
try:
    a = 10 // 0
    print(a)
except ZeroDivisionError:
    print("Cannot be divided by zero.")
finally:
    print("Program executed!")
```

Output

```markdown
Cannot be divided by zero.
Program executed!
```

## Raise Keyword in Python

In Python, raising an exception allows you to signal that an error condition has occured during your program's execution. The `raise` keyword is used to explicity raise an exception.

Let us take an example:

```python
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero!")  # Raise an exception with a message
    result = x / y
    return result

try:
    division_result = divide(10, 0)
    print("Result:", division_result)
except ZeroDivisionError as e:
    print("An error occured:", e)  # Handle the exception and print the message
```

Output

```markdown
An error occured: Can't divide by zero!
```

## Advantages of Exception Handling

- **Improved Error Handling** - It allows you to gracefully handle unexpected situations that arise during program execution. Instead of crashing abruptly, you can define specific actions to take when exceptions occur, providing a smoother experience.
- **Code Robustness** - Exception Handling helps you to write more resilient programs by anticipating potential issues and providing approriate responses.
- **Enhanced Code Readability** - By seperating error handling logic from the core program flow, your code becomes more readable and easier to understand. The `try-except` blocks clearly indicate where potential errors might occur and how they'll be addressed.

## Disadvantages of Exception Handling

- **Hiding Logic Errors** - Relying solely on exception handling might mask underlying logic error in your code. It's essential to write clear and well-tested logic to minimize the need for excessive exception handling.
- **Performance Overhead** - In some cases, using `try-except` blocks can introduce a slight performance overhead compared to code without exception handling. Howerer, this is usually negligible for most applications.
- **Overuse of Exceptions** - Overusing exceptions for common errors or control flow can make code less readable and harder to maintain. It's important to use exceptions judiciously for unexpected situations.

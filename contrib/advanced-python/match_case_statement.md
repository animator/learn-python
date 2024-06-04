# Match Case Statements
## Introduction
Match and case statements are introduced in Python 3.10 for structural pattern matching of patterns with associated actions. It offers more readible and
cleaniness to the code as opposed to the traditional `if-else` statements. They also have destructuring, pattern matching and checks for specific properties in
addition to the traditional `switch-case` statements in other languages, which makes them more versatile.

## Syntax
```
match <statement>:
    case <pattern_1>:
        <do_task_1>
    case <pattern_2>:
        <do_task_2>
    case _:
        <do_task_wildcard>
```
A match statement takes a statement which compares it to the various cases and their patterns. If any of the pattern is matched successively, the task is performed accordingly. If an exact match is not confirmed, the last case, a wildcard `_`, if provided, will be used as the matching case.

## Pattern Matching
As discussed earlier, match case statements use pattern matching where the patterns consist of sequences, mappings, primitive data types as well as class instances. The structural pattern matching uses declarative approach and it nexplicitly states the conditions for the patterns to match with the data.

### Patterns with a Literal
#### Generic Case
`sample text` is passed as a literal in the `match` block. There are two cases and a wildcard case mentioned.
```python
match 'sample text':
    case 'sample text':
        print('sample text')
    case 'sample':
        print('sample')
    case _:
        print('None found')
```
The `sample text` case is satisfied as it matches with the literal `sample text` described in the `match` block.

O/P:
```
sample text
```

#### Using OR
Taking another example, `|` can be used as OR to include multiple patterns in a single case statement where the multiple patterns all lead to a similar task.

The below code snippets can be used interchangebly and generate the similar output. The latter is more consive and readible.
```python
match 'e':
    case 'a':
        print('vowel')
    case 'e':
        print('vowel')
    case 'i':
        print('vowel')
    case 'o':
        print('vowel')
    case 'u':
        print('vowel')
    case _:
        print('consonant')
```
```python
match 'e':
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('vowel')
    case _:
        print('consonant')
```
O/P:
```
vowel
```

#### Without wildcard
When in a `match` block, there is no wildcard case present there are be two cases of match being present or not. If the match doesn't exist, the behaviour is a no-op.
```python
match 'c':
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('vowel')
```
The output will be blank as a no-op occurs.

### Patterns with a Literal and a Variable
Pattern matching can be done by unpacking the assignments and also bind variables with it.
```python
def get_names(names: str) -> None:
    match names:
        case ('Bob', y):
            print(f'Hello {y}')
        case (x, 'John'):
            print(f'Hello {x}')
        case (x, y):
            print(f'Hello {x} and {y}')
        case _:
            print('Invalid')
```
Here, the `names` is a tuple that contains two names. The `match` block unpacks the tuple and binds `x` and `y` based on the patterns. A wildcard case prints `Invalid` if the condition is not satisfied.

O/P:

In this example, the above code snippet with the parameter `names` as below and the respective output.
```
>>> get_names(('Bob', 'Max'))
Hello Max

>>> get_names(('Rob', 'John'))
Hello Rob

>>> get_names(('Rob', 'Max'))
Hello Rob and Max

>>> get_names(('Rob', 'Max', 'Bob'))
Invalid
```

### Patterns with Classes
Class structures can be used in `match` block for pattern matching. The class members can also be binded with a variable to perform certain operations. For the class structure:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
The match case example illustrates the generic working as well as the binding of variables with the class members.
```python
def get_class(cls: Person) -> None:
    match cls:
        case Person(name='Bob', age=18):
            print('Hello Bob with age 18')
        case Person(name='Max', age=y):
            print(f'Age is {y}')
        case Person(name=x, age=18):
            print(f'Name is {x}')
        case Person(name=x, age=y):
            print(f'Name and age is {x} and {y}')
        case _:
            print('Invalid')
```
O/P:
```
>>> get_class(Person('Bob', 18))
Hello Bob with age 18

>>> get_class(Person('Max', 21))
Age is 21

>>> get_class(Person('Rob', 18))
Name is Rob

>>> get_class(Person('Rob', 21))
Name and age is Rob and 21
```
Now, if a new class is introduced in the above code snippet like below.
```python
class Pet:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal
```
The patterns will not match the cases and will trigger the wildcard case for the original code snippet above with `get_class` function.
```
>>> get_class(Pet('Tommy', 'Dog'))
Invalid
```

### Nested Patterns
The patterns can be nested via various means. It can include the mix of the patterns mentioned earlier or can be symmetrical across. A basic of the nested pattern of a list with Patterns with a Literal and Variable is taken. Classes and Iterables can laso be included.
```python
def get_points(points: list) -> None:
    match points:
        case []:
            print('Empty')
        case [x]:
            print(f'One point {x}')
        case [x, y]:
            print(f'Two points {x} and {y}')
        case _:
            print('More than two points')
```
O/P:
```
>>> get_points([])
Empty

>>> get_points([1])
One point 1

>>> get_points([1, 2])
Two points 1 and 2

>>> get_points([1, 2, 3])
More than two points
```

### Complex Patterns
#### Wildcard

#### Guard

## Summary

## Further Reading

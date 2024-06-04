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

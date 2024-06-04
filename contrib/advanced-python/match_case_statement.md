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

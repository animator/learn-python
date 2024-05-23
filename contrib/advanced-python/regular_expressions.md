## Regular Expressions in Python
Regular expressions (regex) are a powerful tool for pattern matching and text manipulation. 
Python's re module provides comprehensive support for regular expressions, enabling efficient text processing and validation.

## 1. Introduction to Regular Expressions
A regular expression is a sequence of characters defining a search pattern. Common use cases include validating input, searching within text, and extracting 
specific patterns.

## 2. Basic Syntax
Literal Characters: Match exact characters (e.g., abc matches "abc").
Metacharacters: Special characters like ., *, ?, +, ^, $, [ ], and | used to build patterns.

**Common Metacharacters:**

* .: Any character except newline.
* ^: Start of the string.
* $: End of the string.
* *: 0 or more repetitions.
* +: 1 or more repetitions.
* ?: 0 or 1 repetition.
* []: Any one character inside brackets (e.g., [a-z]).
* |: Either the pattern before or after.
  
## 3. Using the re Module

**Key functions in the re module:**

* re.match(): Checks for a match at the beginning of the string.
* re.search(): Searches for a match anywhere in the string.
* re.findall(): Returns a list of all matches.
* re.sub(): Replaces matches with a specified string.

Examples:
```bash
import re

# Match at the beginning
print(re.match(r'\d+', '123abc').group())  # Output: 123

# Search anywhere
print(re.search(r'\d+', 'abc123').group())  # Output: 123

# Find all matches
print(re.findall(r'\d+', 'abc123def456'))  # Output: ['123', '456']

# Substitute matches
print(re.sub(r'\d+', '#', 'abc123def456'))  # Output: abc#def#
```

## 4. Compiling Regular Expressions
Compiling regular expressions improves performance for repeated use.

Example:
```bash
import re

pattern = re.compile(r'\d+')
print(pattern.match('123abc').group())  # Output: 123
print(pattern.search('abc123').group())  # Output: 123
print(pattern.findall('abc123def456'))  # Output: ['123', '456']
```

## 5. Groups and Capturing
Parentheses () group and capture parts of the match.

Example:
```bash
import re

match = re.match(r'(\d{3})-(\d{2})-(\d{4})', '123-45-6789')
if match:
    print(match.group())   # Output: 123-45-6789
    print(match.group(1))  # Output: 123
    print(match.group(2))  # Output: 45
    print(match.group(3))  # Output: 6789
```

## 6. Special Sequences
Special sequences are shortcuts for common patterns:

* \d: Any digit.
* \D: Any non-digit.
* \w: Any alphanumeric character.
* \W: Any non-alphanumeric character.
* \s: Any whitespace character.
* \S: Any non-whitespace character.
Example:
```bash
import re

print(re.search(r'\w+@\w+\.\w+', 'Contact: support@example.com').group())  # Output: support@example.com
```

## Summary
Regular expressions are a versatile tool for text processing in Python. The re module offers powerful functions and metacharacters for pattern matching, 
searching, and manipulation, making it an essential skill for handling complex text processing tasks.

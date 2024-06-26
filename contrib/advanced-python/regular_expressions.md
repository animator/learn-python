## Regular Expressions in Python

Regular expressions (regex) are a powerful tool for pattern matching and text manipulation.
Python's re module provides comprehensive support for regular expressions, enabling efficient text processing and validation.
Regular expressions (regex) are a versitile tool for matching patterns in strings. In Python, the `re` module provides support for working with regular expressions.

## 1. Introduction to Regular Expressions

A regular expression is a sequence of characters defining a search pattern. Common use cases include validating input, searching within text, and extracting
specific patterns.

## 2. Basic Syntax

Literal Characters: Match exact characters (e.g., abc matches "abc").
Metacharacters: Special characters like ., \*, ?, +, ^, $, [ ], and | used to build patterns.

**Common Metacharacters:**

- .: Any character except newline.
- ^: Start of the string.
- $: End of the string.
- \*: 0 or more repetitions.
- +: 1 or more repetitions.
- ?: 0 or 1 repetition.
- []: Any one character inside brackets (e.g., [a-z]).
- |: Either the pattern before or after.
- \ : Used to drop the special meaning of character following it
- {} : Indicate the number of occurrences of a preceding regex to match.
- () : Enclose a group of Regex

Examples:

1. `.`

```bash
import re
pattern = r'c.t'
text = 'cat cot cut cit'
matches = re.findall(pattern, text)
print(matches)  # Output: ['cat', 'cot', 'cut', 'cit']
```

2. `^`

```bash
pattern = r'^Hello'
text = 'Hello, world!'
match = re.search(pattern, text)
print(match.group() if match else 'No match')  # Output: 'Hello'
```

3. `$`

```bash
pattern = r'world!$'
text = 'Hello, world!'
match = re.search(pattern, text)
print(match.group() if match else 'No match')  # Output: 'world!'
```

4. `*`

```bash
pattern = r'ab*'
text = 'a ab abb abbb'
matches = re.findall(pattern, text)
print(matches)  # Output: ['a', 'ab', 'abb', 'abbb']
```

5. `+`

```bash
pattern = r'ab+'
text = 'a ab abb abbb'
matches = re.findall(pattern, text)
print(matches)  # Output: ['ab', 'abb', 'abbb']
```

6. `?`

```bash
pattern = r'ab?'
text = 'a ab abb abbb'
matches = re.findall(pattern, text)
print(matches)  # Output: ['a', 'ab', 'ab', 'ab']
```

7. `[]`

```bash
pattern = r'[aeiou]'
text = 'hello world'
matches = re.findall(pattern, text)
print(matches)  # Output: ['e', 'o', 'o']
```

8. `|`

```bash
pattern = r'cat|dog'
text = 'I have a cat and a dog.'
matches = re.findall(pattern, text)
print(matches)  # Output: ['cat', 'dog']
```

9. `\``

```bash
pattern = r'\$100'
text = 'The price is $100.'
match = re.search(pattern, text)
print(match.group() if match else 'No match')  # Output: '$100'
```

10. `{}`

```bash
pattern = r'\d{3}'
text = 'My number is 123456'
matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '456']
```

11. `()`

```bash
pattern = r'(cat|dog)'
text = 'I have a cat and a dog.'
matches = re.findall(pattern, text)
print(matches)  # Output: ['cat', 'dog']
```

## 3. Using the re Module

**Key functions in the re module:**

- re.match(): Checks for a match at the beginning of the string.
- re.search(): Searches for a match anywhere in the string.
- re.findall(): Returns a list of all matches.
- re.sub(): Replaces matches with a specified string.
- re.split(): Returns a list where the string has been split at each match.
- re.escape(): Escapes special character
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

#Return a list where it get matched
print(re.split("\s", txt)) #['The', 'Donkey', 'in', 'the','Town']

# Escape special character
print(re.escape("We are good to go"))  #We\ are\ good\ to\ go
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

- \A:Returns a match if the specified characters are at the beginning of the string.
- \b:Returns a match where the specified characters are at the beginning or at the end of a word.
- \B:Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word.
- \d: Any digit.
- \D: Any non-digit.
- \w: Any alphanumeric character.
- \W: Any non-alphanumeric character.
- \s: Any whitespace character.
- \S: Any non-whitespace character.
- \Z:Returns a match if the specified characters are at the end of the string.

Example:

```bash
import re

print(re.search(r'\w+@\w+\.\w+', 'Contact: support@example.com').group())  # Output: support@example.com
```

## 7.Sets

A set is a set of characters inside a pair of square brackets [] with a special meaning:

- [arn] : Returns a match where one of the specified characters (a, r, or n) is present.
- [a-n] : Returns a match for any lower case character, alphabetically between a and n.
- [^arn] : Returns a match for any character EXCEPT a, r, and n.
- [0123] : Returns a match where any of the specified digits (0, 1, 2, or 3) are present.
- [0-9] : Returns a match for any digit between 0 and 9.
- [0-5][0-9] : Returns a match for any two-digit numbers from 00 and 59.
- [a-zA-Z] : Returns a match for any character alphabetically between a and z, lower case OR upper case.
- [+] : In sets, +, \*, ., |, (), $,{} has no special meaning
- [+] means: return a match for any + character in the string.

## Summary

Regular expressions (regex) are a powerful tool for text processing in Python, offering a flexible way to match, search, and manipulate text patterns. The re module provides a comprehensive set of functions and metacharacters to tackle complex text processing tasks.
With regex, you can:
1.Match patterns: Use metacharacters like ., \*, ?, and {} to match specific patterns in text.
2.Search text: Employ functions like re.search() and re.match() to find occurrences of patterns in text.
3.Manipulate text: Utilize functions like re.sub() to replace patterns with new text.

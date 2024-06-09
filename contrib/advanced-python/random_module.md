# Random Module in Python
The Random module in Python is a built-in module for generating pseudo-random numbers, which aren't truly random but are good enough for many purposes.

## Use Cases:
- Recaptcha: Adding randomness to authentication challenges.
- Lottery Draws: Ensuring fair and unpredictable number selection.
- Card Games: Shuffling decks of cards.
- Dice Games: Simulating dice rolls for games like Ludo.
- Coin Flips: Randomly determining outcomes.

## Importing the module :
1)  ```python
    import random
    ```
    This brings in the random module, letting you access its functions using 
    `random.function_name`. 

2)  ```python
    from random import * 
    ```
    This imports all functions from random directly into your code. While it's shorter to type,      it can make your code harder to read, especially in larger projects.

# Some functions present in `random` module :
 * [randint()](#randint())
 * [randrange()](#randrange())
 * [random()](#random())
 * [uniform()](#uniform())
 * [choice()](#choice())
 * [choices()](#choices())
 * [sample()](#sample())
 * [shuffle()](#shuffle())
 * [seed()](#seed())
 * [getrandbits()](#getrandbits())
 <br/><br/>  
## randint() 
*Syntax* : `random.randint(start, end)`

Returns a random integer from start to end.

#### Example :
```python
import random
print(random.randint(10, 20)) #10 and 20 both are inclusive.
```
#### Output :
```python
20
```
  
*Note* : 
- `random.randint(10, 20.3)` raises TypeError because randint does not support float arguments.
  ```python
  TypeError: 'float' object cannot be interpreted as an integer
  During handling of the above exception, another exception occurred:
  ValueError: non-integer stop for randrange()
  ```
- `random.randint(10, 2)` raises ValueError because it violates the condition `start <= end`
  ```python
  ValueError: empty range for randrange() (10, 3, -7)
  ```
<br/><br/>
## randrange()
*Syntax* : `random.randrange(start, stop[, step])` 

Returns a random integer within specified range.

**Note** : 
- [ ] indicates that step is optional and stop value is exclusive similar to `range` function.*
- By default, the value of `start` is 0 and `step` is 1
- It raises TypeError for `float` parameters and `ValueError` for invalid range(`start < end` is valid range) similar to `randint` function.
  
#### Example : 
```python
import random
start, stop, step = 1, 10, 2
print(random.randrange(stop))
print(random.randrange(start, stop))
print(random.randrange(start, stop, step))
```
#### Output : 
```python
2
9
3
```
<br/><br/>
## random() 

*Syntax* : `random.random()`

Returns a random float value from 0.0 to 1.0 (both are inclusive).
This function does not take arguments.

#### Example :
```python
import random
for i in range(3):
    print(random.random())
```
#### Output :
```python
0.2500515224144165
0.33090026782876447
0.4174030035037901
```
<br/><br/>
## uniform()
*Syntax* : `random.uniform(a, b)`

- Returns a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
- The end-point value b may or may not be included in the range depending on floating-point rounding in the expression a + (b-a) * random().
  
#### Example :
```python
import random
print(random.uniform(20, 100))
```
#### Output :
```python
77.6010657228253
```
<br/><br/>
## choice()
*Syntax* : `random.choice(seq)`

Return a random element from the non-empty sequence `seq`.

#### Example :
```python
import random

print(random.choice("random string"))  # Selects a random character from the string
print(random.choice([0, 1, 2, 3, 4]))  # Selects a random element from the list
print(random.choice((10, 20, 30, 40)))  # Selects a random element from the tuple

# The following lines will give errors:

# print(random.choice({2, 4, 5, 7, 89, 10}))  # Sets cannot be indexed, so choice() cannot be used with sets
# print(random.choice({2 : 4, 4 : 433}))      # Dictionaries cannot be indexed, so choice() cannot be used with dictionaries
# print(random.choice([]))                    # Empty lists cannot be indexed, so choice() will raise an IndexError

```

#### Output :
```python
a
3
10
```
<br/><br/>
## choices()
*Syntax* : `random.choices(population [, weights = None, *, cum_weights = None, k = 1])`

- Return a k sized list of elements chosen from the population with replacement.
- If the population is empty, raises `IndexError`.
#### Parameters : 
`population` : It is a sequence like list, tuple, range of numbers from which elements should be selected.
`weights` : A list were you can weigh the possibility for each value.
`cum_weights` : A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
*Example* : normal weights list: `[2, 1, 1]` is the same as this cum_weights list: `[2, 3, 4]`.
`k` : Length of the list to be returned.

#### Example :
```python
import random  # Importing the random module for random sampling
import itertools  # Importing itertools module for calculating cumulative weights

# List of elements
l = ["a", 1, "b", 2, "c", 3]

# Corresponding weights for each element in the list
wts = [2, 22, 4, 3, 20, 10]

# Calculating cumulative weights using itertools.accumulate()
cum_wts = list(itertools.accumulate(wts))

# Printing the weights and cumulative weights
print("Weights: ", wts)
print("Cumulative weights: ", cum_wts)

# Randomly choosing one element from the list
print(random.choices(l))

# Randomly choosing four elements from the list with replacement
print(random.choices(l, k=4))

# Randomly choosing one element from the list with weights
print(random.choices(l, wts))

# Randomly choosing four elements from the list with replacement and weights
print(random.choices(l, wts, k=4))

# Randomly choosing one element from the list with cumulative weights
print(random.choices(l, cum_wts))

# Randomly choosing four elements from the list with replacement and cumulative weights
print(random.choices(l, cum_wts, k=4))
```
#### Output :
```python
Weights:  [2, 22, 4, 3, 20, 10]
Cumulative weights:  [2, 24, 28, 31, 51, 61]
[1]
['a', 'c', 'b', 2]
['c']
[1, 'c', 1, 1]
[3]
[1, 3, 3, 'b']
```

*Note* : 
- If neither weights nor cum_weights are specified, selections are made with equal probability. 
- If a weights sequence is supplied, it must be the same length as the population sequence. Otherwise, `ValueError` occurs.
- The weights or cum_weights can use any numeric type that includes integers, floats, and fractions but excludes decimals and are assumed to be non-negative and finite.
- A `ValueError` is raised if all weights are zero.
- The value of k may be greater than the length of the sequence.
- The sequence should be non empty and should have indexing property.
- You cannot specify both cum_wts and wts as arguments. You can use either one of them or none.
*Eg:* `random.choices(l, wts, cum_wts, k = 4)` gives the following error : 
    ```python
    TypeError: Random.choices() takes from 2 to 3 positional arguments but 4 positional arguments (and 1 keyword-only argument) were given
    ```
<br/><br/>
## sample()
*Syntax* : `random.sample(population, k)`

- Return a k length list of unique elements chosen from the population sequence.
- Used for random sampling without replacement.
- If the sequence is empty, `IndexError` is raised.


#### Example :
```python
import random

#using list
list1 = [1, 2, 3, 5, 5, 6] 
print("With list:", random.sample(list1, 3))

#using string
string = "any random string"
print("With string:", random.sample(string, 6))

#using tuple
tuple1 = (2, 3, 2, 5, 3) 
print("With tuple:", random.sample(tuple1, 2)) 
```

#### Output :
```python
With list: [3, 5, 5]
With string: ['a', 'a', 'o', 'd', 'r', 't']
With tuple: [2, 2]
```

*Note* : 
- Members of the population need not be hashable or unique.
- If the sample size is larger than the population size, a `ValueError` is raised.
<br/><br/>
## shuffle()
*Syntax* : `random.shuffle(seq)`

Shuffles the sequence `seq` in place.

#### Example :
```python
import random
list_1 = [1, 2, 3, 4, 5]
print("Before shuffling : ", list_1)
random.shuffle(list_1)
print("After shuffling : ", list_1)
```

#### Output :
```python
Before shuffling :  [1, 2, 3, 4, 5]
After shuffling :  [4, 1, 3, 2, 5]
```

*Note* :
- `shuffle()` cannot be directly used with sets, dictionaries, tuples, or strings because they are immutable or unordered collections.
- To shuffle elements of sets, tuples, or strings, you need to convert them to lists first, shuffle the list, and then convert it back if necessary.
<br/><br/>
## seed()
*Syntax* : `random.seed(a=None, version=2)`
- By default, random number generator uses current system time as seed value. seed() function is used to initialize random number generator.
- Same seed value generated same random numbers.
- If the parameter `a` is omitted or `None`, the current system time is used.
  
#### Example :
```python
import random
random.seed()
print("For default seed value: ", random.randint(1, 20))
random.seed()
print("For default seed value: ", random.randint(1, 20))

random.seed(2)
print("For seed value = 2: " , random.randint(1, 20))
random.seed(2)
print("For seed value = 2: " , random.randint(1, 20))

print("After resetting the seed value to default: ", random.randint(1, 20))
```

#### Output :
```python
For default seed value:  20
For default seed value:  13
For seed value = 2:  2
For seed value = 2:  2
After resetting the seed value to default:  3
```

In the above example, the first two outputs are different because the default seed value is set based on the current time, which changes every time the program runs. In the next two lines, the same number is generated twice because the seed value is explicitly set to 2 before each random number generation. In the last line, even though the seed value isn't specified, it's reset to the default seed value (based on the current time) implicitly.
<br/><br/>
## getrandbits()
*Syntax* : `random.getrandbits(k)`

Returns a non-negative Python integer with k random bits. 

#### Example :
```python
import random
for i in range(3):
    print(random.getrandbits(4))

print(random.getrandbits(0)) # number of bits as zero
```

#### Output :
```python
6
10
13
0
```

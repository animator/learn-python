# Viewing rows of the frame 

## `head()` method

The pandas library in Python provides a convenient method called `head()` that allows you to view the first few rows of a DataFrame. Let me explain how it works:
- The `head()` function returns the first n rows of a DataFrame or Series.
- By default, it displays the first 5 rows, but you can specify a different number of rows using the n parameter.

### Syntax

```python
dataframe.head(n)
```
     
`n` is the Optional value. The number of rows to return. Default value is `5`.

### Example

```python
import pandas as pd
df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion','tiger','rabit','dog','fox','monkey','elephant']})
df.head(n=5)
```

#### Output

```
      animal
0  alligator
1        bee
2     falcon
3       lion
4      tiger
```

## `tail()` method

The `tail()` function in Python displays the last five rows of the dataframe by default. It takes in a single parameter: the number of rows. We can use this parameter to display the number of rows of our choice.
- The `tail()` function returns the last n rows of a DataFrame or Series.
- By default, it displays the last 5 rows, but you can specify a different number of rows using the n parameter.

### Syntax

```python
dataframe.tail(n)
```

`n` is the Optional value. The number of rows to return. Default value is `5`.

### Example

```python
import pandas as pd
df = pd.DataFrame({'fruits': ['mongo', 'orange', 'apple', 'lemon','banana','water melon','papaya','grapes','cherry','coconut']})
df.tail(n=5)
```

#### Output

```
        fruits
5  water melon
6       papaya
7       grapes
8       cherry
9      coconut
```

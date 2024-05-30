# Working with Date & Time in Pandas

While working with data, it is common to come across data containing date and time. Pandas is a very handy tool for dealing with such data and provides a wide range of date and time data processing options.

- **Parsing dates and times**: Pandas provides a number of functions for parsing dates and times from strings, including `to_datetime()` and `parse_dates()`. These functions can handle a variety of date and time formats, Unix timestamps, and human-readable formats.

- **Manipulating dates and times**: Pandas provides a number of functions for manipulating dates and times, including `shift()`, `resample()`, and `to_timedelta()`. These functions can be used to add or subtract time periods, change the frequency of a time series, and calculate the difference between two dates or times.

- **Visualizing dates and times**: Pandas provides a number of functions for visualizing dates and times, including `plot()`, `hist()`, and `bar()`. These functions can be used to create line charts, histograms, and bar charts of date and time data.

### `Timestamp` function

The timestamp function in Pandas is used to convert a datetime object to a Unix timestamp. A Unix timestamp is a numerical representation of datetime.

Example for retrieving day, month and year from given date:

```python
import pandas as pd

ts = pd.Timestamp('2024-05-05')
y = ts.year
print('Year is: ', y)
m = ts.month
print('Month is: ', m)
d = ts.day
print('Day is: ', d)
```

Output:

```python
Year is:  2024
Month is:  5
Day is:  5
```

Example for extracting time related data from given date:

```python
import pandas as pd

ts = pd.Timestamp('2024-10-24 12:00:00')
print('Hour is: ', ts.hour)
print('Minute is: ', ts.minute)
print('Weekday is: ', ts.weekday())
print('Quarter is: ', ts.quarter)
```

Output:

```python
Hour is:  12
Minute is:  0
Weekday is:  1
Quarter is:  4
```

### `Timestamp.now()`

Example for getting current date and time:

```python
import pandas as pd

ts = pd.Timestamp.now()
print('Current date and time is: ', ts)
```

Output:
```python
Current date and time is:  2024-05-25 11:48:25.593213
```

### `date_range` function

Example for generating dates' for next five days:

```python
import pandas as pd

ts = pd.date_range(start = pd.Timestamp.now(), periods = 5)
for i in ts:
    print(i.date())
```

Output:

```python
2024-05-25
2024-05-26
2024-05-27
2024-05-28
2024-05-29
```

Example for generating dates' for previous five days:

```python
import pandas as pd

ts = pd.date_range(end = pd.Timestamp.now(), periods = 5)
for i in ts:
    print(i.date())
```

Output:
```python
2024-05-21
2024-05-22
2024-05-23
2024-05-24
2024-05-25
```

### Built-in vs pandas date & time operations

In `pandas`, you may add a time delta to a full column of dates in a single action, but Python's datetime requires a loop.

Example in Pandas:

```python
import pandas as pd

dates = pd.DataFrame(pd.date_range('2023-01-01', periods=100000, freq='T'))
dates += pd.Timedelta(days=1)
print(dates)
```

Output:
```python
                    0
0     2023-01-02 00:00:00
1     2023-01-02 00:01:00
2     2023-01-02 00:02:00
3     2023-01-02 00:03:00
4     2023-01-02 00:04:00
...                   ...
99995 2023-03-12 10:35:00
99996 2023-03-12 10:36:00
99997 2023-03-12 10:37:00
99998 2023-03-12 10:38:00
99999 2023-03-12 10:39:00
```

Example using Built-in datetime library:

```python
from datetime import datetime, timedelta

dates = [datetime(2023, 1, 1) + timedelta(minutes=i) for i in range(100000)]
dates = [date + timedelta(days=1) for date in dates]
```

Why use pandas functions?

- Pandas employs NumPy's datetime64 dtype, which takes up a set amount of bytes (usually 8 bytes per date), to store datetime data more compactly and efficiently.
- Each datetime object in Python takes up extra memory since it contains not only the date and time but also the additional metadata and overhead associated with Python objects.
- Pandas Offers a wide range of convenient functions and methods for date manipulation, extraction, and conversion, such as `pd.to_datetime()`, `date_range()`, `timedelta_range()`, and more. datetime library requires manual implementation for many of these operations, leading to longer and less efficient code.

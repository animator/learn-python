# Pandas DateTime

Pandas is a robust Python library that is available as free source. The Pandas library is used to manipulate and analyse data. Pandas are made up of data structures and functions that allow for efficient data processing.

While working with data, it is common to come across time series data. Pandas is a very handy tool for dealing with time series data. Pandas is a strong Python data analysis toolkit that provides a wide range of date and time data processing options. Many data science jobs require working with time series data, time zones, and date arithmetic, and pandas simplifies these processes.

Features of Pandas `Date_Time`:

- **Parsing dates and times**: Pandas provides a number of functions for parsing dates and times from strings, including `to_datetime()` and `parse_dates()`. These functions can handle a variety of date and time formats, Unix timestamps, and human-readable formats.

- **Manipulating dates and times**: Pandas provides a number of functions for manipulating dates and times, including `shift()`, `resample()`, and `to_timedelta()`. These functions can be used to add or subtract time periods, change the frequency of a time series, and calculate the difference between two dates or times.

- **Visualizing dates and times**: Pandas provides a number of functions for visualizing dates and times, including `plot()`, `hist()`, and `bar()`. These functions can be used to create line charts, histograms, and bar charts of date and time data.



### Installation of libraries

`pip install pandas`

- **Note**: There is no need to install a seperate library for date_time operations, pandas module itself has built-in functions.

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

- **Note**: The timestamp function in Pandas is used to convert a datetime object to a Unix timestamp. A Unix timestamp is a numerical representation of datetime.


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


# Working with Date and Time using Pandas

Pandas is a very useful tool while working with time series data. It provides a different set of tools using which we can perform all the necessary tasks on date-time data.

## Working with dates in Pandas

The date class in the DateTime module of Python deals with dates in the Gregorian calendar. It accepts three integer arguments: year, month, and day. For example:

### Code
```python
from datetime import date

d= date(2024,5,22)

print(d,end=' ')

print(type(d))
```

### Output
`2000-09-17
<class 'datetime.date'>`

## Using Timestamp object

- Retrieveing year, month and day component using Timestamp.

### Code

```python
import pandas as pd

# Creating a Timestamp object
timestamp = pd.Timestamp('2023-05-22 19:14:47')

# Extracting the year from the Timestamp
year = timestamp.year

# Printing the extracted year
print("Year:", year, end=' ')

# Extracting the month from the Timestamp
month = timestamp.month

# Printing the extracted month
print("Month", month, end=' ')

# Extracting the day from the Timestamp
day = timestamp.day

# Printing the extracted day
print("Day:", day, end=' ')
```

### Output
`Year:2024
Month:05 
Day:22`

## Working with time in Pandas

Another class in the DateTime module is called time, which returns a DateTime object and takes integer arguments for time intervals up to microseconds. For example,

### Code

```python
from datetime import time

t = time(12,50,12,40)

print(t)

print(type(t))
```

### Output
`19:33:20.000034
<class 'datetime.time'>`

## Handling Timezones

Time zones play a crucial role in date and time data. Pandas has a set of operations to handle timezones effectively.

- UTC and time zone conversion: Convert between UTC (Coordinated Universal Time) and local time zones.
- Time zone-aware data manipulation: Work with time zone-aware data, ensuring accurate date and time interpretations.
- Custom time zone settings: Specify custom time zone settings for data analysis and visualization.

```python
import pandas as pd

# Creating a Timestamp object with a specific time zone
timestamp = pd.Timestamp('2024-05-22 19:38:21',tz='America/New_York')

print(timestamp)

# Converting the Timestamp to UTC
utc_timestamp = timestamp.utcfromtz('America/New_York')

print(utc_timestamp)

# Converting the UTC timestamp back to the original time zone
original_timestamp = utc_timestamp.tz_localize('America/New_York')

print(original_timestamp)

datetime_index = pd.DatetimeIndex(['2024-05-22',
								'2024-05-24', 
								'2024-05-28'],
								tz='Asia/Shanghai')

print(datetime_index)

utc_datetime_index = datetime_index.utcfromtz('Asia/Shanghai')

print(utc_datetime_index)


original_datetime_index = utc_datetime_index.tz_localize(
												'Asia/Shanghai')


print(original_datetime_index)
```

## Working with date&time in Pandas

Pandas provide convenient methods to extract specific date and time components from Timestamp objects. Such as:

- Creating a dates dataframe using,
`data = pd.date_range('22/5/2024', periods = 10, freq ='H')`

- Creating range of dates and applying operations using,
```python
data = pd.date_range('22/5/2024', periods = 10, freq ='H')
x = pd.datetime.now()
```
- Dividing date into features using,
pandas.Series.dt.year returns the year of the date time. 
pandas.Series.dt.month returns the month of the date time. 
pandas.Series.dt.day returns the day of the date time. 
pandas.Series.dt.hour returns the hour of the date time. 
pandas.Series.dt.minute returns the minute of the date time.

- To get present time using Timestamp.now() or to_datetime()
`t = pandas.tslib.Timestamp.now()`

or,

`t.to_datetime()`

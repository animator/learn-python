# Plotting & Visualization with Matplotlib

## Introduction to Matplotlib

### Overview of Matplotlib
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is highly customizable and supports a wide range of plot types, making it a versatile tool for data visualization.

### Installation and Setup
Before you can use Matplotlib, you need to install it. You can install Matplotlib using pip, Python's package manager:

```
pip install matplotlib
```

### Basic Usage and Structure of a Matplotlib Plot
Once installed, you can start using Matplotlib to create plots. A basic Matplotlib plot involves creating a figure and adding one or more axes (plots) to it.

```python
import matplotlib.pyplot as plt

# Create a figure and an axes
fig, ax = plt.subplots()

# Plot some data on the axes
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# Display the plot
plt.show()
```

### Basic Plotting Functions
Creating Line Charts
Line charts are useful for visualizing trends over time or continuous data. Here's how to create a simple line chart:

```python

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x, y)
plt.title('Line Chart')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```
### Creating Scatter Plots
Scatter plots are used to visualize the relationship between two variables. Each point represents an observation.

```python

import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```
### Creating Bar Charts
Bar charts are useful for comparing different categories or groups. Each bar represents a category.
```python

import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y = [3, 7, 8, 5]

plt.bar(x, y)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
```
### Creating Histograms
Histograms are used to visualize the distribution of a dataset. They show the frequency of different ranges of values.

```python

import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

## Customising Plots
Customising Markers, Colours, and Line Styles
You can customize the appearance of plots by changing markers, colors, and line styles.

```python

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x, y, marker='o', color='r', linestyle='--')
plt.title('Custom Line Chart')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```
## Adding Titles and Labels
Titles and labels help to provide context and make the plot easier to understand.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x, y)
plt.title('Line Chart with Titles and Labels')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

## Adding Legends
Legends are useful when you have multiple plots on the same figure and need to differentiate between them.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 2, 3]
y2 = [2, 2, 3, 4]

plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.title('Line Chart with Legends')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend()
plt.show()
```
## Adding Grid Lines
Grid lines can make your plot easier to read by providing reference points.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x, y)
plt.title('Line Chart with Grid Lines')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()
```

## Saving Plots
You can save your plots to a file in various formats such as PNG, PDF, SVG, etc.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x, y)
plt.title('Line Chart')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.savefig('line_chart.png')
plt.show()
```
## Conclusion

In conclusion, this guide offers a comprehensive introduction to Matplotlib, covering installation, basic plot creation, and customization options. It serves as a starting point for further exploration of Matplotlib's advanced features and capabilities.

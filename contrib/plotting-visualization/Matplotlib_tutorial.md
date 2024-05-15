# Comprehensive Matplotlib Tutorial

Matplotlib is a powerful plotting library for Python, widely used for data visualization. This tutorial will guide you through everything from basic plotting to more advanced customization options, starting from scratch.

### Introduction to Matplotlib

Matplotlib is versatile and can create static, animated, and interactive visualizations. It's especially useful for data analysis and is widely used in scientific and engineering communities.

![Alt text](https://i.imgur.com/9i806Rh.png "Introduction")

### Installation

You can install Matplotlib using pip. Open your terminal or command prompt and run:

```bash

pip install matplotlib

```

### Basic Concepts

#### Figure and Axes

In Matplotlib, the `Figure` is the overall window or page that everything is drawn on, while `Axes` are the individual plots or graphs within the `Figure`.

#### Plotting a Simple Graph

Here's a basic example of how to plot a simple line graph:

```python

import matplotlib.pyplot as plt

# Sample data

x = [1, 2, 3, 4, 5]

y = [2, 3, 5, 7, 11]

# Create a plot

plt.plot(x, y)

# Show the plot

plt.show()

```

This code will display a simple line plot of the given data.

![Alt text](https://www.w3schools.com/python/img_matplotlib_plotting1.png "Introduction")

### Customizing Plots

#### Titles and Labels

You can add titles and labels to your plots to make them more informative:

```python

plt.plot(x, y)

# Adding title and labels

plt.title('Sample Line Plot')

plt.xlabel('X-axis Label')

plt.ylabel('Y-axis Label')

plt.show()

```

#### Legends

Legends help in identifying different plots on the same graph. Here's how to add them:

```python

# Sample data for two lines

x = [1, 2, 3, 4, 5]

y1 = [2, 3, 5, 7, 11]

y2 = [1, 4, 6, 8, 10]

# Plotting two lines

plt.plot(x, y1, label='Prime Numbers')

plt.plot(x, y2, label='Composite Numbers')

# Adding legend

plt.legend()

plt.show()

```

#### Colors and Styles

You can customize the appearance of your plots with colors and line styles:

```python

# Different styles

plt.plot(x, y1, color='blue', linestyle='-', marker='o', label='Prime')

plt.plot(x, y2, color='red', linestyle='--', marker='x', label='Composite')

plt.legend()

plt.show()

```

![Alt text](https://www.includehelp.com/python/images/line-plot.jpg "Introduction")

### Types of Plots

#### Line Plots

Line plots are useful for showing trends over time or continuous data:

```python

plt.plot(x, y)

plt.show()

```

![Alt text](https://www.w3schools.com/python/img_matplotlib_line_red.png) "Introduction")

#### Scatter Plots

Scatter plots are used to show the relationship between two sets of data:

```python

plt.scatter(x, y)

plt.show()

```
![Alt text](https://www.w3schools.com/python/img_scatterplot.png "Introduction")

#### Bar Plots

Bar plots are great for categorical data comparison:

```python

categories = ['A', 'B', 'C', 'D', 'E']

values = [5, 7, 3, 8, 6]

plt.bar(categories, values)

plt.show()

```
![Alt text](https://www.w3schools.com/python/img_matplotlib_bars1.png "Introduction")

#### Histograms

Histograms are used to show the distribution of a dataset:

```python

import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30)

plt.show()

```
![Alt text](https://media.geeksforgeeks.org/wp-content/uploads/20231205223137/Screenshot-2023-12-05-222229.png "Introduction")

#### Pie Charts

Pie charts are useful for showing proportions:

```python

sizes = [15, 30, 45, 10]

labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.show()

```

![Alt text](https://www.w3schools.com/python/img_matplotlib_pie_labels.png "Introduction")

### Saving and Showing Plots

You can save your plots to a file instead of showing them:

```python

plt.plot(x, y)

plt.savefig('plot.png')

plt.show()  # Optional, to display the plot

```


### Subplots

Subplots allow you to create multiple plots in a single figure. This is useful for comparing different datasets or visualizing multiple dimensions of the same data.

**Basic Subplot Creation:**

```python

import matplotlib.pyplot as plt

# Create a figure and an array of subplots with 2 rows and 2 columns

fig, axs = plt.subplots(2, 2)

# Plot different types of plots in each subplot

axs[0, 0].plot([1, 2, 3], [1, 4, 9])  # Line plot

axs[0, 1].scatter([1, 2, 3], [1, 4, 9])  # Scatter plot

axs[1, 0].bar(['A', 'B', 'C'], [5, 7, 3])  # Bar plot

axs[1, 1].hist([1, 2, 2, 3, 3, 3, 4], bins=3)  # Histogram

# Show the figure with subplots

plt.show()

```

![Alt text](https://www.w3schools.com/python/img_matplotlib_subplots1.png "Introduction")

**Customizing Subplots:**

You can adjust the layout and appearance of your subplots using various parameters.

```python

fig, axs = plt.subplots(2, 2, figsize=(10, 10), gridspec_kw={'width_ratios': [2, 1]})

# Adjust spacing between subplots

fig.tight_layout(pad=3.0)

axs[0, 0].plot([1, 2, 3], [1, 4, 9])

axs[0, 0].set_title('Line Plot')

axs[0, 1].scatter([1, 2, 3], [1, 4, 9])

axs[0, 1].set_title('Scatter Plot')

axs[1, 0].bar(['A', 'B', 'C'], [5, 7, 3])

axs[1, 0].set_title('Bar Plot')

axs[1, 1].hist([1, 2, 2, 3, 3, 3, 4], bins=3)

axs[1, 1].set_title('Histogram')

plt.show()

```

![Alt text](https://cdn.analyticsvidhya.com/wp-content/uploads/2024/02/example-3.png "Snapshot 3")


### Plotting with Pandas

Pandas integrates seamlessly with Matplotlib, making it easier to create plots from DataFrames. Here's how you can leverage this integration.

**Basic Pandas Plotting:**

```python

import pandas as pd

# Create a DataFrame

data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [23, 45, 56, 78]}

df = pd.DataFrame(data)

# Plot a bar graph directly from the DataFrame

df.plot(kind='bar', x='Category', y='Values', legend=False)

plt.title('Bar Plot from DataFrame')

plt.show()

```

**Advanced Pandas Plotting:**

You can create more complex plots and customize them further.

```python

# Create a DataFrame

data = {'Category': ['A', 'B', 'C', 'D'],

        'Values1': [23, 45, 56, 78],

        'Values2': [22, 43, 55, 77]}

df = pd.DataFrame(data)

# Plot multiple columns

df.plot(kind='bar', x='Category', y=['Values1', 'Values2'])

plt.title('Multiple Columns Bar Plot')

plt.xlabel('Category')

plt.ylabel('Values')

plt.legend(title='Legend')

plt.show()

```




### Conclusion

This comprehensive tutorial should give you a solid foundation in Matplotlib. You can further explore its extensive documentation and experiment with different types of plots and customizations to deepen your understanding. Happy plotting!

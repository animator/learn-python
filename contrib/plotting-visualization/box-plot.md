# Box Plot 

A box plot represents the distribution of a dataset in a graph. It displays the summary statistics of a dataset, including the minimum, first quartile (Q1), median (Q2), third quartile (Q3), and maximum. The box represents the interquartile range (IQR) between the first and third quartiles, while whiskers extend from the box to the minimum and maximum values. Outliers, if present, may be displayed as individual points beyond the whiskers.
For example - Imagine you have the exam scores of students from three classes. A box plot is a way to show how these scores are spread out.

## Key Ranges in Data Distribution 

The data can be distributed between five key ranges, which are as follows - 
1. Minimum: Q1-1.5*IQR
2. 1st quartile (Q1): 25th percentile
3. Median: 50th percentile
4. 3rd quartile(Q3): 75th percentile
5. Maximum: Q3+1.5*IQR

## Purpose of Box Plots

We can create the box plot of the data to determine the following- 
1. The number of outliers in a dataset
2. Is the data skewed or not (skewness is a measure of asymmetry of the distribution) 
3. The range of the data

## Creating Box Plots using Matplotlib

By using inbuilt funtion boxplot() of pyplot module of matplotlib - 

Syntax - matplotlib.pyplot.boxplot(data,notch=none,vert=none,patch_artist,widths=none)  

1. data: The data should be an array or sequence of arrays which will be plotted.
2. notch: This parameter accepts only Boolean values, either true or false.
3. vert: This attribute accepts a Boolean value. If it is set to true, then the graph will be vertical. Otherwise, it will be horizontal.
4. position: It accepts the array of integers which defines the position of the box.
5. widths: It accepts the array of integers which defines the width of the box.
6. patch_artist: this parameter accepts Boolean values, either true or false, and this is an optional parameter.
7. labels: This accepts the strings which define the labels for each data point
8. meanline: It accepts a boolean value, and it is optional.
9. order: It sets the order of the boxplot.
10. bootstrap: It accepts the integer value, which specifies the range of the notched boxplot.

## Implementation of Box Plot in Python

### Import libraries
import matplotlib.pyplot as plt
import numpy as np 

### Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200) 
fig = plt.figure(figsize =(10, 7))

### Creating plot
plt.boxplot(data)

### show plot
plt.show()

### Implementation of Multiple Box Plot in Python
import matplotlib.pyplot as plt  
import numpy as np  
np.random.seed(10)  
dataSet1 = np.random.normal(100, 10, 220)  
dataSet2 = np.random.normal(80, 20, 200)  
dataSet3 = np.random.normal(60, 35, 220)  
dataSet4 = np.random.normal(50, 40, 200)  
dataSet = [dataSet1, dataSet2, dataSet3, dataSet4]  
figure = plt.figure(figsize =(10, 7))  
ax = figure.add_axes([0, 0, 1, 1])  
bp = ax.boxplot(dataSet)  
plt.show()  

### Implementation of Box Plot with Outliers (visual representation of the sales distribution for each product, and the outliers highlight months with exceptionally high or low sales)
import matplotlib.pyplot as plt
import numpy as np

### Data for monthly sales
product_A_sales = [100, 110, 95, 105, 115, 90, 120, 130, 80, 125, 150, 200]
product_B_sales = [90, 105, 100, 98, 102, 105, 110, 95, 112, 88, 115, 250]
product_C_sales = [80, 85, 90, 78, 82, 85, 88, 92, 75, 85, 200, 95]

### Introducing outliers 
product_A_sales.extend([300, 80])
product_B_sales.extend([50, 300])
product_C_sales.extend([70, 250])

### Creating a box plot with outliers
plt.boxplot([product_A_sales, product_B_sales, product_C_sales], sym='o')
plt.title('Monthly Sales Performance by Product with Outliers')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()

### Implementation of Grouped Box Plot (to compare the exam scores of students from three different classes (A, B, and C))
import matplotlib.pyplot as plt
import numpy as np
class_A_scores = [75, 80, 85, 90, 95]
class_B_scores = [70, 75, 80, 85, 90]
class_C_scores = [65, 70, 75, 80, 85]

### Creating a grouped box plot
plt.boxplot([class_A_scores, class_B_scores, class_C_scores], labels=['Class A', 'Class B', 'Class C'])
plt.title('Exam Scores by Class')
plt.xlabel('Classes')
plt.ylabel('Scores')
plt.show()

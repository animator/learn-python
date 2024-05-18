# Stripplot 
A stripplot is a type of data visualization used in statistical graphics to display the distribution of a dataset along a categorical axis. It is essentially a scatter plot where one of the axes represents a categorical variable. Each data point is plotted as an individual marker along the continuous axis, which helps in visualizing the spread and density of data points in relation to different categories.
 
## Example Usage
A common use case for a stripplot is to compare the distribution of a continuous variable across different groups or categories. For instance, comparing the distribution of test scores across different classes.

## Python program to illustrate Stripplot using inbuilt data-set given in seaborn 

```sh
# Python program to illustrate Plotting categorical scatter plots with Seaborn 
  
# importing the required module 
import matplotlib.pyplot as plt 
import seaborn as sns 
  
# x axis values 
x =['sun', 'mon', 'fri', 'sat', 'tue', 'wed', 'thu'] 
  
# y axis values 
y =[5, 6.7, 4, 6, 2, 4.9, 1.8] 
  
# plotting strip plot with seaborn 
ax = sns.stripplot(x, y); 
  
# giving labels to x-axis and y-axis 
ax.set(xlabel ='Days', ylabel ='Amount_spend') 
  
# giving title to the plot 
plt.title('My first graph'); 
  
# function to show plot 
plt.show()
```
## Output
<img src="https://media.geeksforgeeks.org/wp-content/uploads/seaborn1.png" width="500" height="300" />

## Using iris dataset
```sh
# Python program to illustrate Stripplot using inbuilt data-set given in seaborn 
  
# importing the required module 
import matplotlib.pyplot as plt 
import seaborn as sns 
  
# use to set style of background of plot 
sns.set(style="whitegrid") 
  
# loading data-set 
iris = sns.load_dataset('iris') 

# deciding the attributes of dataset on which plot should be made 
ax = sns.stripplot(x='species', y='sepal_length', data=iris) 
  
# giving title to the plot 
plt.title('Graph') 
  
# function to show plot 
plt.show() 
```
### Output
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20201105184425/Capture-300x195.PNG" width="400" height="300" />


## Explanations
iris is the dataset already present in seaborn module for use.

We use .load_dataset() function in order to load the data.We can also load any other file by giving the path and name of the file in the argument.

.set(style=”whitegrid”) function here is also use to define the background of plot.We can use “darkgrid” instead of whitegrid if we want the dark-colored background.

In .stripplot() function we have to define which attribute of the dataset to be on the x-axis and which attribute of the dataset should on y-axis.data = iris means attributes which we define earlier should be taken from the given data.


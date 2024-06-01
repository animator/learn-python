## Group By Functions

GroupBy is a powerful function in pandas that allows you to split data into distinct groups based on one or more columns and perform operations on each group independently. It's a fundamental technique for data analysis and summarization.

Here's a step-by-step breakdown of how groupby functions work in pandas:

* __Splitting the Data:__  You can group your data based on one or more columns using the .groupby() method. This method takes a column name or a list of column names as input and splits the DataFrame into groups according to the values in those columns.

* __Applying a Function:__ Once the data is grouped, you can apply various functions to each group. Pandas offers a variety of built-in aggregation functions like sum(), mean(), count(), etc., that can be used to summarize the data within each group. You can also use custom functions or lambda functions for more specific operations.

* __Combining the Results:__ After applying the function to each group, the results are combined into a new DataFrame or Series, depending on the input data and the function used. This new data structure summarizes the data by group.


```python
import pandas as pd
import seaborn as sns
import numpy as np
```


```python
iris_data = sns.load_dataset('iris')
```

This code loads the built-in Iris dataset from seaborn and stores it in a pandas DataFrame named iris_data. The Iris dataset contains measurements of flower sepal and petal dimensions for three Iris species (Setosa, Versicolor, Virginica).


```python
iris_data
```

|    | sepal_length | sepal_width | petal_length | petal_width | species   |
|----|--------------|-------------|--------------|-------------|-----------|
| 0  | 5.1          | 3.5         | 1.4          | 0.2         | setosa    |
| 1  | 4.9          | 3.0         | 1.4          | 0.2         | setosa    |
| 2  | 4.7          | 3.2         | 1.3          | 0.2         | setosa    |
| 3  | 4.6          | 3.1         | 1.5          | 0.2         | setosa    |
| 4  | 5.0          | 3.6         | 1.4          | 0.2         | setosa    |
| ...| ...          | ...         | ...          | ...         | ...       |
| 145| 6.7          | 3.0         | 5.2          | 2.3         | virginica |
| 146| 6.3          | 2.5         | 5.0          | 1.9         | virginica |
| 147| 6.5          | 3.0         | 5.2          | 2.0         | virginica |
| 148| 6.2          | 3.4         | 5.4          | 2.3         | virginica |
| 149| 5.9          | 3.0         | 5.1          | 1.8         | virginica |





```python
iris_data.groupby(['species']).count()
```




| species    | sepal_length | sepal_width | petal_length | petal_width |
|------------|--------------|-------------|--------------|-------------|
| setosa     | 50           | 50          | 50           | 50          |
| versicolor | 50           | 50          | 50           | 50          |
| virginica  | 50           | 50          | 50           | 50          |




* We group the data by the 'species' column.
count() is applied to each group, which counts the number of occurrences (rows) in each species category.
* The output (species_counts) is a DataFrame showing the count of each species in the dataset.


```python
iris_data.groupby(["species"])["sepal_length"].mean()
```




  species
  setosa        5.006\
  versicolor    5.936\
  virginica     6.588\
  Name: sepal_length, dtype: float64



* This groups the data by 'species' and selects the 'sepal_length' column.
mean() calculates the average sepal length for each species group.
* The output (species_means) is a Series containing the mean sepal length for each species.


```python
iris_data.groupby(["species"])["sepal_length"].std()
```




  species
  setosa        0.352490\
  versicolor    0.516171\
  virginica     0.635880\
  Name: sepal_length, dtype: float64



* Similar to the previous, this groups by 'species' and selects the 'sepal_length' column.
However, it calculates the standard deviation (spread) of sepal length for each species group using std().
* The output (species_std) is a Series containing the standard deviation of sepal length for each species


```python
iris_data.groupby(["species"])["sepal_length"].describe()
```



| species    | count | mean  | std      | min  | 25%    | 50%  | 75%  | max  |
|------------|-------|-------|----------|------|--------|------|------|------|
| setosa     | 50.0  | 5.006 | 0.352490 | 4.3  | 4.800  | 5.0  | 5.2  | 5.8  |
| versicolor | 50.0  | 5.936 | 0.516171 | 4.9  | 5.600  | 5.9  | 6.3  | 7.0  |
| virginica  | 50.0  | 6.588 | 0.635880 | 4.9  | 6.225  | 6.5  | 6.9  | 7.9  |




* We have used describe() to generate a more comprehensive summary of sepal length for each species group.
* It provides statistics like count, mean, standard deviation, minimum, maximum, percentiles, etc.
The output (species_descriptions) is a DataFrame containing these descriptive statistics for each species.


```python
iris_data.groupby(["species"])["sepal_length"].quantile(q=0.25)
```




  species\
  setosa        4.800\
  versicolor    5.600\
  virginica     6.225\
  Name: sepal_length, dtype: float64




```python
iris_data.groupby(["species"])["sepal_length"].quantile(q=0.75)
```




  species\
  setosa        5.2\
  versicolor    6.3\
  virginica     6.9\
  Name: sepal_length, dtype: float64



* To calculate the quartiles (25th percentile and 75th percentile) of sepal length for each species group.
* quantile(q=0.25) gives the 25th percentile, which represents the value below which 25% of the data points lie.
* quantile(q=0.75) gives the 75th percentile, which represents the value below which 75% of the data points lie.
* The outputs (species_q1 and species_q3) are Series containing the respective quartile values for each species.

## Custom Function For Group By


```python
nc = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']
```


```python
nc
```




  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']




```python
nc = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
def species_stats(species_data,species_name):
        print("Species Name: {}".format(species_name))
        print()
        print("Mean:\n",species_data[nc].mean())
        print()
        print("Median:\n",species_data[nc].median())
        print()
        print("std:\n",species_data[nc].std())
        print()
        print("25% percentile:\n",species_data[nc].quantile(0.25))
        print()
        print("75% percentile:\n",species_data[nc].quantile(0.75))
        print()
        print("Min:\n",species_data[nc].min())
        print()
        print("Max:\n",species_data[nc].max())
        print()
```


```python
setosa_data = iris_data[iris_data['species'] == 'setosa']
```


```python
versicolor_data = iris_data[iris_data['species'] == 'versicolor']
```


```python
virginica_data = iris_data[iris_data['species'] == 'virginica']
```


```python
species_data_names = ['setosa_data','viginica_data','versicolor_data']
for data in species_data_names:
    print("************** Species name {} *****************".format(data))
    species_stats(setosa_data,data)
    print("------------------------------------")
```

  ************** Species name setosa_data *****************\
  Species Name: setosa_data 
  
  Mean:\
    sepal_length    5.006\
  sepal_width     3.428\
  petal_length    1.462\
  petal_width     0.246\
  dtype: float64
  
  Median:\
    sepal_length    5.0\
  sepal_width     3.4\
  petal_length    1.5\
  petal_width     0.2\
  dtype: float64
  
  std:\
    sepal_length    0.352490\
  sepal_width     0.379064\
  petal_length    0.173664\
  petal_width     0.105386\
  dtype: float64
  
  25% percentile:\
    sepal_length    4.8\
  sepal_width     3.2\
  petal_length    1.4\
  petal_width     0.2\
  Name: 0.25, dtype: float64
  
  75% percentile:\
    sepal_length    5.200\
  sepal_width     3.675\
  petal_length    1.575\
  petal_width     0.300\
  Name: 0.75, dtype: float64
  
  Min:\
    sepal_length    4.3\
  sepal_width     2.3\
  petal_length    1.0\
  petal_width     0.1\
  dtype: float64
  
  Max:
    sepal_length    5.8\
  sepal_width     4.4\
  petal_length    1.9\
  petal_width     0.6\
  dtype: float64
  
  ------------------------------------\
  ************** Species name viginica_data *****************\
  Species Name: viginica_data
  
  Mean:\
    sepal_length    5.006\
  sepal_width     3.428\
  petal_length    1.462\
  petal_width     0.246\
  dtype: float64
  
  Median:\
    sepal_length    5.0\
  sepal_width     3.4\
  petal_length    1.5\
  petal_width     0.2\
  dtype: float64
  
  std:\
    sepal_length    0.352490\
  sepal_width     0.379064\
  petal_length    0.173664\
  petal_width     0.105386\
  dtype: float64
  
  25% percentile:\
    sepal_length    4.8\
  sepal_width     3.2\
  petal_length    1.4\
  petal_width     0.2\
  Name: 0.25, dtype: float64
  
  75% percentile:\
    sepal_length    5.200\
  sepal_width     3.675\
  petal_length    1.575\
  petal_width     0.300\
  Name: 0.75, dtype: float64
  
  Min:\
    sepal_length    4.3\
  sepal_width     2.3\
  petal_length    1.0\
  petal_width     0.1\
  dtype: float64
  
  Max:
    sepal_length    5.8
  sepal_width     4.4
  petal_length    1.9
  petal_width     0.6
  dtype: float64
  
  ------------------------------------\
  ************** Species name versicolor_data *****************\
  Species Name: versicolor_data
  
  Mean:\
    sepal_length    5.006\
  sepal_width     3.428\
  petal_length    1.462\
  petal_width     0.246\
  dtype: float64
  
  Median:\
    sepal_length    5.0\
  sepal_width     3.4\
  petal_length    1.5\
  petal_width     0.2\
  dtype: float64
  
  std:\
    sepal_length    0.352490\
  sepal_width     0.379064\
  petal_length    0.173664\
  petal_width     0.105386\
  dtype: float64
  
  25% percentile:\
    sepal_length    4.8\
  sepal_width     3.2\
  petal_length    1.4\
  petal_width     0.2\
  Name: 0.25, dtype: float64
  
  75% percentile:\
    sepal_length    5.200\
  sepal_width     3.675\
  petal_length    1.575\
  petal_width     0.300\
  Name: 0.75, dtype: float64
  
  Min:
    sepal_length    4.3\
  sepal_width     2.3\
  petal_length    1.0\
  petal_width     0.1\
  dtype: float64
  
  Max:\
    sepal_length    5.8\
  sepal_width     4.4\
  petal_length    1.9\
  petal_width     0.6\
  dtype: float64
  
  ------------------------------------
  

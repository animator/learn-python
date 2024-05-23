## Descriptive Statistics

In the realm of data science, understanding the characteristics of data is fundamental. Descriptive statistics provide the tools and techniques to succinctly summarize and present the key features of a dataset. It serves as the cornerstone for exploring, visualizing, and ultimately gaining insights from data.

Descriptive statistics encompasses a range of methods designed to describe the central tendency, dispersion, and shape of a dataset. Through measures such as mean, median, mode, standard deviation, and variance, descriptive statistics offer a comprehensive snapshot of the data's distribution and variability.

Data scientists utilize descriptive statistics to uncover patterns, identify outliers, and assess the overall structure of data before delving into more advanced analyses. By summarizing large and complex datasets into manageable and interpretable summaries, descriptive statistics facilitate informed decision-making and actionable insights.


```python
import pandas as pd
import numpy as np

df = pd.read_csv("Age-Income-Dataset.csv")
df
```

|     | Age         | Income |
| --- | ----------- | ------ |
| 0   | Young       | 25000  |
| 1   | Middle Age  | 54000  |
| 2   | Old         | 60000  |
| 3   | Young       | 15000  |
| 4   | Young       | 45000  |
| 5   | Young       | 65000  |
| 6   | Young       | 70000  |
| 7   | Young       | 30000  |
| 8   | Middle Age  | 27000  |
| 9   | Young       | 23000  |
| 10  | Young       | 48000  |
| 11  | Old         | 52000  |
| 12  | Young       | 33000  |
| 13  | Old         | 80000  |
| 14  | Old         | 75000  |
| 15  | Old         | 35000  |
| 16  | Middle Age  | 29000  |
| 17  | Middle Age  | 57000  |
| 18  | Old         | 43000  |
| 19  | Middle Age  | 56000  |
| 20  | Old         | 63000  |
| 21  | Old         | 32000  |
| 22  | Old         | 45000  |
| 23  | Old         | 89000  |
| 24  | Middle Age  | 90000  |
| 25  | Middle Age  | 93000  |
| 26  | Young       | 80000  |
| 27  | Young       | 87000  |
| 28  | Young       | 38000  |
| 29  | Young       | 23000  |
| 30  | Middle Age  | 38900  |
| 31  | Middle Age  | 53200  |
| 32  | Old         | 43800  |
| 33  | Middle Age  | 25600  |
| 34  | Middle Age  | 65400  |
| 35  | Old         | 76800  |
| 36  | Old         | 89700  |
| 37  | Old         | 41800  |
| 38  | Young       | 31900  |
| 39  | Old         | 25600  |
| 40  | Middle Age  | 45700  |
| 41  | Old         | 35600  |
| 42  | Young       | 54300  |
| 43  | Middle Age  | 65400  |
| 44  | Old         | 67800  |
| 45  | Old         | 24500  |
| 46  | Middle Age  | 34900  |
| 47  | Old         | 45300  |
| 48  | Young       | 68400  |
| 49  | Middle Age  | 51700  |

```python
df.describe()
```

|       | Income      |
|-------|-------------|
| count | 50.000000   |
| mean  | 50966.000000 |
| std   | 21096.683268 |
| min   | 15000.000000 |
| 25%   | 33475.000000 |
| 50%   | 46850.000000 |
| 75%   | 65400.000000 |
| max   | 93000.000000 |


### Mean 

The mean, also known as the average, is a measure of central tendency in a dataset. It represents the typical value of a set of numbers. The formula to calculate the mean of a dataset is:

$$ \overline{x} = \frac{\sum\limits_{i=1}^{n} x_i}{n} $$

* $\overline{x}$ (pronounced "x bar") represents the mean value.
* $x_i$ represents the individual value in the dataset (where i goes from 1 to n).
* $\sum$ (sigma) represents the summation symbol, indicating we add up all the values from i=1 to n.
* $n$ represents the total number of values in the dataset.

```python
df['Income'].mean()
```

#### Result

```
50966.0
```

#### Without pandas


```python
def mean_f(df):
    for col in df.columns:
        if df[col].dtype != 'O':
            temp = 0
            for i in df[col]:
                temp = temp +i
            print("Without pandas Library -> ")
            print("Average of {} is {}".format(col,(temp/len(df[col]))))
            print()
            print("With pandas Library -> ")
            print(df[col].mean())

mean_f(df)
```

Average of Income:

- Without pandas Library -> 50966.0 
- With pandas Library -> 50966.0

### Median


The median is another measure of central tendency in a dataset. Unlike the mean, which is the average value of all data points, the median represents the middle value when the dataset is ordered from smallest to largest. If the dataset has an odd number of observations, the median is the middle value. If the dataset has an even number of observations, the median is the average of the two middle values.

The median represents the "middle" value in a dataset. There are two cases to consider depending on whether the number of observations (n) is odd or even:

**Odd number of observations (n):**

In this case, the median (M) is the value located at the middle position when the data is ordered from least to greatest. We can calculate the position using the following formula:

$$ M = x_{n+1/2} $$

**Even number of observations (n):**

When we have an even number of observations, there isn't a single "middle" value. Instead, the median is the average of the two middle values after ordering the data. Here's the formula to find the median:

$$ M = \frac{x_{n/2} + x_{(n/2)+1}}{2} $$

**Explanation:**

* M represents the median value.
* n represents the total number of observations in the dataset.
* $x$ represents the individual value.

```python
df['Income'].median()
```

#### Result

```
46850.0
```

#### Without pandas

```python
def median_f(df):
    for col in df.columns:
        if df[col].dtype != 'O':
            sorted_data = sorted(df[col])
            n = len(df[col])
            if n%2 == 0:
                x1 =sorted_data[int((n/2))]
                x2 =sorted_data[int((n/2))+1]
                median=(x1+x2)/2
            else:
                median = sorted_data[(n+1)/2]
    print("Median without library ->")
    print("Median of {} is {} ".format(col,median))
    print("Median with library ->")
    print(df[col].median())             
median_f(df)
```

Median of Income:

- Median without library -> 49850.0  
- Median with library -> 46850.0  

### Mode

The mode is a measure of central tendency that represents the value or values that occur most frequently in a dataset. Unlike the mean and median, which focus on the average or middle value, the mode identifies the most common value(s) in the dataset.

```python
def mode_f(df):
    for col in df.columns:
        if df[col].dtype == 'O':
            print("Column:", col)
            arr = df[col].sort_values()
            
            prevcnt = 0
            cnt = 0
            ans = arr[0]
            temp = arr[0]

            for i in arr:
                if(temp == i) :
                    cnt += 1
                else:
                    prevcnt = cnt
                    cnt = 1
                    temp = i
                if(cnt > prevcnt):
                    ans = i
            
            print("Without pandas Library -> ")
            print("Mode of {} is {}".format(col,ans))
            print()
            print("With pandas Library -> ")
            print(df[col].mode())
mode_f(df)
```

#### Result

```
Column: Age
Without pandas Library ->
Mode of Age is Old

With pandas Library ->
0    Old
Name: Age, dtype: object
```

### Standard Deviation

Standard deviation is a measure of the dispersion or spread of a dataset. It quantifies the amount of variation or dispersion of a set of values from the mean. In other words, it indicates how much individual values in a dataset deviate from the mean.

$$s = \sqrt{\frac{\sum(x_i-\overline{x})^{2}}{n-1}}$$

* $s$ represents the standard deviation.
* $\sum$ (sigma) represents the summation symbol, indicating we add up the values for all data points.
* $x_i$ represents the individual value in the dataset.
* $\overline{x}$ (x bar) represents the mean value of the dataset.
* $n$ represents the total number of values in the dataset.

```python
df['Income'].std()
```

#### Result

```
21096.683267707253
```

#### Without pandas

```python
import math
def std_f(df):
    for col in df.columns:
        if len(df[col]) == 0:
            print("Column is empty")
        if df[col].dtype != 'O':
            sum = 0
            mean = df[col].mean()
            for i in df[col]:
                sum = sum + (i - mean)**2
                
            std = math.sqrt(sum/len(df[col]))
            print("Without pandas library ->")
            print("Std : " , std)
            print("With pandas library: ->")
            print("Std : {}".format(np.std(df[col])))            ##ddof = 1
                
std_f(df)
```

Without pandas library ->
Std :  20884.6509187968 \
With pandas library: ->
Std : 20884.6509187968
    

### Count

```python
df['Income'].count()
```

#### Result

```
50
```

### Minimum


```python
df['Income'].min()
```

#### Result

```
15000
```

#### Without pandas

```python
def min_f(df):
    for col in df.columns:
        if df[col].dtype != "O":
            sorted_data = sorted(df[col])
            min = sorted_data[0]
            print("Without pandas Library->",min)
            print("With pandas Library->",df[col].min())
    
min_f(df) 
```

Without pandas Library-> 15000 \
With pandas Library-> 15000
    

### Maximum


```python
df['Income'].max()
```

#### Result

```
93000
```

#### Without pandas

```python
def max_f(df):
    for col in df.columns:
        if df[col].dtype != "O":
            sorted_data = sorted(df[col])
            max = sorted_data[len(df[col])-1]
            print("Without pandas Library->",max)
            print("With pandas Library->",df[col].max())
    
max_f(df) 
```

Without pandas Library-> 93000  
With pandas Library-> 93000
    

### Percentile


```python
df['Income'].quantile(0.25)
```

#### Result

```
33475.0
```

```python
df['Income'].quantile(0.75)
```

#### Result

```
65400.0
```

#### Without pandas

```python
def percentile_f(df,percentile):
    for col in df.columns:
        if df[col].dtype != 'O':
            sorted_data = sorted(df[col])
            index = int(percentile*len(df[col]))
            percentile_result = sorted_data[index]
            print(f"{percentile} Percentile is : ",percentile_result)

percentile_f(df,0.25)
```

0.25 Percentile is :  33000
    

We have used the method of nearest rank to calculate percentile manually.

Pandas uses linear interpolation of data to calculate percentiles.

## Correlation and Covariance


```python
df = pd.read_csv('Iris.csv')
df.head(5)
```

|   | Id | SepalLengthCm | SepalWidthCm | PetalLengthCm | PetalWidthCm | Species     |
|---|----|---------------|--------------|---------------|--------------|-------------|
| 0 | 1  | 5.1           | 3.5          | 1.4           | 0.2          | Iris-setosa |
| 1 | 2  | 4.9           | 3.0          | 1.4           | 0.2          | Iris-setosa |
| 2 | 3  | 4.7           | 3.2          | 1.3           | 0.2          | Iris-setosa |
| 3 | 4  | 4.6           | 3.1          | 1.5           | 0.2          | Iris-setosa |
| 4 | 5  | 5.0           | 3.6          | 1.4           | 0.2          | Iris-setosa |

```python
df.drop(['Id','Species'],axis=1,inplace= True)
```

### Covarience

Covariance measures the degree to which two variables change together. If the covariance between two variables is positive, it means that they tend to increase or decrease together. If the covariance is negative, it means that as one variable increases, the other tends to decrease. However, covariance does not provide a standardized measure, making it difficult to interpret the strength of the relationship between variables, especially if the variables are measured in different units.

$$ COV(X,Y) = \frac{\sum\limits_{i=1}^{n} (X_i - \overline{X}) (Y_i - \overline{Y})}{n - 1}$$

**Explanation:**

* $COV(X, Y)$ represents the covariance between variables X and Y.
* $X_i$ and $Y_i$ represent the individual values for variables X and Y in the i-th observation.
* $\overline{X}$ and $\overline{Y}$ represent the mean values for variables X and Y, respectively.
* $n$ represents the total number of observations in the dataset.

```python
df.cov()
```

|                   | SepalLengthCm  | SepalWidthCm  | PetalLengthCm   | PetalWidthCm |
|-------------------|--------------  |---------------|-----------------|--------------|
| **SepalLengthCm** | 0.685694       | -0.039268     | 1.273682        | 0.516904     |
| **SepalWidthCm**  | -0.039268      | 0.188004      | -0.321713       | -0.117981    |
| **PetalLengthCm** | 1.273682       | -0.321713     | 3.113179        | 1.296387     |
| **PetalWidthCm**  | 0.516904       | -0.117981     | 1.296387        | 0.582414     |

#### Without pandas

```python
def cov_f(df):
    for x in df.columns:
        for y in df.columns:
            mean_x = df[x].mean()
            mean_y = df[y].mean()

            sum = 0
            n = len(df[x])

            for val in range(n):
                sum += (df[x].iloc[val] - mean_x)*(df[y].iloc[val] - mean_y)
            print("Covariance of {} and {} is : {}".format(x,y, sum/(n-1)))
        print()
cov_f(df)
```

#### Result

```
Covariance of SepalLengthCm and SepalLengthCm is : 0.6856935123042504 
Covariance of SepalLengthCm and SepalWidthCm is : -0.03926845637583892 
Covariance of SepalLengthCm and PetalLengthCm is : 1.2736823266219246 
Covariance of SepalLengthCm and PetalWidthCm is : 0.5169038031319911 

Covariance of SepalWidthCm and SepalLengthCm is : -0.03926845637583892 
Covariance of SepalWidthCm and SepalWidthCm is : 0.1880040268456377 
Covariance of SepalWidthCm and PetalLengthCm is : -0.32171275167785235 
Covariance of SepalWidthCm and PetalWidthCm is : -0.11798120805369115 

Covariance of PetalLengthCm and SepalLengthCm is : 1.2736823266219246 
Covariance of PetalLengthCm and SepalWidthCm is : -0.32171275167785235 
Covariance of PetalLengthCm and PetalLengthCm is : 3.113179418344519 
Covariance of PetalLengthCm and PetalWidthCm is : 1.2963874720357946

Covariance of PetalWidthCm and SepalLengthCm is : 0.5169038031319911 
Covariance of PetalWidthCm and SepalWidthCm is : -0.11798120805369115 
Covariance of PetalWidthCm and PetalLengthCm is : 1.2963874720357946 
Covariance of PetalWidthCm and PetalWidthCm is : 0.5824143176733781
````

### Correlation

Correlation, on the other hand, standardizes the measure of relationship between two variables, making it easier to interpret. It measures both the strength and direction of the linear relationship between two variables. Correlation values range between -1 and 1, where:

$$r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{n(\sum x^2) - (\sum x)^2} \cdot \sqrt{n(\sum y^2) - (\sum y)^2}}$$

* r represents the correlation coefficient.
* n is the number of data points.

```python
df.corr()
```

|                   | SepalLengthCm | SepalWidthCm | PetalLengthCm | PetalWidthCm |
|-------------------|---------------|--------------|---------------|--------------|
| **SepalLengthCm** | 1.000000      | -0.109369    | 0.871754      | 0.817954     |
| **SepalWidthCm**  | -0.109369     | 1.000000     | -0.420516     | -0.356544    |
| **PetalLengthCm** | 0.871754      | -0.420516    | 1.000000      | 0.962757     |
| **PetalWidthCm**  | 0.817954      | -0.356544    | 0.962757      | 1.000000     |

#### Without using pandas

```python
import math
def corr_f(df):
    for i in df.columns:
        for j in df.columns:
            n = len(df[i])
            
            sumX  = 0
            for x in df[i]:
                sumX += x
            sumY = 0
            for y in df[j]:
                sumY += y

            sumXY = 0
            for xy in range(n):
                sumXY += (df[i].iloc[xy] * df[j].iloc[xy])
                
            sumX2  = 0
            for x in df[i]:
                sumX2 += (x**2)
            sumY2 = 0
            for y in df[j]:
                sumY2 += (y**2)

            NR = (n * sumXY) - (sumX*sumY)
            DR = math.sqrt( ( (n * sumX2) - (sumX**2))*( (n * sumY2) - (sumY ** 2) ) )

            print("Correlation of {} and {} :{}".format(i,j,NR/DR))
        print()

corr_f(df)
```

#### Result

```
Correlation of SepalLengthCm and SepalLengthCm :1.0
Correlation of SepalLengthCm and SepalWidthCm :-0.10936924995067286
Correlation of SepalLengthCm and PetalLengthCm :0.8717541573048861
Correlation of SepalLengthCm and PetalWidthCm :0.8179536333691775

Correlation of SepalWidthCm and SepalLengthCm :-0.10936924995067286
Correlation of SepalWidthCm and SepalWidthCm :1.0
Correlation of SepalWidthCm and PetalLengthCm :-0.42051609640118826
Correlation of SepalWidthCm and PetalWidthCm :-0.3565440896138223

Correlation of PetalLengthCm and SepalLengthCm :0.8717541573048861
Correlation of PetalLengthCm and SepalWidthCm :-0.42051609640118826
Correlation of PetalLengthCm and PetalLengthCm :1.0
Correlation of PetalLengthCm and PetalWidthCm :0.9627570970509656

Correlation of PetalWidthCm and SepalLengthCm :0.8179536333691775
Correlation of PetalWidthCm and SepalWidthCm :-0.3565440896138223
Correlation of PetalWidthCm and PetalLengthCm :0.9627570970509656
Correlation of PetalWidthCm and PetalWidthCm :1.0
```

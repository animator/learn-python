<span style="font-size: 20px; font-weight: bold;">Working with DataFrames</span>
</br>
</br>
<font size="16">Topics covered:</font>
</br>
<font size="14">
-What is a dataframe 
-Features of a dataframe
-Creation of DataFrames
-Manipulation of DataFrames
</font>
</br>
</br>

<font size="14">1.What is a dataframe</font>
-A dataframe is two-dimensional labeled datastructure used in data analysis and manipulation.
-It is fundamental datastructure provided by pandas library in python 

</br>
</br>

<font size="14">2.Key Features </font>
-Tabular datastructure-Data is represented in a table format with rows and columns
-Labeled Axes-Data is accessed using labels or indices.
-Heterogeneous Datatypes-Unlike arrays and matrices dataframe can hold data with different datatypes
-flexibility-Dataframe offers wide range of functions and methods to perform various opeartions
-Integration with other libraries:Dataframe integrate with other libraries using in data analysis such as Numpy,Matplotlib,Scikitlearn

</br>
</br>

<font size="14">3.Creation of Dataframes</font>

-Consider a dataset.A dataset contains records and attributes
-Import the dataset using pandas library
		import pandas as pd
		df = pd.read_csv('data.csv')  //absolute path of dataset
		print(data)
</br>
</br>


<font size="14">4.Manipulation of Dataframes with simple examples</font>

consider a dataset with attributes </br> 

Index  </br>name </br> age </br> gender</br>  state    </br>     Salary </br>  code </br>   Amount</br>

</br>

*Filtering rows
    filtered_df = df[df['age'] > 30]
<br>
*Selecting columns
    selected_columns_df = df[['name', 'age']]
<br>
*Grouping and aggregating data
    agg_df = df.groupby('gender')['age'].mean()
<br>
*Sorting data
    sorted_df = df.sort_values(by='age', ascending=False)
<br>
*loc and iloc
  loc-it is label based
    df.loc[0:5,"state"] //it gives first five states 
  iloc-it is integer based
    df.iloc[0:5,0:3]    //it prints first 5 rows and 3 columns 
<br>
*Indexing and retrieving data 
   -df['age'].mean()
   -df[df['age']==30].mean() //average of all columns that have age value=30
<br>
*Inserting rows
   df.insert(loc=len(df.columns).column="salary".value="Amount")
<br>
*Deleting columns
   df.drop(["Age","Amount"],axis=1) 
<br>
<br>
*Basic Functions used to manipulate Dataframes
</br>

-head()
   df.head()-reads first five lines of data
</br>
-shape()
   df.shape()-gives dimensionality of data
</br>
-info()
   df.info()-gives information about datatype of column and if there are any missing values,no.of observations in each columns
</br>
-describe()
   df.describe()-gives basic statistical characteristics of each numerical feature,no. of non missing values,mean,standard deviation,range,mean,median,0.25 and 0.75 quartiles 
</br>
-dropna()
   df.dropna()-it removes all the NaN values in the dataframe.
   df.dropna(axis=1)-it removes all the columns with any missing values.
</br>
-merge()
   merged_col=pd.merge(df,df1,on='Name')
</br>
-concat()
   combined_df = pd.concat([df1, df2], axis=0)
</br>
-rename()
   country_code = df.rename(columns={'Name': 'CountryName',
                                  'Code': 'CountryCode'},
                         inplace=False)
</br>
-sort_values()
	student.sort_values(by=['age'], ascending=True)
</br>
-apply()-is used to apply a function on dataframe 
    def double(a):
    	return 2*a  
    df['age']=df['age'].apply(double)
</br>
-append()
    appended_df = df1.append(df2)
</br>
-duplicated()
    df.duplicated()-returns boolean value denoting duplicate row
</br>
-corr()
    df.corr()-used to find pairwise correlatiom of all columns in the dataframe
</br>
-tail()
    df.tail()//returns last 5 records
</br>
-size()
    df.size() //returns no. of rows and columns 
</br>
-isnull()
     df.isnull() //checks if there are any null values
</br>
-nunique()
	df.nunique() //returns no. of unique entries
</br>
-nlargest()
	df.nlargest() //returns first n rows ordered by columns in descending order  
<br>
-eval()
    df.eval('D = B + C', inplace = True)  //to evaluate operation like sum,multiplication of two columns in dataframe 

</br>
</br>
*String manipulation functions
</br>
-lower()
    df.str.lower() //Converts all uppercase characters in strings in the DataFrame to lower case 
</br>
-strip()
    df.str.strip() //If there are spaces at the beginning or end of a string,it trims the strings to eliminate spaces
</br>
-split(‘ ‘)
	df.str.split(',')//Splits each string with the given pattern. Strings are split and the new elements after the performed split operation, are stored in a list.
</br>
-len()
    df.str.len() //compute length of each string in dataframe  
</br>
-get_dummies()
    df.str.get_dummies() // It returns the DataFrame with One-Hot Encoded values like we can see that it returns boolean value 1 if it exists in relative index or 0 if not exists.
</br>
-swapcase()
    df.str.swapcase()// It swaps the case lower to upper and vice-versa
</br>
-findall(//pattern)
    df.str.findall('n')//It returns a list of all occurrences of the pattern
</br>

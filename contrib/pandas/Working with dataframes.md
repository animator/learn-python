Working with DataFrames



Topics covered:

-What is a dataframe 
-Features of a dataframe
-Creation of DataFrames
-Manipulation of DataFrames



1.What is a dataframe
-A dataframe is two-dimensional labeled datastructure used in data analysis and manipulation.
-It is fundamental datastructure provided by pandas library in python 



2.Key Features 
-Tabular datastructure-Data is represented in a table format with rows and columns
-Labeled Axes-Data is accessed using labels or indices.
-Heterogeneous Datatypes-Unlike arrays and matrices dataframe can hold data with different datatypes
-flexibility-Dataframe offers wide range of functions and methods to perform various opeartions
-Integration with other libraries:Dataframe integrate with other libraries using in data analysis such as Numpy,Matplotlib,Scikitlearn



3.Creation of Dataframes

-Consider a dataset.A dataset contains records and attributes
-Import the dataset using pandas library
		import pandas as pd
		df = pd.read_csv('data.csv')  //absolute path of dataset
		print(data)



4.Manipulation of Dataframes with simple examples

consider a dataset 

Index  name  age  gender  state         Salary   code     Amount
1      Ram   30    M      telangana     20000    500070    400
2      Jack  25    M      maharastra    45000    635377    600
3      Riya  45    F      kerala        60000    536456    745
4      Mike  35    M      Bihar         50000    725523    800
5      Jill  56    F      Rajasthan     43500    656372    970   


*Filtering rows
    filtered_df = df[df['age'] > 30]


*Selecting columns
    selected_columns_df = df[['name', 'age']]


*Grouping and aggregating data
    agg_df = df.groupby('gender')['age'].mean()


*Sorting data
    sorted_df = df.sort_values(by='age', ascending=False)


*loc and iloc
  loc-it is label based
    df.loc[0:5,"state"] //it gives first five states 
  iloc-it is integer based
    df.iloc[0:5,0:3]    //it prints first 5 rows and 3 columns 


*Indexing and retrieving data 
   -df['age'].mean()
   -df[df['age']==30].mean() //average of all columns that have age value=30


*Inserting rows
   df.insert(loc=len(df.columns).column="salary".value="Amount")


*Deleting columns
   df.drop(["Age","Amount"],axis=1) 



*Basic Functions used to manipulate Dataframes

-head()
   df.head()-reads first five lines of data

-shape()
   df.shape()-gives dimensionality of data

-info()
   df.info()-gives information about datatype of column and if there are any missing values,no.of observations in each columns

-describe()
   df.describe()-gives basic statistical characteristics of each numerical feature,no. of non missing values,mean,standard deviation,range,mean,median,0.25 and 0.75 quartiles 

-dropna()
   df.dropna()-it removes all the NaN values in the dataframe.
   df.dropna(axis=1)-it removes all the columns with any missing values.

-merge()
   merged_col=pd.merge(df,df1,on='Name')

-concat()
   combined_df = pd.concat([df1, df2], axis=0)

-rename()
   country_code = df.rename(columns={'Name': 'CountryName',
                                  'Code': 'CountryCode'},
                         inplace=False)

-sort_values()
	student.sort_values(by=['age'], ascending=True)

-apply()-is used to apply a function on dataframe 
    def double(a):
    	return 2*a  
    df['age']=df['age'].apply(double)

-append()
    appended_df = df1.append(df2)

-duplicated()
    df.duplicated()-returns boolean value denoting duplicate row

-corr()
    df.corr()-used to find pairwise correlatiom of all columns in the dataframe

-tail()
    df.tail()//returns last 5 records

-size()
    df.size() //returns no. of rows and columns 

-isnull()
     df.isnull() //checks if there are any null values

-nunique()
	df.nunique() //returns no. of unique entries

-nlargest()
	df.nlargest() //returns first n rows ordered by columns in descending order  

-eval()
    df.eval('D = B + C', inplace = True)  //to evaluate operation like sum,multiplication of two columns in dataframe 


*String manipulation functions

-lower()
    df.str.lower() //Converts all uppercase characters in strings in the DataFrame to lower case 

-strip()
    df.str.strip() //If there are spaces at the beginning or end of a string,it trims the strings to eliminate spaces

-split(‘ ‘)
	df.str.split(',')//Splits each string with the given pattern. Strings are split and the new elements after the performed split operation, are stored in a list.

-len()
    df.str.len() //compute length of each string in dataframe  

-get_dummies()
    df.str.get_dummies() // It returns the DataFrame with One-Hot Encoded values like we can see that it returns boolean value 1 if it exists in relative index or 0 if not exists.

-swapcase()
    df.str.swapcase()// It swaps the case lower to upper and vice-versa

-findall(//pattern)
    df.str.findall('n')//It returns a list of all occurrences of the pattern

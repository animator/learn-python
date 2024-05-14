 - *Handling and Processing files:*
    - **JSON**
        - Fundamental library for data interchange.
        - It enables the encoding and decoding of data in JSON format
        - Useful in terms of web development and API interactions (JSON is the standard data format)
        1. Import JSON
            
            ```python
            import json
            ```
            
    
    **HANDLING XML DATA**
    
    - Untangle
        - Simple library which takes an XML document and returns a Python object which mirrors the nodes and attributes in its structure.
        1. Importing and loading untangle
        
        ```python
        import untangle
        obj = untangle.parse('path/to/file.xml')
        ```
        
    - xmltodict
        - simple library that aims at making XML feel like working with JSON.
        - It can be loaded into a Python dictionary and you can access elements, attributes and values.
        - It also lets you go back to XML from python dictionary.
        1. Importing and loading
        
        ```python
        import xmltodict
        with open('path/to/file.xml') as fd:
        	doc = xmltodict.parse(fd.read())
        ```
        
    - xmlschema
        - provides support for using XSD-Schemas in Python.
        - Automatic type parsing is available.
        - supports automatic and explicit validation of XML documents against a schema
        1. Import, loading and validating
        
        ```python
        from xmlschema import XMLSchema
        
        schema = XMLSchema("your_schema.xml")
        schema.validate("your_file.xml")
        ```
        
    
    **YAML**
    
    - Library for processing YAML files.
    
    **PyYAML**
    
    **TOML**
    
    **PyPDF2**
    
    **PDFMiner**
    
    **pdfplumber**
    
    **PyDub**
    

- *Data Manipulation:*
    - Pandas
        
        **Pandas** is a powerful data manipulation and analysis library that provides data structures like DataFrame, which is widely used for handling and analyzing structured data. Pandas excels at tasks such as cleaning, filtering, aggregating, and visualizing tabular data.
        
        1. To install pandas:
        
        ```bash
        pip install pandas
        ```
        
        1. To import pandas in your python script:
        
        ```python
        import pandas as pd
        ```
        
        1. Reading data into DataFrame
        
        ```python
        df = pd.read_csv('example.csv')
        ```
        
    - Intake
        
        **Intake**, on the other hand, is a data cataloging and loading library. It's designed to help you manage and load datasets from various sources in a consistent manner. Intake provides a high-level interface for accessing data, allowing you to define and organize data sources in a catalog and then load them as needed. Intake can work well with various data formats and sources, making it easier to maintain and share data loading configurations. Pandas is more focused on data manipulation and analysis, while Intake is focused on data loading and cataloging. Pandas and Intake can complement each other, Intake can manage and load the data into Pandas DataFrames for subsequent analysis.
        
        If dataset is stored in CSV file:
        
        1. **Install Intake:**
        
        ```bash
        pip install intake
        
        ```
        
        1. **Create an Intake Catalog:**
        Create an Intake catalog file, let's say `my_catalog.yaml`, to describe your dataset. This file might look like:
        
        ```yaml
        sources:
          my_dataset:
            description: My Example Dataset
            driver: csv
            args:
              urlpath: path/to/your/data.csv
        
        ```
        
        In this example, the dataset is a CSV file, but Intake supports various data formats and sources.
        
        1. **Load Data Using Intake:**
        Now, you can use Intake to load the data into a Pandas DataFrame. In your Python script or Jupyter Notebook:
        
        ```python
        import intake
        import pandas as pd
        
        # Load the catalog
        catalog = intake.open_catalog('my_catalog.yaml')
        
        # Load the dataset into a Pandas DataFrame
        df = catalog.my_dataset.read()
        
        # Now, df is a Pandas DataFrame, and you can perform your analysis using Pandas
        print(df.head())
        
        ```
        
        This code uses Intake to read the dataset described in the catalog and loads it into a Pandas DataFrame (`df`). Once you have the data in a Pandas DataFrame, you can use all the powerful Pandas functions for data manipulation and analysis.
        
        This approach has the advantage of separating the data loading configuration (described in the Intake catalog) from the data analysis code. It makes it easier to manage and share data loading configurations, especially when working with multiple datasets or collaborating with others.
        
    
    - **PyJanitor**:
        
        PyJanitor is a Python library that provides a set of convenient functions for cleaning and tidying up messy data. It builds on top of Pandas and extends its functionality, offering a variety of methods to simplify common data cleaning tasks. Pyjanitor is designed to make data cleaning and transformation code more readable, concise, and expressive.
        
        Key features and use cases of PyJanitor include:
        
        1. **Column Name Cleaning:**
        PyJanitor provides functions to clean and standardize column names, making them more consistent and easy to work with. For example, the `clean_names` function can be used to convert column names to lowercase, replace spaces with underscores, and remove special characters.
        2. **Data Type Conversion:**
        It includes functions for converting data types of columns. This is useful when you need to ensure that columns have the correct data types for analysis or visualization.
        3. **Handling Missing Data:**
        PyJanitor offers functions to handle missing data more efficiently. For example, the `coalesce` function can be used to fill missing values in a column with the first non-null value from a set of columns.
        4. **Concatenating DataFrames:**
        The library provides an easy way to concatenate DataFrames, making it more convenient to combine data from multiple sources.
        5. **Data Aggregation and Grouping:**
        PyJanitor simplifies the process of aggregating and grouping data using functions like `dataframe_groupby_agg`.
        6. **Function Chaining:**
        PyJanitor encourages method chaining, allowing you to perform multiple operations on a DataFrame in a single, concise statement. This can lead to more readable and compact code.
        
        Here's a simple example of using pyjanitor to clean column names and handle missing data:
        
        ```python
        import pandas as pd
        import janitor
        
        # Create a messy DataFrame
        data = {'First Name': ['John', 'Jane', 'Bob'],
                'Last Name ': ['Doe', 'Smith', 'Johnson'],
                'Age': [25, None, 30]}
        df = pd.DataFrame(data)
        
        # Clean column names and handle missing data
        cleaned_df = (
            df.clean_names()  # Clean column names
        			 .coalesce('age', 'first_name')  # Fill missing values in 'Age' with values from 'First Name'
        )
        
        print(cleaned_df)
        
        ```
        
       `clean_names` is used to standardize column names, and `coalesce` is used to fill missing values in the 'Age' column with values from the 'First Name' column. This makes the data more consistent and ready for analysis.

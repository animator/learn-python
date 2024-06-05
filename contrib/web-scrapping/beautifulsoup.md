# Beautiful Soup Library in Python

## Table of Contents
1. Introduction
2. Prerequisites
3. Setting Up Environment
4. Beautiful Soup Objects
5. Tag object
6. Children, Parents and Siblings
7. Filter: Findall method
8. Web Scraping the Contents of a Web Page

## 1. Introduction
Beautiful Soup is a Python library used for web scraping purposes to extract data from HTML and XML files. It creates a parse tree for parsed pages that can be used to extract data easily.

## 2. Prerequisites
- Understanding of HTTP Requests and Responses.
- Understanding of HTTP methods (GET method).
- Basic Knowledge on HTML.
-  Python installed on your machine (version 3.6 or higher).
- pip (Python package installer) installed.

## 3. Setting Up Environment
1.**Install latest version of Python:** Go to Python.org and Download the latest version of Python.

2.**Install a IDE:** Install any IDE of your choice to code. VS code is preferred.
>Note: You can use Google Colab without installing Python and IDE.

3.**Install Beautiful Soup:**
```python
!pip install bs4
```

## 4. Beautiful Soup Objects
Beautiful Soup is a Python library for pulling data out of HTML and XML files. This can be done by presenting the HTML as a set of objects.

Take the below HTML page as input
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3>Title</h3>
<p>This is the main context of the page</p>
</body>
</html>
```

lets store the HTML code in a variable
```
html=  "<!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h3><b> Title </b></h3>
        <p>This is the main context of the page</p>
        </body>
        </html>"
```

To parse the HTML document, pass the variable to the `BeautifulSoup` Constructor.
```
soup = BeautifulSoup(html,'html.parser')
```
Beautiful Soup transforms a complex HTML document into a complex tree of Python objects.

## 5. Tags

The Tag object corresponds to an HTML tag in the original document.

```
tag_obj = soup.title
print("tag object:", tag_obj)
print("tag object type:",type(tag_obj))
```
```
Result:
tag object: <title>Page Title</title>

tag object type: <class 'bs4.element.Tag'>
```

## 6. Children, Parent and Siblings

We can access the child of the tag or navigate down.

```
tag_obj = soup.h3
child = tag_obj.b
print(child)
parent = child.parent
print(parent)
sib = tag_obj.next_sibling
print(sib);
```
```
Result:
<b> Title </b>
<h3><b> Title </b></h3>
<p>This is the main context of the page</p>
```

> We need to mention the child to which we want to navigate. It is because there can be more than one child to a tag but only one parent and next sibling.

**Navigable String:** A string corresponds to a bit of text or content within a tag. Beautiful Soup uses the NavigableString class to contain this text.

```
tagstr = child.string
print(tagstr)
```
```
Result:
Title
```

## 7. Filter

Filters allow you to find complex patterns, the simplest filter is a string.

Consider the following HTML code:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Table</title>
</head>
<body>
    <h1>Sample Table</h1>
    <table class="myTable">
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>City</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>John Doe</td>
                <td>28</td>
                <td>New York</td>
            </tr>
            <tr>
                <td>Jane Smith</td>
                <td>34</td>
                <td>Los Angeles</td>
            </tr>
            <tr>
                <td>Emily Jones</td>
                <td>23</td>
                <td>Chicago</td>
            </tr>
        </tbody>
    </table>
</body>
</html>

```
Store the above code in a variable.
```
table = "<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Table</title>
</head>..............

table_bs = BeautifulSoup(table, 'html.parser')
"
```
**Find All:**  The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters. It places all the objects in a list. We can access by indexing.

## 8. Web Scraping the Contents of a Web Page

1. Get the URL of the webpage we need to scrape.

2. Get the HTML content by using `get` method in HTTP request.

3. Pass the HTML content to the BeautifulSoup Constructor to prepare an object.

4. Access the HTML elements using Tag name.

Below is the code to extract the img tags in a wikipedia page.

```
import requests
!pip install bs4
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Encyclopedia"
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

for link in soup.find_all('a'):
  print(link)
  print(link.get('src'))
```
We can retrieve any data in the webpage by access through the tags.

# JSON Module

## What is JSON?

- [JSON]("https://www.json.org/json-en.html") (JavaScript Object Notation)  is a format for structuring data.
- JSON is a lightweight, text-based data interchange format that is completely language-independent.
- Similar to XML, JSON is a format for structuring data commonly used by web applications to communicate with each other.

## Why JSON?

- Whenever we declare a variable and assign a value to it, the variable itself doesn't hold the value. Instead, the variable holds an address in memory where the value is stored. For example:

```python
age = 21
```

- When we use `age`, it gets replaced with `21`. However, *age doesn't contain 21, it contains the address of the memory location where 21 is stored*.

- While this works locally, transferring this data, such as through an API, poses a challenge. Sending your computer’s entire memory with the addresses is impractical and insecure. This is where JSON comes to the rescue.

### Example JSON

- JSON supports most widely used data types including String
  , Number, Boolean, Null, Array and Object.
- Here is an example of JSON file

```json
{
  "name": "John Doe",
  "age": 21,
  "isStudent": true,
  "address": null,
  "courses": ["Math", "Science", "History"],
  "grades": {
    "Math": 95,
    "Science": 89,
    "History": 76
  }
}
```

# Python JSON

Python too supports JSON with a built-in package called `json`. This package provides all the necessary tools for working with JSON Objects including `parsing, serializing, deserializing, and many more`.

## 1. Python parse JSON string.

- To parse JSON string Python firstly we import the JSON module.
- JSON string is converted to a Python object using `json.loads()` method of JSON module in Python.
- Example Code:

```python
# Python program to convert JSON to Python
import json

# JSON string
students ='{"id":"01", "name": "Yatharth", "department":"Computer Science Engineering"}'

# Convert string to Python dict
students_dict = json.loads(students)
print(students_dict)

print(students_dict['name'])

```

- Ouput:

```json
{"id": "01", "name": "Yatharth", "department": "Computer Science Engineering"}
```

## 2. Python load JSON file.

- JSON data can also be directly fetch from a json file
- Example:

```python
import json
# Opening JSON file
f = open('input.json',)

# Returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json file
for i in data['students']:
    print(i)

# Closing file
f.close()
```

- JSON file

```json
{
  "students":{
    {
      "id": "01", 
      "name": "Yatharth", 
      "department": "Computer Science Engineering"
    },
     {
      "id": "02", 
      "name": "Raj", 
      "department": "Mechanical Engineering"
    }
  }
}
```

- Ouput

```json
{"id": "01", "name": "Yatharth", "department": "Computer Science Engineering"}
{"id": "02", "name": "Raj", "department": "Mechanical Engineering"}
```
- `json.load()`: Reads JSON data from a file object and deserializes it into a Python object.
- `json.loads()`: Deserializes JSON data from a string into a Python object.


## Addtiotnal Context
Relation between python data types and json data types is given in table below.

| Python Object   | JSON Object |
|-----------------|-------------|
| Dict            | object      |
| list, tuple     | array       |
| str             | string      |
| int, long, float | numbers    |
| True            | true        |
| False           | false       |
| None            | null        |



## 3. Python Dictionary to JSON String
- Parsing python dictionary to json string using `json.dumps()`.
- Example Code:
```python
import json 
    
# Data to be written 
dictionary ={ 
  "id": "03", 
  "name": "Suraj", 
  "department": "Civil Engineering"
} 

# Serializing json  
json_object = json.dumps(dictionary, indent = 4) 
print(json_object)
```
- Output:
``` json
{
    "department": "Civil Engineering",
    "id": "02",
    "name": "Suraj"
}
```
## 4. Python Dictionary to JSON file.
- - Parsing python dictionary to json string using `json.dump()`.
- Example Code:
``` python
import json

# Data to be written
dictionary ={
	"name" : "Satyendra",
	"rollno" : 51,
	"cgpa" : 8.8,
	"phonenumber" : "123456789"
}

with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile)

```
- Ouput: `sample.json`
``` json
{
	"name" : "Satyendra",
	"rollno" : 51,
	"cgpa" : 8.8,
	"phonenumber" : "123456789"
}

```
## 5. Append Python Dictionary to JSON String.
- Append to an already existing string using `json.update()`.
- Example :
```python
import json
# JSON data:
x = { 
  "id": "03", 
  "name": "Suraj"
} 

# python object to be appended
y = { "department": "Civil Engineering"}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))

```
- Ouput:
```json
{"id": "03", "name": "Suraj", "department": "Civil Engineering"} 
```


## 6. Append Python Dictionary to JSON File.
- There is no direct function to append in file. So, we will load file in a dictionary, update dictionary then update content and convert back to json file format.
- `data.json`
``` json
{
  "students":{
    {
      "id": "01", 
      "name": "Yatharth", 
      "department": "Computer Science Engineering"
    },
     {
      "id": "02", 
      "name": "Raj", 
      "department": "Mechanical Engineering"
    } 
  }
}
```
- Example Code:
``` python
import json

# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside students
        file_data["students"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

# python object to be appended
y = { 
  "id": "03", 
  "name": "Suraj", 
  "department": "Civil Engineering"
} 
    
write_json(y) 

```
- Output:
```json
{
  "students":{
    {
      "id": "01", 
      "name": "Yatharth", 
      "department": "Computer Science Engineering"
    },
     {
      "id": "02", 
      "name": "Raj", 
      "department": "Mechanical Engineering"
    },
    { 
      "id": "03", 
      "name": "Suraj", 
      "department": "Civil Engineering"
    } 
  }
}
```

The Python json module simplifies the handling of JSON data, offering a bridge between Python data structures and JSON representations, vital for data exchange and storage in modern applications.
# Overview of Flask & Deploying an ML model using Flask

Developed by Armin Ronacher of Pocoo, Flask is an open-source micro web framework written in Python. It provides a lightweight and modular design that makes it highly adaptable for a variety of applications.

## Key Features of Flask

- Micro & Modular Framework
- Provides Routing Mechnanism to map URLs to Python functions
- Uses Jinja2 as its template engine, allowing to build dynamic web pages
- Provides a request object for each HTTP request, allowing to handle GET, POST requests,etc.
- Supports secure cookie-based session management
- Protects against common web attacks like Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF)

## Environment Setup & Installation

Let's begin with setting up the Flask environment and installing it. We need to make sure the current python3 version is higher than 2.7 for doing so.

#### Virtual environment installation
```python
pip install virtualenv
```

#### Create New Folder for virtual environment
```python
mkdir my_new_fold  
cd  my_new_fold  
virtualenv venv
```

#### Activate the environment
```python
venv\scripts\activate
```

#### Install the Flask
```python
 pip install flask  
```

## Basic Application using Flask & Routes

Create and save the following file as flask_basic.py.
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_basic_appli():
   return 'This is my basic flask application!’

if __name__ == '__main__':
   app.run(debug=True)
```

This application has a single route (/) that returns “This is my basic flask application!”.

## Request & Response Objects - Using GET & POST methods

Flask provides request and response objects to handle HTTP requests and responses. Here’s an example of handling GET and POST requests:

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        return "You've posted some data: " + str(request.json)
    else:
        return "Hello, GET request!"
```

## Dynamic Route Creation, Error Handling & HTTP Requests

We can create dynamic routes in Flask like this:

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username
```

For error handling, we can use error handlers:
```python
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
```

## Decorators & CRUD Operations

Flask uses decorators for route handling. We can also use Flask-SQLAlchemy for CRUD operations:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
```


## Creating ML Application & Deploying using Flask

We can use Flask to serve a machine learning model. Consider an example of a Sentiment analysis model that predicts whether a given text is positive or negative in the context of analyzing customer reviews.

- We’ll use Flask to serve the model, and we’ll use the **joblib** library to load the model because it’s more efficient for large datasets.
- We’ll assume that the model has been trained and saved to a file named **‘Amazon_Customer_Reviews_Analysis_model.joblib’**, and the vectorizer (used for converting text data into numerical data that can be used by the model) has been saved to a file named **‘vectorizer.joblib’**.

#### Installation of joblib library (if not yet installed)

```python
pip install  joblib
```

#### Quickstart with Code

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('Amazon_Customer_Reviews_Analysis_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

@app.route('/api', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json(force=True)

    # Convert data into numerical data
    data_vectorized = vectorizer.transform([data['text']])

    # Make prediction using model loaded from disk as per the data
    prediction = model.predict(data_vectorized)

    # Take the first value of prediction
    output = prediction[0]

    # Convert the prediction into a JSON response
    response = jsonify({'prediction': output})

    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

We can then run your Flask app with the following command:
```python
python app.py
```
Our Flask app will be accessible at http://localhost:5000/api.



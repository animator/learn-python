# Python Requests Module Project

## Description

This project demonstrates how to use the Python `requests` module to make HTTP requests. It includes examples of GET, POST, PUT, DELETE, HEAD, and PATCH requests, as well as handling responses and extracting useful information.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Making a GET Request](#making-a-get-request)
  - [Other HTTP Methods](#other-http-methods)
  - [Response Object](#response-object)
  


## Introduction

The `requests` library in Python is a simple and elegant HTTP library. It allows you to send HTTP/1.1 requests with methods like GET and POST, add headers, form data, multipart files, and parameters with simple Python dictionaries, and access the response data in the same way.

## Installation

To install the `requests` module, use the following command:

pip install requests


## Usage

Making a GET Request

Here's how to make a simple GET request using the requests module:

import requests

## Making a GET request
response = requests.get('https://api.github.com/')


print(f'Status Code: {response.status_code}')


print(f'Content: {response.content}')


## Other HTTP Methods
The requests module supports several other HTTP methods:

response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.text)

response = requests.put('https://httpbin.org/put', data={'key': 'value'})
print(response.text)


## Response Object
The response object contains useful information about the response. Here are some of the most commonly used attributes and methods:

response = requests.get('https://api.github.com/')

# Print response URL
print(f'URL: {response.url}')

# Print status code
print(f'Status Code: {response.status_code}')

# Print response headers
print(f'Headers: {response.headers}')

# Print response content (in bytes)
print(f'Content: {response.content}')

# Print response encoding
print(f'Encoding: {response.encoding}')

# Print response text (decoded content)
print(f'Text: {response.text}')

# Print cookies
print(f'Cookies: {response.cookies}')

# Print elapsed time
print(f'Time Elapsed: {response.elapsed}')

# Close the connection
response.close()

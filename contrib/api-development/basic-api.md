# Book Management API

## Overview

The Book Management API allows users to perform CRUD operations on a collection of books. It provides endpoints for creating, reading, updating, and deleting books.

## Base URL

The base URL for accessing the Book Management API is `https://api.bookmanager.com/v1/`.

## Authentication

Authentication is not required for accessing public endpoints such as retrieving books. However, for creating, updating, or deleting books, users must authenticate using an API key or token.

## Endpoints

### Get All Books

- **Endpoint:** `GET /books`
- **Description:** Retrieves a list of all books.
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Harry Potter and the Philosopher's Stone",
      "author": "J.K. Rowling",
      "genre": "Fantasy",
      "published_year": 1997
    },
    {
      "id": 2,
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "genre": "Fiction",
      "published_year": 1960
    }
  ]
  ```


### Get Book by ID

- **Endpoint:** `GET /books/{id}`
- **Description:** Retrieves details of a specific book by its ID.
- **Parameters:**
  - `{id}`: The ID of the book.
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "genre": "Fantasy",
    "published_year": 1997
  }
  ```

### Create Book

- **Endpoint:** `POST /books`
- **Description:** Creates a new book.
- **Request Body:**
  ```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic",
    "published_year": 1925
  }
  ```
- **Response:**
  ```json
  {
    "id": 3,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic",
    "published_year": 1925
  }
  ```

### Update Book

- **Endpoint:** `PUT /books/{id}`
- **Description:** Updates an existing book.
- **Request Body:**
  ```json
  {
    "title": "The Great Gatsby (Updated)",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic Fiction",
    "published_year": 1925
  }
  ```
- **Response:**
  ```json
  {
    "id": 3,
    "title": "The Great Gatsby (Updated)",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic Fiction",
    "published_year": 1925
  }
  ```

### Delete Book

- **Endpoint:** `DELETE /books/{id}`
- **Description:** Deletes a book by its ID.
- **Parameters:**
  - `{id}`: The ID of the book.

## Definitions

- **CRUD:** Stands for Create, Read, Update, and Delete, representing basic operations in persistent storage.
- **Authentication:** Process of verifying the identity of a user or system.
- **API Key:** A unique identifier used for authentication and authorization in APIs.
- **Token:** A security credential used for authenticating API requests.

Feel free to use this markdown file as a reference for implementing the Book Management API.

```

This markdown file covers the API overview, base URL, authentication details, endpoints for CRUD operations on books, definitions of key terms, and usage instructions.
```
## here's how we can implement the Book Management API using Python and Flask:

First, you'll need to install Flask, a lightweight web framework for Python:

```bash
pip install Flask
```

Now, create a Python file named `app.py` and add the following code:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample book data
books = [
    {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "genre": "Fantasy", "published_year": 1997},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "published_year": 1960}
] #list of dicts

# This route is used to Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books) #returns a json file of books

# This route is used to Get book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# This route is used to Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author'],
        'genre': data['genre'],
        'published_year': data['published_year']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# This route is used to Update book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# This route is used to Delete book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

To run the API, execute the `app.py` file:

```bash
python app.py
```

Now your Book Management API is running on `http://127.0.0.1:5000/`. You can use tools like Postman or cURL to test the API endpoints:

- GET all books: `GET http://127.0.0.1:5000/books`
- GET book by ID: `GET http://127.0.0.1:5000/books/1`
- POST new book: `POST http://127.0.0.1:5000/books` with JSON body
- PUT update book by ID: `PUT http://127.0.0.1:5000/books/1` with JSON body
- DELETE book by ID: `DELETE http://127.0.0.1:5000/books/1`

Feel free to modify and extend the code to suit your needs, such as adding error handling, database integration, or authentication mechanisms.

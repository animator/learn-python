# API Methods

| Method  | Summary                                                  | CRUD   | Accepts Request Body | Idempotent | Safe |
|---------|----------------------------------------------------------|--------|-----------------------|------------|------|
| GET     | To fetch a single resource or group of resources         | Read   | No                    | Yes        | Yes  |
| PUT     | To update an entire resource in one go                   | Update | Yes                   | Yes        | No   |
| POST    | To create a new resource                                 | Create | Yes                   | No         | No   |
| PATCH   | To partially update a resource                           | Update | Yes                   | No         | No   |
| DELETE  | To delete a resource                                    | Delete | No                    | Yes        | No   |
| OPTIONS | To get information on permitted operations               | Read   | No                    | Yes        | Yes  |
| HEAD    | To get metadata of the endpoint                         | Read   | No                    | Yes        | Yes  |
| TRACE   | For diagnosing purposes                                  | Read   | No                    | Yes        | Yes  |
| CONNECT | To make the two-way connection between the client and the resource | - | No | No         | No   |

## Method Details:

- **GET**: 
    - The GET method is used to retrieve data from a specified resource. 

- **POST**: 
    - The POST method is used to submit data to be processed to a specified resource. 

- **PUT**: 
    -   The PUT method is used to update a specified resource with new data. 

- **PATCH**:
    - The PATCH method is used to apply partial modifications to a resource. 

- **DELETE**: 
    - The DELETE method is used to delete a specified resource. 

- **OPTIONS**:
    - The OPTIONS method is used to describe the communication options for the target resource. 

- **HEAD**:
    - The HEAD method is similar to the GET method, but it only retrieves the headers of the response without the body. 

- **TRACE**:
    - The TRACE method is used to test the connectivity between the client and the server. 

- **CONNECT**:
    - The CONNECT method is used to establish a tunnel to the server using a proxy. 


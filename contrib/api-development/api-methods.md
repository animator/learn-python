# API Methods

| Method  | Summary                                                  | CRUD   | Accepts Request Body | Idempotent | Safe | Response Body |
|---------|----------------------------------------------------------|--------|-----------------------|------------|------|---------------|
| GET     | To fetch a single resource or group of resources         | Read   | No                    | Yes        | Yes  | Yes           |
| PUT     | To update an entire resource in one go                   | Update | Yes                   | Yes        | No   | Yes           |
| POST    | To create a new resource                                 | Create | Yes                   | No         | No   | Yes           |
| PATCH   | To partially update a resource                           | Update | Yes                   | No         | No   | Yes           |
| DELETE  | To delete a resource                                    | Delete | No                    | Yes        | No   | No            |
| OPTIONS | To get information on permitted operations               | Read   | No                    | Yes        | Yes  | Yes           |
| HEAD    | To get metadata of the endpoint                         | Read   | No                    | Yes        | Yes  | No            |
| TRACE   | For diagnosing purposes                                  | Read   | No                    | Yes        | Yes  | No            |
| CONNECT | To make the two-way connection between the client and the resource | - | No | No         | No   | No            |

## Method Details:

- **GET**: 
    - The GET method is used to retrieve data from a specified resource. It does not typically alter the state of the resource and is safe and idempotent. It can accept query parameters in the URL to filter or sort the results. A response body is returned with the requested data.

- **POST**: 
    - The POST method is used to submit data to be processed to a specified resource. It is commonly used for creating new resources, and it may or may not require a request body containing the data to be created. It is not idempotent nor safe. A response body is returned with the newly created resource's details.

- **PUT**: 
    -   The PUT method is used to update a specified resource with new data. It typically requires a request body containing the complete representation of the resource to be updated. It is idempotent and not safe. A response body is returned with the updated resource's details.

- **PATCH**:
    - The PATCH method is used to apply partial modifications to a resource. It typically requires a request body containing the specific changes to be made. It is not idempotent nor safe. A response body is returned with the updated resource's details.

- **DELETE**: 
    - The DELETE method is used to delete a specified resource. It does not typically require a request body, as the resource to be deleted is identified in the request URI. It is idempotent but not safe. No response body is returned.

- **OPTIONS**:
    - The OPTIONS method is used to describe the communication options for the target resource. It does not typically require a request body and is safe and idempotent. A response body is returned with information about the supported HTTP methods and other metadata.

- **HEAD**:
    - The HEAD method is similar to the GET method, but it only retrieves the headers of the response without the body. It does not typically require a request body and is safe and idempotent.

- **TRACE**:
    - The TRACE method is used to test the connectivity between the client and the server. It does not typically require a request body and is safe and idempotent.

- **CONNECT**:
    - The CONNECT method is used to establish a tunnel to the server using a proxy. It does not typically require a request body and is neither safe nor idempotent.

### Definitions:

- **CRUD**:
    - CRUD stands for Create, Read, Update, and Delete, representing the four basic functions of persistent storage. These operations are commonly used in database and RESTful API designs.

- **Accepts Request Body**:
    - Indicates whether the HTTP method typically accepts a request body containing data to be processed or modified. If yes, the method may require the client to include data in the request body.

- **Idempotent**:
    - An idempotent operation means that making the same request multiple times will produce the same result as making it once. In the context of HTTP methods, an idempotent method does not change the server state after multiple identical requests.

- **Safe**:
    - A safe operation does not modify the state of the server or its resources. It only retrieves data without causing any side effects. Safe methods are typically used for read-only operations.
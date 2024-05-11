## API Methods

- **GET**: 
    - The GET method is used to retrieve data from a specified resource. 
    - It is a safe and idempotent method, meaning that it should not have any side effects and can be called multiple times without changing the result. 
    - Use the GET method when you want to retrieve information from the server.

- **POST**: 
    - The POST method is used to submit data to be processed to a specified resource. 
    - It is not idempotent, meaning that calling the same POST request multiple times may result in different outcomes. 
    - Use the POST method when you want to create a new resource on the server.

- **PUT**: 
    -   The PUT method is used to update a specified resource with new data. 
    - It is idempotent, meaning that calling the same PUT request multiple times should have the same effect as calling it once. 
    - Use the PUT method when you want to update an existing resource on the server.

- **PATCH**:
    - The PATCH method is used to apply partial modifications to a resource. 
    - It is not idempotent, meaning that calling the same PATCH request multiple times may result in different outcomes. 
    - Use the PATCH method when you want to update a resource with partial data.

- **DELETE**: 
    - The DELETE method is used to delete a specified resource. 
    - It is idempotent, meaning that calling the same DELETE request multiple times should have the same effect as calling it once. 
    - Use the DELETE method when you want to remove a resource from the server.

- **OPTIONS**:
    - The OPTIONS method is used to describe the communication options for the target resource. 
    - It is idempotent, meaning that calling the same OPTIONS request multiple times should have the same effect as calling it once. 
    - Use the OPTIONS method when you want to retrieve the communication options for a resource.

- **HEAD**:
    - The HEAD method is similar to the GET method, but it only retrieves the headers of the response without the body. 
    - It is idempotent, meaning that calling the same HEAD request multiple times should have the same effect as calling it once. 
    - Use the HEAD method when you want to check the headers of a resource without retrieving the body.

- **TRACE**:
    - The TRACE method is used to test the connectivity between the client and the server. 
    - It is idempotent, meaning that calling the same TRACE request multiple times should have the same effect as calling it once. 
    - Use the TRACE method when you want to test the connectivity between the client and the server.

- **CONNECT**:
    - The CONNECT method is used to establish a tunnel to the server using a proxy. 
    - It is not idempotent, meaning that calling the same CONNECT request multiple times may result in different outcomes. 
    - Use the CONNECT method when you want to establish a tunnel to the server using a proxy.


                                 #Request Module in Python
      >>Introduction
       The Requests library in Python is one of the integral parts of Python for making HTTP requests to a specified URL. Whether it be REST APIs 
    or Web Scraping, requests are a must to be learned for proceeding further with these technologies. When one makes a request to a URI, it 
    returns a response. Python requests provide inbuilt functionalities for managing both the request and response

      >> What is Python Requests module?
       Requests is an Apache2 Licensed HTTP library, that allows to send HTTP/1.1 requests using Python.
   To play with web, Python Requests is must. Whether it be hitting APIs, downloading entire facebook pages, and much more cool stuff, one will 
    have to make a request to the URL.

   * Installing Requests
   Requests installation depends on type of operating system on eis using, the basic command anywhere would be to open a command terminal and run,

     pip install requests

   * Making a Request
       Python requests module has several built-in methods to make Http requests to specified URI using GET, POST, PUT, PATCH or HEAD requests. A 
     Http request is meant to either retrieve data from a specified URI or to push data to a server. It works as a request-response protocol 
     between a client and a server. Let’s demonstrate how to make a GET request to an endpoint. GET method is used to retrieve information from the 
     given server using a given URI. The GET method sends the encoded user information appended to the page request. The page and the encoded 
     information are separated by the ‘?’ character. For example: https://www.google.com/search?q=...
                
    >>How to make GET request through Python Requests
      Python’s requests module provides in-built method called get() for making a GET request to a specified URI.

    * Syntax
    requests.get(url, params={key: value}, args)

     Example :
     Let’s try making a request to github’s APIs for example purposes.
  import requests 

  # Making a GET request 
   r = requests.get('https://api.github.com/...') 

  # check status code for response received 
  # success code - 200 
  print(r) 

# print content of request 
  print(r.content) 
  save this file as request.py and through terminal run,
        python request.py


      >> Http Request Methods
      Method	  Description
     1. GET	      GET method is used to retrieve information from the given server using a given URI.
     2.POST	     POST request method requests that a web server accepts the data enclosed in the body of the request message, most likely for 
                  storing 
     3. PUT	      The PUT method requests that the enclosed entity be stored under the supplied URI. If the URI refers to an already existing 
                  resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that 
                   URI.
    4.DELETE	  The DELETE method deletes the specified resource
    5.HEAD	      The HEAD method asks for a response identical to that of a GET request, but without the response body.
    6.PATCH	      It is used for modify capabilities. The PATCH request only needs to contain the changes to the resource, not the complete 
                  resource


    >> Response object
       When one makes a request to a URI, it returns a response. This Response object in terms of python is returned by requests.method(), method 
      being – get, post, put, etc. Response is a powerful object with lots of functions and attributes that assist in normalizing data or creating 
      ideal portions of code. For example, response.status_code returns the status code from the headers itself, and one can check if the request 
       was processed successfully or not. Response object can be used to imply lots of features, methods, and functionalities.
 
  # import requests module 
   import requests 
   # Making a get request 
   response = requests.get('https://api.github.com/') 
   # print request object 
   print(response.url) 
  # print status code 
   print(response.status_code)

    >> Response Methods
    Method              `  `	Description
   1.response.headers	response.headers returns a dictionary of response headers.
   2.response.encoding	response.encoding returns the encoding used to decode response.content.
   3.response.elapsed	response.elapsed returns a timedelta object with the time elapsed from sending the request to the arrival of the response.
   4.response.close()	response.close() closes the connection to the server.
   5.response.content	response.content returns the content of the response, in bytes.
   6.response.cookies	response.cookies returns a CookieJar object with the cookies sent back from the server.
   7.response.history	response.history returns a list of response objects holding the history of request (url).
   8.response.is_permanent_redirect	 returns True if the response is the permanent redirected url, otherwise False.

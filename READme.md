FASTAPI

# Option 1: Use a Virtual Environment (Recommended)

Create and activate it in your project folder:

python3 -m venv venv

source venv/bin/activate

# Then install FastAPI and Uvicorn:

pip install fastapi uvicorn

# Run your app:

uvicorn +(filename):app --reload
uvicorn books:app --reload

# RUN UVICORN ON A DIFFERENT PORT

You can simply start it on a new port, for example 8001:

- uvicorn books2:app --reload --port 8004

## For folders, don't use:
- uvicorn IntroFastApi/books2:app --reload

## Include dot notation (.) to import-Use the following:

- uvicorn IntroFastApi/books2:app --reload

# TO USE THE BROWSER, ADD the api endpoint
 http://127.0.0.1:8000/books


# TO USE SWAGGER, ADDD DOCS
http://127.0.0.1:8000/docs 

# Why adding __init__.py to every fastApiPython folder?
- Marks the directly as python package
- Wether empty or not it is always useful
- Makes the app portable, stable and professional 
- Prevent import and reload errors

# MEANING OF FAST API

Web-framework for building modern API

Fast(Performance)
Fast(Development)

** PATH PARAMETERS, DYNAMIC PARAMETERS, AND PATH PARAMETERS

# Static Parameters

Static parameters are fixed parts of the URL — they don’t change.

## For example:

@app.get("/books")
def get_books():
    return {"message": "List of all books"}


/books is static — it will always match that exact path.

Visiting /books returns the same thing every time.

## Example usage:

Listing all items

Fixed endpoints like /status, /login, /about

# Dynamic Parameters

Dynamic parameters are variable parts of the path — they change depending on the request.

## For example:

@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {"book_id": book_id}


Here:

{book_id} is a path parameter — it’s dynamic.

/books/1 → book_id = 1

/books/99 → book_id = 99

## Example usage:

Getting a specific item (/users/{id})

Updating or deleting something by ID

# Query Parameters

These are dynamic too — but they appear after the ? in the URL, not in the path.

# What is a query parameter?

Sort and filter through data that is not marked by path parameter

# Example:

@app.get("/books")
def search_books(title: str | None = None):
    return {"title": title}


/books?title=Harry → query parameter title = "Harry"



NOTE: FASTAPI execute endpoints from top to the bottom


** POST REQUEST **

- Used to create data
- POST has additional information that GET doesn't have

# TO USE POST, WE NEED TO IMPORT "BODY" from FASTAPI

# TO USE PUT, WE NEED TO IMPORT "BODY" from FASTAPI


# PART 2 OF THE PROJECT

Data validation
Exception Handling
Status codes, 
Swagger configuration
Python Request Objects

PYDANTICS

- Python library that is used for data modeling,data parsing, and has efficient error handling
- Pydantics is commonly used as a resource for data validation and how to handle data in fastAPI applications.

# DATA VALIDATION IN PYTHON

Using "Path()"

- Path(gt=0); id entered and is less than zero, the error will be thrown

Using "Query()"
- Query(gt=0, lt=6)   --------id entered and is less than zero, the error will be thrown.

However, this is only used for Filter, search, sort, paginate


# Status Codes

HTTP Status Code: Used to help client(user or system submitting data to the server) to understand what happened on the server side of the application

It allows everyone who sends the request to know if their submission was successful or not

1xx --> Information Response: Request Processing
2xx --> Success: Request Successfully Complete
3xx --> Redirection: Further Action must be Complete
4xx --> Client Errors: An error was caused by the client
5xx --> Server Errors: An error occured on the server


2xx --> Success: Request Successfully Complete:

200:OK --> Standard Response for a Successful Request. Commonly used for sucessfull Get Request when data is being returned
201: Created --> The request has been successfull, creating a new resource. Used when request create an entity
204: No Content --> The request has been successfull, did not create an entity nor return anything. Commonly used with put request

4xxx --> Client Errors Status Codes

400: Bad Request--> Can not process the request due to client error. Commonly used for invalid requests methods
401: Unauthorized --> Client does not have valid authentication for target resource
404: Not found --> The client requested resource can not be found
422: Unprocessable Entity --> Semantic Errors in Client Request

5xxx --> Server Status Codes:

500: Internal Server Error --> Generic Error Message, when unexpected issue on the server happened


NEXT CHAPTER

Authorization and Authentication

Web Page   -->                   FastAPI     <--                        Database
           <--                   (Server)    -->   

Define Database?

- Organized Collection of Structured Information of Data, which is stored in computer system
The data can be 
- Data can be easily accessed
- Data can be easily modified
- The data can be controlled and organized
- Many databases uses Structured Query Language(SQL) to modify and write data

Define Data?

- Data can be related to any object
- For example, user on an application may have:
   Name, Age and Email
- All of these is data

Thus, Database allow the management of this data, since data is just data on its own

Data are organized in how Data can be retrieved, stored and modified

There are many types of Database Management Systems(DBMS): 
- SQLITE
- MYSQL
- PostGRESQL

Define SQL?

- Standard language for dealing with relational databases
- With Database records, SQL can be used different things
      Those include READ, CREATE, UPDATE, AND DELETE(CRUD OPERATIONS) 


## INSTALLATION OF SQL ALCHEMY
* Benefit:
       - To connect FastAPI to databases(MySQL, SQLite, PostgreSQL)
       - To write databases queries in Python instead of raw SQL querries
       - Map Python classes-> database tables(ORM)
       - Manage relationships, joins, and transactions



## CREATING MODELS

- Helps SQLALCHEMY to understand what kind of database tables to create in the future

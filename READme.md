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

uvicorn books2:app --reload --port 8004

# TO USE THE BROWSER, ADD the api endpoint
 http://127.0.0.1:8000/books


# TO USE SWAGGER, ADDD DOCS
http://127.0.0.1:8000/docs 


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

- Path(gt=0); id intered and is less than zero, the error will be thrown

Using "Query()"
- Query(gt=0, lt=6)   --------id intered and is less than zero, the error will be thrown.

However, this is only used for Filter, search, sort, paginate



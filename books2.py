from fastapi import FastAPI, Body, Path, Query,HTTPException
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()


class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int
    published_date:int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author 
        self.description = description
        self.rating = rating
        self.published_date = published_date

# Adding a this class for data validation purpose
# class BookRequest(BaseModel):
#     id:int 
#     title:str = Field(min_length=3)
#     author:str = Field(min_length=1)
#     description:str = Field(min_length=1,max_length=100)
#     rating: int = Field(gt=-1, lt=6) #rating from 1 to 5(exclude -1 and 6)

# CHanging id data validation, you won't need to add id. It will be assigned authomatically, and chronologically
class BookRequest(BaseModel):
    id:Optional[int] = None
    title:str = Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1,max_length=100)
    rating: int = Field(gt=-1, lt=6) #rating from 1 to 5(exclude -1 and 6)
    published_date:int = Field(gt=-1, lt=2026)

    model_config = {
        "json_schema_extra":{
            "example": {
                "title":"A new book",
                "author": "Coding with Niyongira",
                "description": "A new description of a book",
                "rating": 5,
                "published_date":2000
            }
        }
    }


BOOKS = [
    Book(1, 'Computer Science Pro', 'Coding with Niyongira', 'A very awesome book to read', 5, 2000),
    Book(2, 'Be Fast with FastAPI', 'Coding with Niyongira', 'A great book', 5,2002),
    Book(3, 'Master endpoints', 'Coding with Niyongira', 'Rewarding book', 3,2002),
    Book(4, 'HP1', 'Author 1', 'Book Description', 1, 2000),
    Book(5, 'HP1', 'Author 1', 'Book Description', 3, 1995),
    Book(6, 'HP1', 'Author 1', 'Book Description', 2, 1900)

]

@app.get("/books")
async def read_all_books():
    return BOOKS

# CREATE A BOOK
# @app.post("/books")
# async def create_book(new_book=Body()):
#     BOOKS.append(new_book)
    # return BOOKS

# When creating  a new book, using "Body" doesn't allow data validation. Thus we prefer to use pydantic class

# @app.post("/books")
# async def create_book(new_book:BookRequest):
#     BOOKS.append(new_book)
#     return BOOKS


# Advanced-finding the id of the book. This will override and arrange the id of the books in chronological order(ascending)
def find_book_id(book:Book):
    if len(BOOKS)> 0:
        book.id = BOOKS[-1].id+1
    else:
        book.id = 1
    return book


@app.post("/books")
async def create_book(new_book:BookRequest):
    BOOKS.append(find_book_id(new_book))
    return BOOKS

@app.get("/books/{book_id}")
async def find_book(book_id: int=Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail = 'item not found')
        
# Get a book by rating
@app.get("/books/rating/{book_rating}")    # /rating was added to make the route look differnt from get a book by id 
async def get_book_by_rating(book_rating:int):
    list_books = []
    for book in BOOKS:
        if book.rating == book_rating:
            list_books.append(book)
    return list_books

#Second Method-Using Query Parameter-Including Data Validation
@app.get("/books/")    # /rating was added to make the route look differnt from get a book by id 
async def get_book_by_rating(book_rating:int=Query(gt=0,lt=6)):
    list_books = []
    for book in BOOKS:
        if book.rating == book_rating:
            list_books.append(book)
    return list_books


# DELETE A BOOK

# @app.delete("/books/{book_id}")
# async def delete_book(book_id: int):
#     for book in BOOKS:
#         if book.id == book_id:
#             BOOKS.remove(book)
#         return BOOKS


#2nd method of deleting a book 
#Path data validation added
@app.delete("/books/{book_id}")
async def delete_book(book_id: int=Path(..., gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return BOOKS
    raise HTTPException(status_code = 404, detail = "item not found")


# UPDATE A BOOK-1ST METHOD

@app.put("/books/update_book")
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id: 
            BOOKS[i] = book
            return BOOKS
    raise HTTPException(status_code=404, detail="item not found")

# Get books by published date
@app.get("/books/pub_date/{pub_date}")
async def get_book_by_pub_date(pub_date:int=Path(gt=1000,lt=2000)):   #Any id less than 0, the error will occur
    return_books = []
    for book in BOOKS:
        if book.published_date == pub_date:
            return_books.append(book)
    return return_books

#Second Method-Get book by Published date-Including Data Validation
@app.get("/books/publish/")
async def get_book_publish_date(pub_date:int=Query(gt=1800,lt=2031)):
    return_books = []
    for book in BOOKS:
        if book.published_date == pub_date:
            return_books.append(book)
    return return_books
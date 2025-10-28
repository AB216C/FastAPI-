from fastapi import FastAPI, Body
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()


class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author 
        self.description = description
        self.rating = rating

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


BOOKS = [
    Book(1, 'Computer Science Pro', 'Coding with Niyongira', 'A very awesome book to read', 5),
    Book(2, 'Be Fast with FastAPI', 'Coding with Niyongira', 'A great book', 4.9),
    Book(3, 'Master endpoints', 'Coding with Niyongira', 'Rewarding book', 4.7),
    Book(4, 'HP1', 'Author 1', 'Book Description', 1),
    Book(5, 'HP1', 'Author 1', 'Book Description', 3),
    Book(6, 'HP1', 'Author 1', 'Book Description', 2),

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
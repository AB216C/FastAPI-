from fastapi import FastAPI, Body

app = FastAPI()


class Book:
    id:int
    title:str
    author:str
    description:str
    rating:str

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author 
        self.description = description
        self.rating = rating

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

@app.post("/books")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS


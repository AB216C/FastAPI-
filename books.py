from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title one', 'author': 'Author one', 'category': 'Science'},
    {'title': 'Title twO', 'author': 'Author two', 'category': 'Science'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'History'},
    {'title': 'Title four', 'author': 'Author four', 'category': 'Math'},
    {'title': 'Title five', 'author': 'Author five', 'category': 'Math'},
    {'title': 'Title six', 'author': 'Author six', 'category': 'Math'},
]

# Example of a static parameter

@app.get("/books")

async def Read_All_Books():
    return BOOKS


# Example of a dynamic parameter

@app.get("/books/category")
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold()== category.casefold():
            books_to_return.append(book)
    return books_to_return


# @app.get("/books/category")
# async def read_category_by_query(category:str):
#     return [book for book in BOOKS if book["category"].casefold()==category.casefold()]


#Dynamic and query parameter

@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# Filter books by author and category
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str, category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
            
# POST REQUEST

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    return BOOKS
    
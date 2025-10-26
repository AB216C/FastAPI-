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

## EXERCISES response
#To use the code as query parament, it was moved up here to work properly
@app.get("/books/byauthor")
async def get_book_by_author_query(author:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

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
    

# PUT REQUEST
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
            BOOKS[i] = updated_book

# DELETE REQUEST
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


## EXERCISES

# Getting books form a specific author using query path or query parameter

## EXERCISES
#Path parameter
# TO make a query parameter, author should be removed and move thw whole code to the top
@app.get("/books/byauthor/{author}")
async def get_book_by_author_path(author:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return
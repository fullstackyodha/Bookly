# FastAPI framework, high performance, easy to learn, fast to code, ready for production
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel

# FastAPI app class, the main entrypoint to use FastAPI.
app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


# RETURNS LIST OF BOOKS
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/book", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    # Generate a dictionary representation of the model
    new_book = book_data.model_dump()
    books.append(new_book)

    return new_book


@app.get("/book/{book_id}")
async def get_book_by_id(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id} not found"
    )


@app.post("/book/{book_id}")
async def update_book_by_id(book_id: int) -> dict:
    pass


@app.delete("/book/{book_id}")
async def delete_book_by_id(book_id: int) -> dict:
    pass


# @app.get("/")
# async def read_root():
#     return {"message": "Hello World!"}


# @app.get('/greet/{name}')
# async def greet_name(name:str)-> dict:
#     return {"message":f"Hello {name}!"}


# PATH & QUERY PARAMERTS
# @app.get("/greet/{name}")
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}, age: {age}!"}


# @app.get("/greet")
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}", "age": age}

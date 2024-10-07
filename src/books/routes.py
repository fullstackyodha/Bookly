from fastapi import status, APIRouter, Depends
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel
from src.db.main import get_Session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService

book_router = APIRouter()
book_service = BookService()

# RETURNS LIST OF BOOKS
@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession= Depends(get_Session)):
    all_books = book_service.get_all_books(session)
    
    return all_books


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    # Generate a dictionary representation of the model
    new_book = book_data.model_dump()
    books.append(new_book)

    return new_book


@book_router.get("/{book_id}")
async def get_book_by_id(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id} not found"
    )


@book_router.patch("/{book_id}")
async def update_book_by_id(book_id: int, updated_book_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book_data.title
            book["author"] = updated_book_data.author
            book["published_date"] = updated_book_data.published_date
            book["page_count"] = updated_book_data.page_count
            book["language"] = updated_book_data.language
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id} not found"
    )


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(book_id: int):
    book_to_delete = next((book for book in books if book["id"] == book_id), None)

    if book_to_delete:
        books.remove(book_to_delete)
        return  # No content should be returned for status 204

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found",
    )

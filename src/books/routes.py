from fastapi import status, APIRouter, Depends
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel, BookCreateModel
from src.db.main import get_Session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService

book_router = APIRouter()
book_service = BookService()


# RETURNS LIST OF BOOKS
@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_Session)):
    all_books = await book_service.get_all_books(session)

    return all_books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_Session)
) -> dict:
    new_book = await book_service.create_book(book_data, session)

    if new_book is not None:
        return new_book

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error Creating Book!!"
    )


@book_router.get("/{book_uid}", response_model=Book)
async def get_book_by_id(
    book_uid: str, session: AsyncSession = Depends(get_Session)
) -> dict:
    book = await book_service.get_book(book_uid, session)

    if book is not None:
        return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_uid} not found"
    )


@book_router.patch("/{book_uid}", response_model=Book)
async def update_book_by_id(
    book_uid: str,
    updated_book_data: BookUpdateModel,
    session: AsyncSession = Depends(get_Session),
) -> dict:
    updated_book = await book_service.update_books(book_uid, updated_book_data, session)

    if updated_book is not None:
        return updated_book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_uid} not found"
    )


@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(
    book_uid: str,
    session: AsyncSession = Depends(get_Session),
):
    book_to_delete = await book_service.delete_book(book_uid, session)

    if book_to_delete:
        return None

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_uid} not found",
    )

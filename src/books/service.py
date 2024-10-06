from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel
from sqlmodel import select, desc
from .models import Book


class BookService:

    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))

        result = await session.exec(statement)
        return result.all()

    async def get_books(self, book_uuid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uuid)

        result = await session.exec(statement)
        return result.first()

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        pass

    async def update_books(self, book_uuid: str, session: AsyncSession):
        pass

    async def delete_book(self, book_uuid: str, session: AsyncSession):
        pass

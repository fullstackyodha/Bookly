from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel,BookUpdateModel
from sqlmodel import select, desc
from .models import Book


class BookService:

    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))

        result = await session.exec(statement)
        return result.all()

    async def get_book(self, book_uuid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uuid)

        result = await session.exec(statement)
        book =  result.first()
        
        return book	if book is not None else None

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Book(**book_data_dict)
        
        # Place an object into this _orm.Session
        session.add(new_book)
        # ommit the current transaction in progress
        await session.commit()

        # Return the new object                     
        return new_book
        

    async def update_books(self, book_uuid: str, updated_data:BookUpdateModel,session: AsyncSession):
        book_to_update = await self.get_book(book_uuid, session)
        
        if book_to_update is not None:
            update_data_dict = updated_data.model_dump()

            for k,v in update_data_dict.items():
                setattr(book_to_update,k,v)

            await session.commit()                          
            return book_to_update
        else:
            return None	

    async def delete_book(self, book_uuid: str, session: AsyncSession):
        book_to_delete = await self.get_all_books( book_uuid, session)
        
        if book_to_delete is not None:
            session.delete(book_to_delete)  
            await session.commit()               
        else:
            return None	



from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
import uuid
import datetime

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID, primary_key=True, unique=True, nullable=False, default=uuid.uuid4
        )
    )
    
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified:bool = False
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


    def __repr__(self) -> str:
        return f"<User {self.username} {self.first_name} {self.last_name}>"
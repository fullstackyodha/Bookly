from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class User(BaseModel):
    uid: uuid.UUID
    username: str
    first_name: str
    last_name: str
    email: str
    password_hash: str = Field(exclude=True)
    created_at: datetime
    updated_at: datetime

class UserCreate(BaseModel):
    username: str = Field(max_length=10)
    email: str = Field(max_length=50)
    password_hash: str = Field(min_length=6, max_length=255)
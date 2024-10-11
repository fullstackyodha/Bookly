from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    password_hash: str = Field(exclude=True)
    created_at: datetime
    updated_at: datetime

class UserCreate(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)
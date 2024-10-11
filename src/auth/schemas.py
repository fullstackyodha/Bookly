from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class UserCreate(BaseModel):
    username: str = Field(max_length=10)
    email: str = Field(max_length=50)
    password_hash: str = Field(min_length=6, max_length=255)
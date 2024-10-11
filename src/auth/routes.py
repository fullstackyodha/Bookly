from fastapi import status, APIRouter, Depends, HTTPException
from src.db.main import get_Session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.auth.schemas import UserCreate
from .service import UserService
from .schemas import User

auth_router = APIRouter()
user_service = UserService()


@auth_router.post("/signup", response_model= User, status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data: UserCreate, session: AsyncSession = Depends(get_Session)):
    email = user_data.emai
    
    user_exists = await user_service.user_exists(email, session)
    
    if user_exists:
        raise  HTTPException( status_code=status.HTTP_403_FORBIDDEN, detail="User with email already exists!!")
    
    new_user = await user_service.create_user(user_data, session) 
      
    return new_user
        
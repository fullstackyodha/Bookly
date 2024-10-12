from fastapi import status, APIRouter, Depends, HTTPException, responses
from src.db.main import get_Session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.auth.schemas import UserCreate
from .service import UserService
from .schemas import UserCreate, UserModel, UserLogin
from .utlity import create_access_token, decode_access_token, verify_password
from datetime import timedelta

REFRESH_TOKEN_EXP = 2

auth_router = APIRouter()
user_service = UserService()


@auth_router.post(
    "/signup", response_model=UserModel, status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_data: UserCreate, session: AsyncSession = Depends(get_Session)
):
    email = user_data.email

    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with email already exists!!",
        )

    new_user = await user_service.create_user(user_data, session)

    return new_user


@auth_router.post("/login")
async def login_user(
    login_data: UserLogin, session: AsyncSession = Depends(get_Session)
):
    email = login_data.email
    password = login_data.password

    user = await user_service.get_user_by_email(email, session)

    if user is not None:
        password_verified = verify_password(password, user.password_hash)

        if password_verified:
            access_token = create_access_token(
                user_data={
                    "user_uid": str(user.uid),
                    "email": user.email,
                    "username": user.username,
                }
            )

            refresh_token = create_access_token(
                user_data={
                    "user_uid": str(user.uid),
                    "email": user.email,
                    "username": user.username,
                },
                expiry=timedelta(days=REFRESH_TOKEN_EXP),
                refresh=True,
            )

            return responses.JSONResponse(
                content={
                    "message": "Login Successfull.",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {
                        "user_uid": str(user.uid),
                        "email": user.email,
                        "username": user.username,
                    },
                },
                status_code=status.HTTP_200_OK,
            )

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User not found!!",
    )

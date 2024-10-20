from passlib.context import CryptContext
from datetime import datetime, timedelta
from src.config import Config
import jwt
import uuid

password_context = CryptContext(schemes=["bcrypt"])
ACCESS_TOKEN_EXP = 3600


def generate_password_hash(password: str) -> str:
    # run secret through selected algorithm, returning resulting hash.
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    # verify secret against an existing hash.
    return password_context.verify(password, hashed_password)


def create_access_token(
    user_data: dict, expiry: timedelta = None, refresh: bool = False
):
    payload = {}

    payload["user"] = user_data
    payload["expires"] = (
        datetime.now()
        + (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXP))
    ).strftime("%Y-%m-%d %H:%M:%S.%f")

    payload["jti"] = str(uuid.uuid4())  # JSON Web Token Identifier
    payload["refresh"] = refresh

    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET_KEY,
        algorithm=Config.JWT_ALGO,
    )

    return token


def decode_access_token(token: str):
    try:
        token_data = jwt.decode(
            jwt=token, key=Config.JWT_SECRET_KEY, algorithms=[Config.JWT_ALGO]
        )

        return token_data
    except jwt.PyJWTError as e:
        return None

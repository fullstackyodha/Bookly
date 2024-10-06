# FastAPI framework, high performance, easy to learn, fast to code, ready for production
from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is Starting...")
    # CONNECT TO DB
    await init_db()

    yield
    print("Server has Stopped!!")


version = "v1"

# FastAPI app class, the main entrypoint to use FastAPI.
app = FastAPI(title="Bookly", version=version, lifespan=life_span)


# Include an APIRouter in the same app
app.include_router(
    book_router,
    prefix=f"/api/{version}/books",
    tags=["books"],
)

# @app.get("/")
# async def read_root():
#     return {"message": "Hello World!"}


# @app.get('/greet/{name}')
# async def greet_name(name:str)-> dict:
#     return {"message":f"Hello {name}!"}


# PATH & QUERY PARAMERTS
# @app.get("/greet/{name}")
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}, age: {age}!"}


# @app.get("/greet")
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}", "age": age}

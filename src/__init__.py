# FastAPI framework, high performance, easy to learn, fast to code, ready for production
from fastapi import FastAPI, status


# FastAPI app class, the main entrypoint to use FastAPI.
app = FastAPI()


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

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.get("/")
def root():
    return JSONResponse(content={"message": "Hello, World!"}, status_code=200)


@app.post("/user")
def create_user(user: User, request: Request):
    accept_header = request.headers.get("Accept")
    if accept_header != "text/plain":
        return JSONResponse(content={"message": "Unsupported Media Type"}, status_code=400)
    return JSONResponse(content={"User": user.model_dump()}, status_code=200)


@app.get("/user")
def get_user():
    example_user = User(name="Jean", age=25)
    return JSONResponse(content={"User": example_user.model_dump()}, status_code=200)


@app.get("/ping")
def get_ping():
    return("pong")


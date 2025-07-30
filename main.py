from fastapi import FastAPI
from starlette.responses import JSONResponse, Response
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int

@app.get("/")
def root():
    return JSONResponse(content={"Default message Root": "Hello, World!"}, status_code=200)

@app.get("/hello")
def read_hello():
    with open("./hello.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")

@app.get("/welcome")
def welcome_user(name: str):
    return { f"Bienvenue {name}"}



@app.post("/Players")
def create_players(list)
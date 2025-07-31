from datetime import datetime
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse, Response
from pydantic import BaseModel
from typing import List

app = FastAPI()
class Post(BaseModel):
    author: str
    title: str
    content :str
    creation:datetime

#@app.post("/user")
#def create_user(user: User, request: Request):
#    accept_header = request.headers.get("Accept")
#    if accept_header != "text/plain":
#        return JSONResponse(content={"message": "Unsupported Media Type"}, status_code=400)
#    return JSONResponse(content={"User": user.model_dump()}, status_code=200)


@app.get("/user")
def get_user():
    example_user = User(name="Jean", age=25)
    return JSONResponse(content={"User": example_user.model_dump()}, status_code=200)


@app.get("/ping")
def get_ping():
    return Response("pong" , status_code = 200)

@app.get("/home")
def read_home():
    with open("./welcome.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    with open("notFound.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=404, media_type="text/html")

post_memory: List[Post] = []
@app.post("/posts", status_code=201)
def create_players(list_posts: List[Post]):
    post_memory.extend(list_posts)
    return post_memory

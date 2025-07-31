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
post_memory: List[Post] = []

@app.get("/posts",status_code=200)
def get_players():
    return  post_memory;

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

@app.post("/posts", status_code=201)
def create_players(list_posts: List[Post]):
    post_memory.extend(list_posts)
    return post_memory

@app.put("/posts")
def change_posts(newPost: Post):
    for i, post in enumerate(post_memory):
        if post.title == newPost.title:
            post_memory[i] = newPost
            return {"message": "post modifié", "posts": post_memory}
    post_memory.append(newPost)
    return {"message": "Nouveau post  ajouté", "players": post_memory}

#@app.get("/ping/auth")
#def
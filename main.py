
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse, Response
from pydantic import BaseModel
from typing import List
class Player(BaseModel):
    number: int
    name: str

app = FastAPI()

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

# Mémoire vive (persistante tant que le serveur tourne)
players_memory: List[Player] = []
@app.post("/players", status_code=201)
def create_players(list_player: List[Player]):
    players_memory.extend(list_player)
    return players_memory

@app.get("/players",status_code=200)
def get_players():
    return  players_memory;

@app.put("/players")
def change_players(newPlayer: Player):
    for i, player in enumerate(players_memory):
        if player.number == newPlayer.number:
            players_memory[i] = newPlayer
            return {"message": "Joueur modifié", "players": players_memory}

    players_memory.append(newPlayer)
    return {"message": "Nouveau joueur ajouté", "players": players_memory}






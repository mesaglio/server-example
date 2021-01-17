from typing import List, Optional

from fastapi import APIRouter, Response

from src.model.usuario import Usuario

users: List[Usuario] = []

usuarios = APIRouter()


@usuarios.get("/usuarios")
async def get_user():
    return users


@usuarios.post("/usuarios")
async def create_user(user: Usuario, response: Response):
    users.append(user)
    response.status_code = 201
    return response


@usuarios.get("/usuarios/{username}", status_code=200)
async def create_user(username: str, response: Response):
    user = find_user(username)
    if user:
        return user
    response.status_code = 404
    return response


@usuarios.delete("/usuarios/{username}")
def delete_user(username: str, response: Response):
    user = find_user(username)
    if user:
        users.remove(user)
    response.status_code = 200
    return response


@usuarios.patch("/usuarios/{username}")
def update_user(username: str, req_user: Usuario, response: Response):
    user = find_user(username)
    if user:
        users.remove(user)
        users.append(req_user)
        response.status_code = 200
    else:
        response.status_code = 404
    return response


def find_user(username: str) -> Optional[Usuario]:
    for u in users:
        if u.username == username:
            return u
    return None

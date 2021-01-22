from fastapi import APIRouter

ping = APIRouter()


@ping.get("/ping")
async def pong():
    return "Pong"

import uvicorn as uvicorn
from fastapi import FastAPI
from routes.ping_route import ping
from routes.usuario_route import usuarios

app = FastAPI()

app.include_router(ping)
app.include_router(usuarios)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, debug=False, reload=False, lifespan="on")

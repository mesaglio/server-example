import uvicorn as uvicorn
from fastapi import FastAPI

from src.routes.ping_route import ping
from src.routes.usuario_route import usuarios


def create_app():
    app = FastAPI()
    app.include_router(ping)
    app.include_router(usuarios)
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run("main:create_app", host="0.0.0.0", port=8080, debug=False, reload=False, lifespan="on")

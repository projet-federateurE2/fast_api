from fastapi import FastAPI

from app.routes.route_client import router_client as router_client

app = FastAPI()

app.include_router(router_client, tags=["v1"], prefix="/v1")

@app.get("/", tags=["API Root"])
async def read_root():
    return {"message": "Welcome to ufo APP!"}

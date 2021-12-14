from fastapi import FastAPI
from routes.route_client import router_client

app = FastAPI()

app.include_router(router_client, tags=["test"], prefix="/test")

app.include_router(router_client, tags=["v1"], prefix="/v1")

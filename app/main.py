from fastapi import FastAPI
from app.routes.route_client import router_client
from app.routes.route_artisan import router_artisan

app = FastAPI()

# app.include_router(router_client, tags=["test"], prefix="/test")

app.include_router(router_client, tags=["v1"], prefix="/v1")

app.include_router(router_artisan, tags=["v1"], prefix="/v1")

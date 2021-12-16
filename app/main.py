from fastapi import FastAPI
from app.routes.route_proprietaire import router_proprietaire

app = FastAPI()

# app.include_router(router_proprietaire, tags=["test"], prefix="/test")

app.include_router(router_proprietaire, tags=["v1"], prefix="/v1")

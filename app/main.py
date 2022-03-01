from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.route_proprietaire import router_proprietaire
from app.routes.route_artisan import router_artisan
from app.routes.route_projet import router_projet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# List all routes
@app.get("/")
def list_all_routes():
    url_list = [{"path": route.path, "name": route.name}
        for route in app.routes]
    return url_list


app.include_router(router_proprietaire, tags=["v1"], prefix="/v1")

app.include_router(router_artisan, tags=["v1"], prefix="/v1")

app.include_router(router_projet, tags=["v1"], prefix="/v1")

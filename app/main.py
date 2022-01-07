from fastapi import FastAPI
from app.routes.route_proprietaire import router_proprietaire
from app.routes.route_artisan import router_artisan

app = FastAPI()

# List all routes
@app.get("/")
def list_all_routes():
    url_list = [{"path": route.path, "name": route.name}
        for route in app.routes]
    return url_list


app.include_router(router_proprietaire, tags=["v1"], prefix="/v1")

app.include_router(router_artisan, tags=["v1"], prefix="/v1")

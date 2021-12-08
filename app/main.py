from fastapi import FastAPI

<<<<<<< HEAD
from app.routes.route_client import router_client as router_client

app = FastAPI()

app.include_router(router_client, tags=["v1"], prefix="/v1")
=======
app = FastAPI()

>>>>>>> 09d56879ab7c5bba9dd12c13f9983ed9be40fa86

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
    
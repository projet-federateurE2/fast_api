from fastapi import FastAPI

from app.routes.ufos import router as UfoRouter

app = FastAPI()

app.include_router(UfoRouter, tags=["v1"], prefix="/v1")

@app.get("/", tags=["API Root"])
async def read_root():
    return {"message": "Welcome to ufo APP!"}

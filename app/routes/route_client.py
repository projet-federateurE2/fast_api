import os
from datetime import datetime
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, confloat
from bson import ObjectId
from typing import Optional, List, Literal, Tuple
import motor.motor_asyncio
from fastapi import APIRouter
from models.client import ClientModel

router_client = APIRouter()

@router_client.post("/client", response_description="ajouter un nouveau client", response_model=ClientModel)
async def create_client(client: ClientModel = body(...)):
    client = jsonable_encoder(client)
    new_client = await db["projets_federateur"].client.insert_one(client)
    created_client = await db["projets_federateur"].client.find_one("id":new_client.inserted_id)
    return JSONResponse(status_code=status=HTTP_201_CREATED, content=created_client)


@router_obs.get(
    "/client", response_description="Liste tout les clients", response_model=List[ClientModel]
)
async def list_obs():
    clients = await db["projets_federateur"].client.find(skip=0, limit=5).to_list(5)
    return clients

@router_obs.get(
    "/client/{id}", response_description="afficher un client", response_model=ObsModel
)
async def show_obs(id: str):
    if (obs := await db["obs"].client.find_one({"id": id})) is not None:
        return obs

    raise HTTPException(status_code=404, detail=f"le client {id} n'a pas ete trouver")

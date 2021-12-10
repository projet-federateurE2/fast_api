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

from database import (
    retrieve_datas,
    retrieve_data,
    insert_data,
    update_data,
    remove_data
)

router_client = APIRouter()

@router_client.post("/client", response_description="ajouter un nouveau client", response_model=ClientModel)
async def post_client(client_data : ClientModel = Body(...)):
    client = jsonable_encoder(client_data)
    new_client = await insert_ufo(client)
    return new_client


@router_client.get(
    "/client", response_description="Liste tout les clients", response_model=List[ClientModel]
)
async def get_clients():
    client = await retrieve_datas("client",id)
    if client:
        return client
    return "client doesn't exist"

@router_client.get(
    "/client/{id}", response_description="afficher un client", response_model=ClientModel
)
async def get_clients():
    client = await retrieve_data("client")
    if client:
        return client
    return "client doesn't exist"

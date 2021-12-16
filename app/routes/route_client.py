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
from app.models.user import UserModel
from app.database import common_utils

router_client = APIRouter()

@router_client.post("/client", response_description="ajouter un nouveau client", response_model=UserModel)
async def post_client(client_data : UserModel = Body(...)):
    client = jsonable_encoder(client_data)
    new_client = await common_utils.insert("client", client)
    return new_client


@router_client.get(
    "/client", response_description="Liste tout les clients", response_model=List[UserModel]
)
async def get_clients():
    client = await common_utils.get_all("client")
    if client:
        return client
    return "client doesn't exist"

@router_client.get(
    "/client/{id}", response_description="afficher un client", response_model=UserModel
)
async def get_client(id:str):
    client = await common_utils.get_one("client",id)
    if client:
        return client
    return "client doesn't exist"

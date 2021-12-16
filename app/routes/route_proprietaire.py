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
from app.models.users.Proprietaire import proprietaire

from app.database.common_utils import (
    get_all,
    get_one,
    insert,
    update,
    remove
)

router_proprietaire = APIRouter()

# Liste tout les proprietaires
@router_proprietaire.get("/proprietaire",
                         response_description="Liste tout les proprietaires",
                         response_model=List[proprietaire])
async def get_proprietaire():
    proprietaire = await get_all("proprietaire")
    if proprietaire:
        return proprietaire
    return "proprietaire doesn't exist"

# afficher un proprietaire identifié par son id
@router_proprietaire.get("/proprietaire/{id}",
                         response_description="afficher un proprietaire",
                         response_model=proprietaire)
async def get_proprietaire(id:str):
    proprietaire = await get_one("proprietaire",id)
    if proprietaire:
        return proprietaire
    return "proprietaire doesn't exist"

# ajouter un nouveau proprietaire
@router_proprietaire.post("/proprietaire",
                          response_description="ajouter un nouveau proprietaire",
                          response_model=proprietaire)

async def post_proprietaire(proprietaire_data : proprietaire = Body(...)):
    proprietaire = jsonable_encoder(proprietaire_data)
    new_proprietaire = await insert("proprietaire", proprietaire)
    return new_proprietaire

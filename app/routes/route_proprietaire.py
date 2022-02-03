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
@router_proprietaire.get("/proprietaires", response_description="Liste tous les propriétaires", response_model=List[proprietaire])
async def get_all_proprietaires():
    proprietaire = await get_all("proprietaire")
    if proprietaire:
        return proprietaire
    raise HTTPException(404, "Aucun propriétaire n'a été trouvé")

# afficher un proprietaire identifié par son id
@router_proprietaire.get("/proprietaire/{id}",
                         response_description="Afficher un propriétaire",
                         response_model=proprietaire)
async def get_one_proprietaire(id:str):
    proprietaire = await get_one("proprietaire",id)
    if proprietaire:
        return proprietaire
    raise HTTPException(404, "Le propriétaire recherché n'existe pas")

# ajouter un nouveau proprietaire
@router_proprietaire.post("/proprietaire",
                          response_description="Ajouter un nouveau propriétaire",
                          response_model=proprietaire)

async def post_proprietaire(proprietaire_data : proprietaire = Body(...)):
    proprietaire = jsonable_encoder(proprietaire_data)
    new_proprietaire = await insert("proprietaire", proprietaire)
    if new_proprietaire:
        return new_proprietaire
    raise HTTPException(500, "Erreur technique lors de l'opération")

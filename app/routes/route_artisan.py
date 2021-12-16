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
from models.user import UserModel

from database import (
    retrieve_datas,
    retrieve_data,
    insert_data,
    update_data,
    remove_data
)

router_artisan = APIRouter()

@router_artisan.get(
    "/artisans/{catArtisan}", response_description="Liste les catégories de travaux", response_model=List[ArtisanModel]
)
async def get_artisans(catArtisan):
    travaux = await retrieve_data("Artisan", "categorieArtisan", catArtisan)
    if travaux:
        return travaux
    return "error"

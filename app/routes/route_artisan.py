from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body
from app.models.artisan import Artisan

from app.database import artisan
from app.database import common_utils

router_artisan = APIRouter()

# Fonction renvoyant tous les artisans, à décommenter si utilisée pour débuggage
""" @router_artisan.get(
    "/artisans", response_description="Liste des artisans", response_model=List[Artisan]
)
async def get_artisans():
    artisans = await common_utils.get_all("Artisan")
    if artisans:
        return artisans
    return "artisans doesn't exist" """


@router_artisan.get(
    "/artisans/{catArtisan}", response_description="Liste les catégories de travaux", response_model=List[Artisan]
)
async def get_artisans_category(catArtisan):
    try:
        artisans = await artisan.get_artisans_category(catArtisan)
        return artisans
    except ValueError:
        return "error"

# Fonction permettant de post un artisan, à décommenter pour ajouter des jeux de test
""" @router_artisan.post("/artisans", response_description="ajouter un nouvel artisan", response_model=Artisan)
async def post_artisan(artisan_data : Artisan = Body(...)):
    artisan = jsonable_encoder(artisan_data)
    new_artisan = await common_utils.insert("Artisan", artisan)
    return new_artisan """

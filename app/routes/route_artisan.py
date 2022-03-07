from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, HTTPException
from app.models.artisan import Artisan

from app.database import artisan
from app.database import common_utils

router_artisan = APIRouter()


@router_artisan.get("/artisans/{catArtisan}",
                    response_description="Liste les catégories de travaux",
                    response_model=List[Artisan])
async def get_artisans_category(catArtisan):
    try:
        artisans = await artisan.get_artisans_category(catArtisan)
        if artisans:
            return artisans
        raise HTTPException(
            404, "La liste a renvoyée est vide, la catégorie n'a pas été trouvée")
    except ValueError:
        return "error"


# Ajouter un artisan
@router_artisan.post("/artisans", response_description="Ajouter un nouvel artisan", response_model=Artisan)
async def post_artisan(artisan_data: Artisan = Body(...)):
    artisan = jsonable_encoder(artisan_data)
    new_artisan = await common_utils.insert("Artisan", artisan)
    if new_artisan:
        return new_artisan
    raise HTTPException(500, "Erreur technique lors de l'opération")


# Obtenir tous les artisans
@router_artisan.get("/artisans",
                    response_description="Liste les artisans",
                    response_model=List[Artisan])
async def get_artisans():
    artisans = await common_utils.get_all("Artisan")
    if artisans:
        return artisans
    raise HTTPException(404, "Aucun artisan retourné")

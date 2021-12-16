from typing import List
from fastapi import APIRouter
from app.models.artisan import Artisan

from app.database import (
    retrieve_datas,
    retrieve_data,
    insert_data,
    update_data,
    remove_data
)

router_artisan = APIRouter()

@router_artisan.get(
    "/artisans/{catArtisan}", response_description="Liste les catégories de travaux", response_model=List[Artisan]
)
async def get_artisans(catArtisan):
    travaux = await retrieve_data("Artisan", "categorieArtisan", catArtisan)
    if travaux:
        return travaux
    return "error"

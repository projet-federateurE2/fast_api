from typing import List
from fastapi import APIRouter
from app.models.artisan import Artisan

from app.database.artisan import (
    get_artisans_category
)

router_artisan = APIRouter()

@router_artisan.get(
    "/artisans/{catArtisan}", response_description="Liste les catégories de travaux", response_model=List[Artisan]
)
async def get_artisans(catArtisan):
    artisans = await get_artisans_category(catArtisan)
    if artisans:
        return artisans
    return "error"

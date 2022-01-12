from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body
from app.models.travaux import Projet

from app.database import projet
from app.database import common_utils

router_projet = APIRouter()


@router_projet.get(
    "/projet/{id}", response_description="Renvoie un projet par son id", response_model=List[Projet]
)
async def get_projet(id):
    try:
        monProjet = await projet.get_projet(id)
        return monProjet
    except ValueError:
        return "error"

# Fonction permettant de post un projet
@router_projet.post("/projet", response_description="ajouter un nouveau projet", response_model=Projet)
async def post_projet(projet_data : Projet = Body(...)):
    projet = jsonable_encoder(projet_data)
    new_artisan = await common_utils.insert("Projets", projet)
    return new_artisan
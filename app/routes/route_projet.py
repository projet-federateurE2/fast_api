from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body
from app.models.projet import Projet

from app.database.common_utils import (
    get_one,
    insert
)

router_projet = APIRouter()


@router_projet.get(
    "/projet/{id}", response_description="Renvoie un projet par son id", response_model=Projet
)
async def get_projet(id):
    try:
        monProjet = await get_one("Projets", id)
        return monProjet
    except ValueError:
        return "error"

# Fonction permettant de post un projet
@router_projet.post("/projet", response_description="ajouter un nouveau projet", response_model=Projet)
async def post_projet(projet_data : Projet = Body(...)):
    projet = jsonable_encoder(projet_data)
    new_projet = await insert("Projets", projet)
    return new_projet
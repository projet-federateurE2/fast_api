from typing import List

from app.models.users.Proprietaire import proprietaire, updateProprietaire
from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from app.database.common_utils import (
    get_one,
    insert,
    get_all,
    remove,
    update
)

router_proprietaire = APIRouter()

# Liste tout les proprietaires

@router_proprietaire.get("/proprietaires",
                         response_description="Liste tous les propriétaires",
                         response_model=List[proprietaire])
async def get_all_proprietaires():
    proprietaire = await get_all("proprietaire")
    if proprietaire:
        return proprietaire
    raise HTTPException(404, "Aucun propriétaire n'a été trouvé")


# Afficher un proprietaire identifié par son id

@router_proprietaire.get("/proprietaire/{id}",
                         response_description="Afficher un propriétaire",
                         response_model=proprietaire)
async def get_one_proprietaire(id: str):
    proprietaire = await get_one("proprietaire", id)
    if proprietaire:
        return proprietaire
    raise HTTPException(404, "Le propriétaire recherché n'existe pas")


# Ajouter un nouveau proprietaire

@router_proprietaire.post("/proprietaire",
                          response_description="Ajouter un nouveau propriétaire",
                          response_model=proprietaire)
async def post_proprietaire(proprietaire_data: proprietaire = Body(...)):
    proprietaire = jsonable_encoder(proprietaire_data)
    new_proprietaire = await insert("proprietaire", proprietaire)
    if new_proprietaire:
        return new_proprietaire
    raise HTTPException(500, "Erreur technique lors de l'opération")


# Modifier un proprietaire

@router_proprietaire.patch("/proprietaire/update/{id}",
                           response_description="Modifier les infos et/ou les projets d'un propriétaire",
                           response_model=proprietaire)
async def update_proprietaire(id: str, proprietaire_data_update: updateProprietaire = Body(...)):
    proprietaire = {k: v for k, v in proprietaire_data_update.dict().items() if v is not None}
    try:
        new_proprietaire = await update("proprietaire", id, proprietaire)
        if new_proprietaire:
            return new_proprietaire
    except ValueError:
        raise HTTPException(404, "Le propriétaire à modifier est inexistant")
    raise HTTPException(500, "Erreur technique lors de l'opération")

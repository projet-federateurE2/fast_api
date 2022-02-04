from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, HTTPException
from app.models.projet import Projet

from app.database.common_utils import (
    get_one,
    insert,
    get_all
)

router_projet = APIRouter()

@router_projet.get("/projet/template",
    response_description= "Renvoie tout les projets",
    response_model= List[Projet]
)
async def get_all_projet():
    monProjet= await get_all("Projets")
    if(monProjet):
        return monProjet
    raise HTTPException(404, "Projet inexistant")

@router_projet.get("/projet/{id}",
    response_description= "Renvoie un projet par son id",
    response_model= Projet
)
async def get_projet(id:str):
    monProjet= await get_one("Projets", id)
    if(monProjet):
        return monProjet
    raise HTTPException(404, "Projet inexistant")
   

# Fonction permettant de post un projet
@router_projet.post("/projet",
    response_description= "ajouter un nouveau projet",
    response_model= Projet)

async def post_projet(projet_data : Projet = Body(...)):
    projet= jsonable_encoder(projet_data)
    new_projet= await insert("Projets", projet)
    return new_projet

@router_projet.get("/projets/{id}",
    response_description= "Renvoie la liste des projets d'un propriétaire donné",
    response_model= List[Projet]
)


async def get_projets_proprietaire(id:str):
    proprietaire = await get_one("proprietaire",id)
    if (proprietaire):
        listProprietes= proprietaire["proprietes"]
        if (not listProprietes): raise HTTPException(404, "Aucune propriétée trouvée pour cette personne")
        listProjets = []
        for propriete in listProprietes:
            projets= propriete["idProjet"]
            listProjets.extend(projets)

        if (listProjets):
            liste= []
            for projet in listProjets:
                projets = await get_one("Projets", projet)
                print(projets)
                if (projets != None):
                    liste.append(projets)
            if liste:
                return liste

        raise HTTPException(404, f"Le propriétaire {id} n'a pas de projets")
    raise HTTPException(status_code=404, detail="Aucun propriétaire trouvé")

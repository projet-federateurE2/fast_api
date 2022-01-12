from typing import List
from pydantic import BaseModel
from typing_extensions import Literal
from bson.objectid import ObjectId

class Conseils(BaseModel):
    type: Literal["Aide", "Avertissement"]
    texte: str

class Tache(BaseModel):
    nom: str

class Etape(BaseModel):
    nom: str
    conseils: List[Conseils]
    taches: List[Tache]

class Travaux(BaseModel):
    nom: str
    conseils: List[Conseils]
    etapes: List[Etape]

# Nom de class Template_travaux à changer
class Projet(BaseModel):
    id: str
    type: Literal["Isolation", "Chauffage", "Ventilation"]
    description: str
    pitch: str
    travaux: List[Travaux]
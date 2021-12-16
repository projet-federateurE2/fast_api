from typing import List
from pydantic import BaseModel
from typing_extensions import Literal

class Tache(BaseModel):
    nom: str

class Etape(BaseModel):
    nom: str
    conseils: List[conseils]
    taches: List[Tache]

class conseils(BaseModel):
    type: Literal["Aide", "Avertissement"]
    texte: str

class Travaux(BaseModel):
    nom: str
    conseils: List[conseils]
    etapes: List[Etape]

# Nom de class Template_travaux à changer
class Template_travaux(BaseModel):
    type: Literal["Isolation", "Chauffage", "Ventilation"]
    description: str
    pitch: str
    travaux: List[Travaux]
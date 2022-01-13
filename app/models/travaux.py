from typing import List, Optional
from pydantic import BaseModel, Field
from typing_extensions import Literal

from app.models.utils import PyObjectId


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
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    type: Literal["Isolation", "Chauffage", "Ventilation"]
    description: str
    pitch: str
    travaux: List[Travaux]
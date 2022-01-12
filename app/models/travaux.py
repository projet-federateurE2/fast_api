from typing import List, Optional
from pydantic import BaseModel, Field
from typing_extensions import Literal
from bson.objectid import ObjectId

class Conseils(BaseModel):
    type: Literal["Aide", "Avertissement"]
    texte: str

from app.models.utils import PyObjectId


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
class Template_travaux(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    type: Literal["Isolation", "Chauffage", "Ventilation"]
    description: str
    pitch: str
    travaux: List[Travaux]
from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from app.models.utils import PyObjectId
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
    id : Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    type: Literal["Isolation", "Chauffage", "Ventilation"]
    description: str
    pitch: str
    travaux: List[Travaux]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "type": "Isolation",
                "description": "string",
                "pitch": "string",
                "travaux": [
                    {
                    "nom": "string",
                    "conseils": [
                        {
                        "type": "Aide",
                        "texte": "string"
                        }
                    ],
                    "etapes": [
                        {
                        "nom": "string",
                        "conseils": [
                            {
                            "type": "Aide",
                            "texte": "string"
                            }
                        ],
                        "taches": [
                            {
                            "nom": "string"
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
}

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
    img_url_travaux: str
    conseils: List[Conseils]
    etapes: List[Etape]


# Nom de class Template_travaux à changer
class Projet(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    type: Literal["Isolation", "Chauffage", "Ventilation"]
    description: str
    pitch: str
    img_url_projet: str
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
                "img_url_projet": "https://i.kym-cdn.com/photos/images/newsfeed/000/925/494/218.png_large",
                "travaux": [
                    {
                        "nom": "string",
                        "img_url_travaux": "https://i.kym-cdn.com/photos/images/newsfeed/000/925/494/218.png_large",
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

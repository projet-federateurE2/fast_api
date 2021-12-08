from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId


class ClientModel(BaseModel):
    id : str
    nom : str = Field(max_length=25)
    prenom : str = Field(max_length=15)
    age : int
    #Revenu Fiscale de Reference
    rfr : int
    # En activité ou retraite
    situation : str
    propriete : list[str] = []
    coordonnee : str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "client",
                "nom": "Dujardin",
                "prenom": "jean",
                "age": "40",
                "Revenu Fiscale de Reference": "8454€",
                "situation":"en activité",
                "propriete": ["35 avenue de terrasse, Poitiers"],
                "coordonnee": "0626341285"
                }
            }

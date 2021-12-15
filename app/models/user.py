from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId

class Logement(BaseModel):
    adresse : str
    surface : int
    type : str
    idProjet : List[str]

class UserModel(BaseModel):

    email : str
    password : str
    role : str
    nom : str = Field(max_length=25)
    prenom : str = Field(max_length=15)
    situation : str
    revenu_fiscal : int
    propriete : List[Logement]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "client",
                "password" : "kdsl",
                "role" : "propriétaires",
                "nom": "Dujardin",
                "prenom": "jean",
                "situation":"en activité",
                "revenu_fiscal" : 454,
                "propriete": [{
                    "adresse":"32 avenue des terrasses",
                    "surface" : 35,
                    "type":"appartement",
                    "idProjet":[
                        "aaaaa"
                    ]
                }]
            }
        }

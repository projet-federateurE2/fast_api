from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from pydantic.networks import EmailStr

class UserModel(BaseModel):
    email : EmailStr
    role : Literal["Conseiller", "Propriétaire", "Admin"]
    nom : str = Field(max_length=25)
    prenom : str = Field(max_length=15)
    
"""     class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "client",
                "role" : "propriétaires",
                "nom": "Dujardin",
                "prenom": "jean",
                "situation":"Actif",
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
        } """

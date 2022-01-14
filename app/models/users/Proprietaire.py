from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel
from bson.objectid import ObjectId
from pydantic.networks import EmailStr
from app.models.user import UserModel

class Logement(BaseModel):
    adresse : str
    surface : int
    type : Literal["Maison", "Appartement"]
    idProjet : List[str]

class proprietaire(UserModel):
    situation : Literal["Actif", "Retraité", "Sans emploi"]
    revenu_fiscal: int
    proprietes: List[Logement]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "jean.dujardin@laposte.fr",
                "role" : "Propriétaire",
                "nom": "Dujardin",
                "prenom": "Jean",
                "situation":"Actif",
                "revenu_fiscal" : 21000,
                "proprietes": [{
                    "adresse":"32 avenue des terrasses",
                    "surface" : 35,
                    "type":"Appartement",
                    "idProjet":[
                        "aaaaa"
                    ]
                }]
            }
        }
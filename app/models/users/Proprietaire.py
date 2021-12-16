from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel
from bson.objectid import ObjectId
from pydantic.networks import EmailStr
from app.models.user import UserModel

class Logement(BaseModel):
    adresse : str
    surface : int
    type : Literal["Maison", "Appaterment"]
    idProjet : List[str]

class Proprietaire(UserModel):
    situation : Literal["Actif", "Retraité", "Sans emploi"]
    revenue_fiscal: int
    proprietes: List[Logement]

    # class Config:
    #     allow_population_by_field_name = True
    #     arbitrary_types_allowed = True
    #     json_encoders = {ObjectId: str}
    #     schema_extra = {
    #         "example": {
    #             "email": "client",
    #             "role" : "propriétaires",
    #             "nom": "Dujardin",
    #             "prenom": "jean",
    #             "situation":"Actif",
    #             "revenu_fiscal" : 21000,
    #             "propriete": [{
    #                 "adresse":"32 avenue des terrasses",
    #                 "surface" : 35,
    #                 "type":"appartement",
    #                 "idProjet":[
    #                     "aaaaa"
    #                 ]
    #             }]
    #         }
    #     }
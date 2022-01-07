from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from bson.objectid import ObjectId


class ConseillerModel(BaseModel):
    id : str
    nom : str = Field(max_length=25)
    prenom : str = Field(max_length=15)
    client : List[str] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "AzeTrD47",
                "nom": "Naymar",
                "prenom": "jean",
                "client": ["client1","client2"]
                }
            }
class UpdateConseillerModel(BaseModel):
    id : Optional[str]
    nom : Optional[str] = Field(max_length=25)
    prenom : Optional[str] = Field(max_length=15)
    client : Optional[List[str]] = []
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "AzeTrD47",
                "nom": "Naymar",
                "prenom": "jean",
                "client": ["client1","client2"]
                }
            }

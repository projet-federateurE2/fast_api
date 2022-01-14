from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId, _random_bytes
from pydantic.networks import EmailStr
from app.models.utils import PyObjectId

class UserModel(BaseModel):
    id : Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    email : EmailStr
    role : Literal["Conseiller", "Propriétaire", "Admin"]
    nom : str = Field(max_length=25)
    prenom : str = Field(max_length=15)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "jean.dujardin@laposte.fr",
                "role": "Propriétaire",
                "nom": "Dujardin",
                "prenom": "Jean"
                }

        }

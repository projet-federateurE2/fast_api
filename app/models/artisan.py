from typing import Optional
from pydantic import BaseModel, Field
from pydantic.networks import HttpUrl, EmailStr

class Adresse(BaseModel):
    rue: str
    ville: str
    code_postal: str = Field(max_length=6)

class Artisan(BaseModel):
    categorie: str
    nom: str
    telephone: str = Field(max_length=10)
    adresse: Adresse
    email: EmailStr
    site: Optional[HttpUrl]

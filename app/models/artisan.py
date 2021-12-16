from typing import Optional
from pydantic import BaseModel
from pydantic.networks import HttpUrl, EmailStr

class Adresse(BaseModel):
    rue: str
    ville: str
    code_postal: int(max_length=6)

class Artisan(BaseModel):
    categorie: str
    nom: str
    telehpone: int(max_length=10)
    adresse: Adresse
    email: EmailStr
    site: Optional[HttpUrl]

from datetime import datetime
from typing import List, Optional

import integer as integer
from pydantic import BaseModel, Field
from bson.objectid import ObjectId

class Adresse(BaseModel):
    rue: str
    ville: str
    code_postal: int(max_length=6)

class Artisan(BaseModel):
    categorieArtisan: str
    nomArtisan: str
    telehpone: int
    adresse: List[Adresse]
    email: str
    site: Optional[str]

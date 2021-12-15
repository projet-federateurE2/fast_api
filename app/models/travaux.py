from datetime import datetime
from typing import List
class Tache(BaseModel):
    nomTache: str
class Etape(BaseModel):
    nomEtape: str
    conseils: List[conseils]
    tache: List[Tache]
class conseils(BaseModel):
    typeConseil: str
    texte: str
class Travaux(BaseModel):
    nom_travail: str
    conseils: List[conseils]
    etape: List[Etape]
class Template_travaux(BaseModel):
    typeTravaux: str
    description: str
    pitch: str
    travaux: List[Travaux]
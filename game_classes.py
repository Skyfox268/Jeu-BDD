from dataclasses import dataclass
from typing import *

@dataclass
class Entity:
    name: str
    hp: int
    max_hp : int
    attack: int
    defense: int

@dataclass
class Character(Entity):
    equipement: List["Item"]


from typing import Dict, List
from entity import Entity
from enemy import Enemy
from random import *
from db_init import MongoDBClient

class Vague:
    def __init__(self, vague_actuel: int, ennemis: List["Enemy"]):
        self.vague_actuel = vague_actuel
        self.ennemis = ennemis

        def pick_enemy(self, enemy: "Enemy") -> None:
            self.ennemis.append(enemy)

        def play_vague(self) -> None:
            pass

        def get_difficulty(self, difficulty: int) -> None:
            self.difficulty = self.mongo_client["game_db"]["difficulty"].find_one({"lap": difficulty})



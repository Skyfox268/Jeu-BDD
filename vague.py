from typing import Dict, List
from entity import Entity
from enemy import Enemy
from random import *
from db_init import MongoDBClient
from player import Player

class Vague:
    def __init__(self, vague_actuel: int, ennemis: List["Enemy"]):
        self.vague_actuel = vague_actuel
        self.ennemis = ennemis

        def pick_enemy(self, enemy: "Enemy") -> None:
            self.ennemis.append(enemy)

        def play_vague(self, player: "Player"):
            for enemy in self.ennemis:
                while enemy.is_alive() and player.is_alive():
                    player.play_turn(enemy)
                    player.attack(enemy)
                    if enemy.is_alive():
                        enemy.play_turn(player)
                        enemy.attack(player)
            return player.is_alive()

        def get_difficulty(self, difficulty: int) -> None:
            self.difficulty = self.mongo_client["game_db"]["difficulty"].find_one({"lap": difficulty})



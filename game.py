from typing import Dict, List
from player import Player
from db_init import MonsterDB, VagueDB, Difficulty, SaveDB, ItemList
from pymongo import MongoClient
from vague import Vague

class Game:
    def __init__(self, player: Player):
        self.player = player
        self.mongo_client = MongoClient()
        self.vague = Vague(1, [])

        def save_game(self, save_date: SaveDB):
            save_data = SaveDB(
                player_name=self.player.name,
                score=self.player.score,
                equipe=self.player.equipe,
                monsters=self.player.monsters,
                inventaire=self.player.inventory
            )

        def load_game(sel, lodad_save: SaveDB):
            pass

        def launch_game():
            pass

        def show_leaderboard():
            pass

        def exit_game():
            pass


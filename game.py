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

        def save_game():
            pass

        def load_game():
            pass

        def launch_game():
            pass

        def show_leaderboard():
            pass

        def exit_game():
            pass


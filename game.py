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

        def save_game(self):
            save_data = SaveDB(
                player_name=self.player.name,
                score=self.player.score,
                equipe=self.player.equipe,
                monsters=self.player.monsters,
                inventaire=self.player.inventory
            )
            return save_data

        def load_game(self, load_save: SaveDB):
            self.player.name = load_save.player_name
            self.player.score = load_save.score
            self.player.equipe = load_save.equipe
            self.player.monsters = load_save.monsters
            self.player.inventory = load_save.inventaire

        def launch_game(self):
            self.menu()
            self.save_data = self.save_game()
            if self.player.is_team_alive():
                self.play_vague()

        def show_leaderboard(self):
            leaderboard = self.mongo_client["game_db"]["scores"].find().sort("score", -1).limit(10)
            print("Classement des meilleurs scores :")
            for i, player in enumerate(leaderboard, start=1):
                print(f"{i}. {player['player_name']} - Score: {player['score']}")

        def exit_game(self):
            self.save_game(SaveDB)
            print("La partie a été sauvegardée avec succès.")
            exit()




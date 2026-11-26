from typing import Dict, List
from player import Player
from db_init import MonsterDB, VagueDB, Difficulty, SaveDB, ItemList, CharacterSaveDB, MonsterSaveDB
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
                equipe=[
                    CharacterSaveDB(
                        name=character.name,
                        hp=character.hp,
                        equipement=character.equipement,
                    )
                for character in self.player.team],
                monsters=[
                    MonsterSaveDB(
                        name=monster.name,
                        hp=monster.hp
                    )
                    for enemy in self.vague.ennemis,
                ],
                inventaire=self.player.inventory,
            )

            return save_data

        def load_game(self, player_name: str):
            return self.mongo_client["saves"].find_one({"player_name": player_name})


        def launch_game(self):
            if not self.player.is_alive():
                print(f"{self.player.name} est mort. La partie est terminée.")
                return

            self.vague.play_vague(self.player)

        def show_leaderboard(self):
            scores = (
                self.mongo_client["game_db"]["scores"]
                .find()
                .sort("score", -1)
                .limit(10)
            )
            print("Classement des meilleurs scores :")
            for i, player in enumerate(scores, start=1):
                print(f"{i}. {player['player_name']} - Score: {player['score']}")


        def exit_game(self):
            self.save_game(SaveDB)
            print("La partie a été sauvegardée avec succès.")
            exit()




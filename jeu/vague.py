from typing import List
from jeu.entities.enemy import Enemy
from jeu.player import Player


class Vague:
    def __init__(self, vague_actuel: int, ennemis: List["Enemy"]):
        self.vague_actuel = vague_actuel
        self.ennemis = ennemis

        def pick_enemies(self, enemy: "Enemy") -> None:
            self.ennemis.append(enemy)

        def play_vague(self, player: "Player"):
            #Tant qu'il reste un ennemi et que l'equipe est vivante
            while self.ennemis and player.is_team_alive():
            #1: chaque personnage vivant attaque
                for character in player.team:
                    if character.is_alive():
                        if self.ennemis:
                            target_enemy = self.ennemis[0]
                            damage_dealt = character.attack(target_enemy)
                            print(f"{character.name} attaque {target_enemy.name} et inflige {damage_dealt} points de dégâts.")
                            if not target_enemy.is_alive():
                                print(f"{target_enemy.name} est mort.")
                                self.ennemis.remove(target_enemy)
                #2 si l'ennemi est vivant, il attaque le personnage vivant
                for enemy in self.ennemis:
                    if enemy.is_alive():
                        target_character = next((character for character in player.team if character.is_alive()), None)
                        if target_character:
                            damage_dealt = enemy.attack(target_character)
                            print(f"{enemy.name} attaque {target_character.name} et inflige {damage_dealt} points de dégâts.")
                            if not target_character.is_alive():
                                print(f"{target_character.name} est mort.")
                #3 la vague s'arrete si l'equipe est vivante et que l'ennemi est mort
                if not self.ennemis and player.is_team_alive():
                    print(f"Vague {self.vague_actuel} terminée. Tous les ennemis sont morts.")
                    exit()

        def get_difficulty(self, difficulty: int) -> None:
            for difficulty in DifficultyDB:
                if difficulty["lab"] == vague_actuel//10:
                    return difficulty



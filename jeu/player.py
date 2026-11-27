from typing import Dict, List
from jeu.items.item import Item
from jeu.entities.character import Character
from jeu.entities.entity import Entity


class Player:
    def __init__(self, name: str, score: int, team: List["Character"], inventory: List["Item"]):
        self.name = name
        self.score = score
        self.team = team
        self.inventory = inventory

    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}, Team: {[character.name for character in self.team]}, Inventory: {[item.name for item in self.inventory]}"

    def create_team(self, characters: List["Character"]) -> None:
        self.team = characters

    def pick_character(self, character: "Character") -> None:
        if len(self.team) < 3:
            self.team.append(character)
        else:
            raise ValueError("Team is full. Cannot pick more characters.")

    def is_team_alive(self) -> bool:
        return any(character.is_alive() for character in self.team)

    def check_inventory(self) -> List[str]:
        return [item.name for item in self.inventory]

    def use_item(self, item: Item, target: Entity) -> None:
        if item in self.inventory:
            item.use(target)
            self.inventory.remove(item)
        else:
            raise ValueError(f"{item.name} n'est pas présent dans l'inventaire du joueur {self.name}.")

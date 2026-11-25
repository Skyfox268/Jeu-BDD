from dataclasses import dataclass
from typing import Dict, List
from item import Item
from character import Character


class Player:
    def __init__(self, name: str, score: int, team: List["Character"], inventory: List["Item"]):
        self.name = name
        self.score = score
        self.team = team
        self.inventory = inventory

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

    
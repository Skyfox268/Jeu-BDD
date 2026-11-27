from typing import Dict, List
from jeu.items.item import Item
from jeu.entities.entity import Entity
from random import *

class Enemy(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, dropable: List[Item]):
        super().__init__(name, hp, max_hp, defense, attack)
        self.dropable = dropable

    def get_dropable(self) -> List[Item]:
        return self.dropable

    def drop_loot(self) -> List[Item]:
        dropped_items = []
        for item in self.dropable:
            if random() < item.drop_rate:
                dropped_items.append(item)
        return dropped_items


    def play_turn(self, target: 'Entity') -> Dict[str, int]:
        damage_dealt = self.attack(target)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage_dealt
        }

    def is_alive(self) -> bool:
        return self.hp > 0


from typing import Dict, List
from item import Item
from entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, dropable: List[Item]):
        super().__init__(name, hp, max_hp, defense, attack)
        self.dropable = dropable

    def drop_loot(self) -> List[Item]:
        return self.dropable

    def play_turn(self, target: 'Entity') -> Dict[str, int]:
        damage_dealt = self.attack(target)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage_dealt
        }

    def is_alive(self) -> bool:
        return self.hp > 0


from dataclasses import dataclass
from typing import Dict, List


class Entity:
    name : str
    hp: int
    max_hp : int
    attack : int
    defense : int

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int) -> int:
        acutual_damage = max(damage - self.defense, 1)
        self.hp = max(self.hp - acutual_damage, 0)
        return acutual_damage

    def heal(self, amount: int) -> int:
        actual_heal = min(amount, self.max_hp - self.hp)
        self.hp += actual_heal
        return actual_heal

    def attack(self, target: 'Entity') -> int:
        damage_dealt = target.take_damage(self.attack)
        return damage_dealt

    def play_turn(self, target: 'Entity') -> Dict[str, int]:
        damage_dealt = self.attack(target)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage_dealt
        }


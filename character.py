from dataclasses import dataclass
from typing import Dict, List
from entity import Entity
from item import Item

class Character(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, equipement: List["Item"]):
        super().__init__(name, hp, max_hp, defense, attack)
        self.equipement = equipement

    def equip_item(self, item: "Item"):
        self.equipement.append(item)

    def unequip_item(self, item: "Item"):
        if item in self.equipement:
            self.equipement.remove(item)

    def is_slot_avaible(self, item_type: str) -> bool:
        for item in self.equipement:
            if item.item_type == item_type:
                return False
        return True




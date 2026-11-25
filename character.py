from dataclasses import dataclass
from typing import Dict, List
from entity import Entity

class Character(Entity):
    equipement: List['Item']
    attack: int
    defense: int

    def equip_item(self, item: 'Item') -> None:
        self.equipement.append(item)

    def unequip_item(self, item: 'Item') -> None:
        if item in self.equipement:
            self.equipement.remove(item)

    def is_slot_available(self, item: 'Item') -> bool:
        # Check if the item can be equipped based on its type
        for equipped_item in self.equipement:
            if equipped_item.item_type == item.item_type:
                return False
        return True

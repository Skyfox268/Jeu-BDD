from typing import Dict, List
from item import Item

class Equipable(Item):
    def __init__(self, name: str, description: str, drop_rate: int, rarity: str, item_type: str, stats: Dict[str, int]):
        super().__init__(name, description, drop_rate, rarity, item_type, stats)

        self.item_type = item_type

    def is_equipable(self, item_type: str) -> bool:
        if item_type not in ["consumable"]:
            return True
        return False









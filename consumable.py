from typing import Dict, List
from item import Item
from entity import Entity

class Consumable(Item):
    def __init__(self, name: str, description: str, drop_rate: int, rarity: str, item_type: str, stats: Dict[str, int]):
        super().__init__(name, description, drop_rate, rarity, item_type, stats)


    def use(self, entity: 'Entity') -> None:
        for stat, value in self.stats.items():
            if hasattr(entity, stat):
                current_value = getattr(entity, stat)
                new_value = current_value + value
                setattr(entity, stat, new_value)




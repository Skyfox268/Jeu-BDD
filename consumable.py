from typing import Dict, List
from item import Item
from entity import Entity

class Consumable(Item):
    def __init__(self, name: str, description: str, drop_rate: int, rarity: str, item_type: str, stats: Dict[str, int]):
        super().__init__(name, description, drop_rate, rarity, item_type, stats)


    def is_consumable(self) -> bool:
        if self.item_type == "consumable":
            return True
        return False
    
    def use(self, entity: 'Entity') -> None:
        if not self.is_consumable():
            raise ValueError(f"{self.name} n'est pas un objet consommable.")
        else:
            for stat, value in self.stats.items():
                if hasattr(entity, stat):
                    current_value = getattr(entity, stat)
                    new_value = current_value + value
                    setattr(entity, stat, new_value)




from typing import Dict, List

class Item:
    def __init__(self, name: str, description: str, drop_rate: int, rarity: str, item_type: str, stats: Dict[str, int]):
        self.name = name
        self.description = description
        self.drop_rate = drop_rate
        self.rarity = rarity
        self.item_type = item_type
        self.stats = stats

        def __str__(self):
            return f"{self.name} (Description: {self.description}, Drop Rate: {self.drop_rate}, Rarity: {self.rarity}, Type: {self.item_type}, Stats: {self.stats})"
    




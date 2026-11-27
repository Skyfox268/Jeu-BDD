from typing import Dict, List
from jeu.entities.entity import Entity
from jeu.items.item import Item

class Character(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, equipement: List["Item"]):
        super().__init__(name, hp, max_hp, defense, attack)
        self.equipement = equipement
    
    def equip_item(self, item: "Item"):
        if not self.is_slot_avaible(item.item_type):
            raise ValueError(f"Slot '{item.item_type}' est déja occupé.")
        self.equipement.append(item)

    def unequip_item(self, item: "Item"):
        if item in self.equipement:
            self.equipement.remove(item)

    def is_slot_avaible(self, slot_name: str) -> bool:
        for slot in self.equipement:
            if slot.item_type == slot_name:
                return False
        return True

    def get_equipement(self, slot_name: str) -> List["Item"]:
        for item in self.equipement:
            if item.item_type == slot_name:
                return item
        return None

    def project_damage(self, target: 'Entity') -> int:
        projected_damage = max(self.attack - target.defense, 1)
        return projected_damage

    def play_turn(self, target: 'Entity') -> Dict[str, int]:
        damage_dealt = self.attack(target)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage_dealt
        }

    def is_alive(self) -> bool:
        return self.hp > 0




import os
from pymongo import MongoClient

client  = MongoClient("mongodb://localhost:27017/")
db = client["jeu_db"]
collection_heros = db["Heros"]
collection_ennemies = db["Monsters"]

monsters = [
    {"Gobelin": {"ATK": 10, "DEF": 5, "PV": 50}},
    {"Orc": {"ATK": 20, "DEF": 8, "PV": 120}},
    {"Dragon": {"ATK": 35, "DEF": 20, "PV": 300}},
    {"Zombie": {"ATK": 12, "DEF": 6, "PV": 70}},
    {"Troll": {"ATK": 25, "DEF": 15, "PV": 200}},
    {"Spectre": {"ATK": 18, "DEF": 10, "PV": 100}},
    {"Golem": {"ATK": 30, "DEF": 25, "PV": 250}},
    {"Vampire": {"ATK": 22, "DEF": 12, "PV": 150}},
    {"Loup-garou": {"ATK": 28, "DEF": 18, "PV": 180}},
    {"Squelette": {"ATK": 15, "DEF": 7, "PV": 90}},
]

heros = [
    {"Guerrier": {"ATK": 15, "DEF": 10, "PV": 100}},
    {"Mage": {"ATK": 20, "DEF": 5, "PV": 80}},
    {"Archer": {"ATK": 18, "DEF": 7, "PV": 90}},
    {"Voleur": {"ATK": 22, "DEF": 8, "PV": 85}},
    {"Paladin": {"ATK": 14, "DEF": 12, "PV": 110}},
    {"Sorcier": {"ATK": 25, "DEF": 3, "PV": 70}},
    {"Chevalier": {"ATK": 17, "DEF": 15, "PV": 120}},
    {"Moine": {"ATK": 19, "DEF": 9, "PV": 95}},
    {"Berserker": {"ATK": 23, "DEF": 6, "PV": 105}},
    {"Chasseur": {"ATK": 16, "DEF": 11, "PV": 100}},
    {"Dieu de la guerre": {"ATK": 190, "DEF": 20, "PV": 10000}},
    ]

collection_heros.insert_many(heros)
collection_ennemies.insert_many(monsters)
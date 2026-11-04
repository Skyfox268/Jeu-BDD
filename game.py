from db_init import collection_heros, collection_ennemies
import random
from utils import afficher_creating_team
import json 
TEAM_SIZE = 3


#############################################  PARTIE MENU  ############################################################


#Choix du pseudo par l'utilisateur
def ask_pseudo(pseudo):
    while True:
        pseudo = input("Entre le pseudo souhaité de maximum 10 caractères : ")
        if is_pseudo_valide(pseudo):
            return pseudo
        print("Pseudo invalide veuillez utiliser seulement des lettres et au maximum 10 caractères")
    

#Validité du pseudo rentré par l'utilisateur
def is_pseudo_valide(pseudo):
    if pseudo.isalpha() and len(pseudo) <= 10:
        return True
    return False

#Verification de la validité du choix du menu
def is_player_choice_valide(choice):
    return choice in ["1", "2", "3"]

#Menu du début avec choix de lancer jeu, afficher les scores ou quitter le jeu
def ask_choice_menu():
    while True:
        choice = input("Veuillez choisir une option entre 1, 2 et 3 : ")
        if is_player_choice_valide(choice):
            return choice
        print("Choix invalide. Veuillez entre un chiffre correspondant entre 1 et 3")

#Menu du jeu 
def choix_menu():
    while True:
        choice = ask_choice_menu()
        if choice == "1":
           print("Lancement du jeu...")
           start_game()
        elif choice == "2":
            print("Vous avez choisi d'afficher les scores")
            leaderboard()
        elif choice == "3":
            print("Vous avez choisi de quitter le jeu")
            quit_game()

#Commencer jeu
def start_game():
    pseudo = ask_pseudo("")
    team = choose_heros()
    show_team(team)
    print("Le jeu commence !")

#Afficher classement
def leaderboard():
    print("Voici le classement des joueurs :")

#Quitter
def quit_game():
    print("Merci d'avoir joué !")
    exit()


############################################################  PARTIE HEROS  ############################################################



#Recuperer heros
def get_heros():
    #recuperer et mettre dans une liste les heros de la bdd
    return list(collection_heros.find())

#Montrer les heros disponibles
def show_heros():
    heros = get_heros()
    print("========================")
    print("Voici les heros disponibles")
    #boucle 
    for index, hero in enumerate(heros, start = 1):
        #montrer hero avec index et stats
        show_hero(index, hero)
    print()
    print("Veuillez en choisir le nombre necessaire pour former votre équipe pour votre équipe en utilisant les chiffres de 1 à 9 correspondant à chaque héros.")
    print("========================")

#Condition de completion de la team
def team_complete(team):
    #si longeur de team est egale au max de heros
    return len(team) == TEAM_SIZE

#Verification de la validité du choix rentré par l'user
def is_team_choice_valide(choice, heros):
    #verifier si choix ciffre et si choix compris dans intervalle
    return (choice.isdigit() and 1<= int(choice) <= len(heros))

#Demander le choix du hero au user
def ask_choice_heros(heros, team):
    afficher_creating_team(team)
    while True:
        #demander choix a user
        choice = input(f"Veuillez choisir un héros entre 1 et {len(heros)} : ")
        #si choix valide et que team pas complete 
        if is_team_choice_valide(choice, heros) and not team_complete([]):
            #retourner choix de user converti
            return int(choice)
        #renvoyer au user message derreur si choix pas valide
        print(f"Choix invalide. Veuillez entrer un chiffre entre 1 et {len(heros)}.")

#Choix des heros et insertion dans une liste pour visualiser la team
def choose_heros():
    #recuperer heros dans une variable
    heros = get_heros()
    #montrer heros avec future fonction show_heros()
    show_heros()
    #créer un tab pour stocker liste finale
    chosen_heros = []
    #tant que team pas complete
    while not team_complete(chosen_heros):
        #demander choix au user
        choice = ask_choice_heros(heros)
        #ajouter le hero choisi dans la liste finale
        hero = heros[choice - 1]
        chosen_heros.append(heros)
        #retourner la liste au user
        return chosen_heros

#Patron d'affichage propre d'un personnage
def show_hero(index, hero):
    #recuperer les stats avec les clés
    name = next(key for key in hero if key != "_id")
    stats = hero[name]
    print(f"{index}. {name} - ATK: {stats['ATK']}, DEF: {stats['DEF']}, PV: {stats['PV']}")

#Afficher la team a l'utilisateur
def show_team(team):
    print()
    print("========================")
    print("Voici votre équipe :")
    for index, hero in enumerate(team, start = 1):
        show_hero(index, hero)
    
    print("========================")


############################################################  PARTIE MONSTRES  ############################################################

#Comme pour heros on recuperer les monstres de la bdd en inserant dans liste
def get_monsters():
    return list(collection_ennemies.fin())

#Choisir aleatoirement un monstre
def choose_monster():
    monsters = get_monsters()
    if not monsters:
        print("Aucun monstre disponible.")
    return random.choice(monsters)


############################################################  PARTIE COMBAT  ############################################################



def start_round(team,monster):
    hero = choose_active_hero(team)
    attack(hero, monster)
    if monster_is_alive(monster):
        subir_attack(hero, monster)
    return monster_is_alive(monster)

def combat(team, monster):
    while team_is_alive(team) and monster_is_alive(monster):
        start_round(team, monster)

    if monster_is_alive(monster):
        return False
    print(f"Vous avez vaincu {get_character_name(monster)} !")
    return True

def get_character_stats(character):
    for key in character:
        if key != "_id":
            return character[key]
        break

def get_character_name(character):
    for key in character:
        if key != "_id":
            return key
        break

def print_stats(hero, monster):
    hero_name = get_character_name(hero)
    hero_stats = get_character_stats(hero)

    monster_name = get_character_name(monster)
    monster_stats = get_character_stats(monster)

    print(f"Stats de {hero_name} : ATK: {hero_stats['ATK']}, DEF: {hero_stats['DEF']}, PV: {hero_stats['PV']}")
    print(f"Stats de {monster_name} : ATK: {monster_stats['ATK']}, DEF: {monster_stats['DEF']}, PV: {monster_stats['PV']}")


def monster_is_alive(monster):
    stats = get_character_stats(monster)
    return stats['PV'] > 0

def hero_is_alive(hero):
   stats = get_character_stats(hero)
   return stats['PV'] > 0

def team_is_alive(team):
    for hero in team:
        if hero_is_alive(hero):
            return True
    return False
        
def choose_active_hero(team):
    for hero in team:
        if hero_is_alive(hero):
            return hero
    return ("Il n'y as plus de heros disponibles")

def calculate_damage(hero, monster):
    attacker_stats = get_character_stats(hero)
    defender_stats = get_character_stats(monster)

    damage = max(0, attacker_stats['ATK'] - defender_stats['DEF'])
    return max(1, damage)

def monster_take_damage(monster, hero):
    damage = calculate_damage(hero, monster)
    monster_stats = get_character_stats(monster)

    monster_stats['PV'] = max(0, monster_stats['PV'] - damage)
    print(f"{get_character_name(hero)} inflige {damage} point de dégats à {get_character_name(monster)} !")

def hero_take_damage(hero, monster):
    damage = calculate_damage(monster, hero)
    hero_stats = get_character_stats(hero)

    hero_stats['PV'] = max(0, hero_stats['PV'] - damage)
    print(f"{get_character_name(monster)} inflige {damage} points de dégats à {get_character_name(hero)} !")

def attack(hero, monster):
    if hero_is_alive(hero) and monster_is_alive(monster):
        monster_take_damage(monster, hero)
    
def subir_attack(hero, monster):
    if hero_is_alive(hero) and monster_is_alive(monster):
        hero_take_damage(hero, monster)
   
def count_waves():
    "..."

def end_game():
    "..."
        













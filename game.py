from db_init import *
import random
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
        choice = input("Veuillez choisir une option entre 1, 2 et 3")
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
    return list(collection_heros.find())

#Montrer les heros disponibles
def show_heros():
    print("========================")
    print("Voici les heros disponibles")
    for hero in get_heros():
        print(f"{hero}\n")
    print()
    print("Veuillez en choisir le nombre necessaire pour former votre équipe pour votre équipe en utilisant les chiffres de 1 à 9 correspondant à chaque héros.")
    print("========================")

#Condition de completion de la team
def team_complete(team):
    return len(team) == TEAM_SIZE

#Verification de la validité du choix rentré par l'user
def is_team_choice_valide(choice, heros):
    return (choice.isdigit() and 1<= int(choice) <= len(heros))

#Demander le choix du hero au user
def ask_choice_heros(heros):
    while True:
        choice = input(f"Veuillez choisir un héros entre 1 et {len(heros)} : ")
        if is_team_choice_valide(choice, heros) and not team_complete([]):
            return int(choice)
        print(f"Choix invalide. Veuillez entrer un chiffre entre 1 et {len(heros)}.")

#Choix des heros et insertion dans une liste pour visualiser la team
def choose_heros():
    heros = get_heros()
    show_heros()
    chosen_heros = []
    while not team_complete(chosen_heros):
        choice = ask_choice_heros(heros)
        hero = heros[choice - 1]
        chosen_heros.append(heros)
        return chosen_heros

#Patron d'affichage propre d'un personnage
def show_hero(index, hero):
    name = next(key for key in hero if key != "_id")
    stats = hero[name]
    print(f"{index}. {name} - "f"ATK: {stats['ATK']}, DEF: {stats['DEF']}, PV: {stats['PV']}")

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
        
def switch_hero():
    "..."

def monster_take_damage(monster, hero):
    "..."

def hero_take_damage(hero, monster):
    "..."

def attack(hero, monster):
    get_hero_stats(hero)
    get_monster_stats(monster)
    while monster_is_alive(monster) and hero_is_alive(hero):
        print_stats(hero,monster)
        monster_take_damage()
        monster_is_alive(monster)    

def subir_attack(hero, monster):
    get_hero_stats(hero)
    get_monster_stats(monster)
    while monster_is_alive(monster) and hero_is_alive(hero):
        print_stats(hero,monster)
        hero_take_damage()
        hero_is_alive(hero)

def count_waves():
    "..."

def end_game():
    "..."
        













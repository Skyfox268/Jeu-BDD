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
    if choice.isdigit() and choice < 4 and choice > 0:
        return True
    else:
        return ("Le choix doit être fait avec les chiffres de 1 à 3 seulement")

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
    return list(collection_heros["Heros"].find())

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
    maximum_heros = None
    if len(team) == maximum_heros:
        return True

#Verification de la validité du choix rentré par l'user
def is_team_choice_valide(choice):
    choice = input("Veuillez choisir les heros que vous souhaitez inserer dans votre équipe")
    if choice.isdigit() and choice <10 and choice >0:
        return True
    else:
        return ("Le choix des heros doit être fait avec les chiffres de 1 à 9 seulement")

#Choix des heros et insertion dans une liste pour visualiser la team
def choose_heros(heros, choice):
    heros = get_heros()
    show_heros()
    chosen_heros = []
    while not team_complete(chosen_heros) and is_team_choice_valide(choice):
        chosen_heros.append(heros(choice[-1]))
        return chosen_heros


#Afficher la team a l'utilisateur
def show_team(team):
    team = choose_heros()
    print()
    print("========================")
    print("Voici votre équipe :")
    for hero in team:
        print(f"{hero}\n")
    print("========================")


############################################################  PARTIE MONSTRES  ############################################################


#Choisir aleatoirement un monstre
def choose_monster():
    monsters = list(collection_ennemies["Monsters"].find())
    choosen_monster = random.choice(monsters)
    return choosen_monster



############################################################  PARTIE COMBAT  ############################################################



def start_round(team,monster):
    team = choose_heros()
    monster = choose_monster()
    combat(team, monster)

def combat(team, monster):
    while team_is_alive(team):
        start_round(team, monster)
        while monster_is_alive(monster):
            attack(team,monster)
            if hero_is_alive(team):
                subir_attack(team,monster)

def get_hero_stats(hero):
    hero_stats = collection_heros.find_one({"Heros": hero})
    return hero_stats["Heros"][hero]

def get_monster_stats(monster):
    monster_stats = collection_ennemies.find_one({"Monsters": monster})
    return monster_stats["Monsters"][monster]

def print_stats(hero, monster):
    hero_stats = get_hero_stats(hero)
    monster_stats = get_monster_stats(monster)
    print(f"Stats de {hero} : ATK: {hero_stats['ATK']}, DEF: {hero_stats['DEF']}, PV: {hero_stats['PV']}")
    print(f"Stats de {monster} : ATK: {monster_stats['ATK']}, DEF: {monster_stats['DEF']}, PV: {monster_stats['PV']}")

def monster_is_alive(monster):
    while True:
        stats = get_monster_stats(monster)
        if stats <= 0:
            print(f"{monster} est mort !")
            return False
        break
    return stats

def hero_is_alive(hero):
    while True:
        stats = get_hero_stats(hero)
        if stats <= 0:
            print(f"{hero} est mort !")
            return switch_hero()
        break
    return stats

def team_is_alive(team):
    for hero in team:
        if hero_is_alive(hero):
            return True
        
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
        













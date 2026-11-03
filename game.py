from db_init import collection_ennemies, collection_heros
import random


#Choix du pseudo par l'utilisateur
def ask_pseudo(pseudo):
    pseudo = input("Entre le pseudo souhaité de maximum 10 caractères : ")
    if pseudo.isalpha() and len(pseudo) <= 10:
        return pseudo
    else:
        print("Le pseudo doit contenir uniquement des lettres et ne pas dépasser 10 caractères.")
        return ask_pseudo(pseudo)

#Verification de la validité du choix 
def is_player_choice_valide(choice):
    if choice.isdigit() and choice < 4 and choice > 0:
        return True
    else:
        return ("Le choix doit être fait avec les chiffres de 1 à 3 seulement")

#Menu du début avec choix de lancer jeu, afficher les socres ou quitter le jeu
def lancement():
    choice = int("Entre votre choix")
    if not is_player_choice_valide(choice):
        print("Le choix doit être fait avec les chiffres de 1 à 3 seulement")
        return lancement()
    else:
        choix_menu()

def choix_menu():
    while True:
        if lancement() == 1:
            pseudo = ask_pseudo()
            print(f"Bienvenue {pseudo} dans le jeu !")
            start_game()
        elif lancement() == 2:
            print("Vous avez choisi d'afficher les scores")
            leaderboard()
        elif lancement() == 3:
            print("Vous avez choisi de quitter le jeu")
            quit_game()

#Commencer jeu
def start_game():
    print("Le jeu commence !")

#Afficher classement
def leaderboard():
    print("Voici le classement des joueurs :")

#Quitter
def quit_game():
    print("Merci d'avoir joué !")
    exit()


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
    while not team_complete(chosen_heros):
        chosen_heros.append(heros(choice[-1]))

#Choisir aleatoirement un monstre
def choose_monster():
    monsters = list(collection_ennemies["Monsters"].find())
    choosen_monster = random.choice(monsters)
    return choosen_monster















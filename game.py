from db_init import *
import random


#############################################  PARTIE MENU  ############################################################


#Choix du pseudo par l'utilisateur
def ask_pseudo(pseudo):
    pseudo = input("Entre le pseudo souhaité de maximum 10 caractères : ")
    if is_pseudo_valide(pseudo):
        return pseudo
    else:
        ask_pseudo(pseudo)

#Validité du pseudo rentré par l'utilisateur
def is_pseudo_valide(pseudo):
    if pseudo.isalpha() and len(pseudo) <= 10:
        return True
    else:
        return ("Le pseudo doit contenir uniquement des lettres et ne pas dépasser 10 caractères.")

#Verification de la validité du choix du menu
def is_player_choice_valide(choice):
    if choice.isdigit() and choice < 4 and choice > 0:
        return True
    else:
        return ("Le choix doit être fait avec les chiffres de 1 à 3 seulement")

#Menu du début avec choix de lancer jeu, afficher les scores ou quitter le jeu
def lancement():
    choice = input("Veuillez choisir une option entre 1 et 3 : ")
    if not is_player_choice_valide(choice):
        print("Le choix doit être fait avec les chiffres de 1 à 3 seulement")
        return lancement()
    else:
        choix_menu()
        return choice

#Menu du jeu 
def choix_menu():
    while True:
        if lancement() == 1:
            pseudo =ask_pseudo()
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
    while not team_complete(chosen_heros):
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


"ATTAQUER"

#Definir attack

    #Recuperer les stats du hero 
    #Recuperer les stats du monstre ainsi que son nom
        #Boucle
            #Afficher vie et defense du monstre
            #Mettre damage au monstre avec vie monstre = vie monstre - atk hero
            #Check monstre_is_alive


#monster_is_alive()
    #recuperer stats du monstre après attack
    #comparer cette valeur avec 0
    #SI vie <= 0
        #indiquer monstre battu 
    #SINON
        #indiquer combien de vie reste au monstre 
    
"SUBIR ATTAQUE"

#Definir subir_attak

    #Recuperer stats hero 
    #Recuperer stats monstre
        #Boucle
            #Afficher vie et defense du hero 
            #Mettre damage au hero avec vie hero = vie hero - atk monstre
            #Chek hero_is_alive

#hero_is_alive()
    #recuperer stats du hero après atak
    #comparer la valeur avec 0
    #SI vie <= 0
        #indiquer si hero encore vivant
    #SI
        #indiquer combien de vie restante
    #SINON 
        #Proposer de changer le heros si hero mort ( switch_hero )















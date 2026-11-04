from game import *

def display_menu_choices():
    print("\n+------------------------------------+")
    print("|        BIENVENUE SUR LE JEU        |")
    print("+------------------------------------+")
    print("| [1]  Demarrer le jeu               |")
    print("| [2]  Voir les scores               |")
    print("| [3]  Quitter                       |")
    print("+------------------------------------+")

def afficher_creating_team(team):
    if not team_complete(team):
        print("Avant de commencer vous devez créer une équipe")
    print("Votre équipe est déja complete, demarrage du jeu...")








################# AFFICHAGE DU JEU ET DU MENU #################

#Dans message box 
#Afficher bienvenue
#Afficher regles du jeu
#Afficher les choix possibles du menu 
    #print 1 pour lancer
    #print 2 pour leaderboard
    #print 3 pour quitter
    #(l'utilisateur choisi) --> lance les fonctions associées

#SI user lance jeu et que verifier team is complete == False:
    #Afficher un message "choisir pseudo"
    #Afficher un message "vous devez choisir une équipe de TEAM_SIZE heros pour commencer le jeu"
    #Afficher le menu pour choisir une équipe


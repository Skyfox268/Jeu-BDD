def afficher_en_forme_jeu():
    print("=====================")
    print("Bienvenue dans le jeu")
    print("=====================")
    print("Les règles sont les suivantes:")
    print("1. Tu devra choisir une équipe de 3 heros")
    print("2. Un ennemi apparaitera aléatoirement, tu devra le battre pour passer a la vague suivante")
    print("3. Si un de tes heros meurt, le jeu te demandera de choisir qui tu veux envoyer combattre")
    print("=====================")

def afficher_menu():
    print("=====================")
    print("Vous avez 3 choix possibles :")
    print("=====================")
    print("Appuyez sur 1 pour lancer le jeu")
    print("Appuyez sur 2 pour afficher les scores")
    print("Appuyez sur 3 pour quitter le jeu")

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
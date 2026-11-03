
Structure 

- Avant le debut du jeu
    -Bienvenue + affichage des regles
    -Demande a l'utilisateur son pseudo 
        .Verifier si input valide
        .Ajouter le pseudo a la BDD pour le score
    -Affiche les personnages jouables a l'utilisateur
        .Demande a l'utilisateur de choisir avec 1 2 ou 3 (3 perso maxi)
        .Verifier si les inputs de l'user sont valables
        .Ajouter les heros a la main de l'user
    -Montrer la main de heros au joueur
        .Lui demander si il souhaite changer ou valider definitivement
            .Ajouter l'equipe definitvement a la bdd
    
    -Lancement du jeu 
    Dans une boucle :
        -Faire apparaitre un monstre aleatoirement
        -Afficher a l'user qu'un monstre est apparu et afficher ses caracteristiques
        -COMBAT :
            -Tirer aleatoirement le premier qui attaque
                si monstre attaque en premier:
                    vie de heros = vie de heros - attaque de monstre
                sinon : 
                    vie de monstre = vie de monstre - attaque de heros
                
            - Si monstre mort :
                message disant que il a tue un ennemi 
                respawn aleatoire d'un ennemi
                vague + = 1
            
             si heros mort : 
              message disant que un des heros est mort
              passer au heros suivant dans la main
            
        sinon:
            continuer combat
        
        -FIN COMBAT : 
            si plus de heros :
                message disant fin de partie vous avez perdu 
                afficher nombre de vagues
                enregistrer score dans bdd
            
            sinon : 
                si vague = 20
                afficher victoire
                enregistrer victoire




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
            

def combat()
    tant que la team est en vie 
        start round
        tant que ennemi en vie 
            attaquer ennemi
            si hero est en vie 
                monstre attaque hero


#######################  LOGIQUE PRINCIPALE DU JEU ############################

######### AFFICHAGE DU DEBUT ########

Message de bienvenu du jeu 
Règles
Afficher menu avec 3 choix possibles
lancement des choix :
    demander choix a user
    si choix player valide:
        on lance le menu et on retourne le choix fais par le user
        
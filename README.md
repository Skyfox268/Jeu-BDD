
#######################  LOGIQUE PRINCIPALE DU JEU ############################

######### AFFICHAGE DU DEBUT ########

Message de bienvenu du jeu 
Règles
Afficher menu avec 3 choix possibles
lancement des choix :
    demander choix a user
    si choix player valide:
        on lance le menu et on retourne le choix fais par le user

Menu des choix:
    Si choix user est de jouer:
        on demande pseudo a l'aide de ask_pseudo
        et on start_game
    si choix est leaderboard:
        on affiche leaderboard
    et sinon choix est quitter
        quitter game

pseudo_valide : 
    verification de validité:
        valide
    pas valide

choix_valide :
    verification;
        valide
    pas valide


###########  MENU DES HEROS ###########

on recupere les heros dans la base de données:
    on les montres a user:
        tant que team pas complete et choix de user est valide parmis les heros:
            inserer heros dans la liste chosen_heros
            retourner les heros choisis lorsque team complete fin boucle

    montrer team complete a user:
        recuperer la liste finis
        afficher en console

team_choice_valide:
    input du choix
    si choix est chiffre et choix compris dans intervalle:
        valide
    pas valide

team_complete:
    si longeur de team est egale a maximum hero possibles:
        team complete (true)
    team pas finis


##############   CHOISIR MONSTRE #############

choisir_monstre:
    on recupere monstre dans la bdd
    on en pioche un de facon random
    on le retourne


##############    BOUCLE DE JEU COMBAT    ####################

lancer le combat:
    lancer un round aleatoirement:
        choisir un monstre aleatoire = choisir_monstre
        combattre(team et monstre):
            tant que la team est vivante et tant que un monstre est présent (vivant):
                on peux lancer combat
                attaquer le monstre:
                    afficher vie monstre
                    afficher vie et degat de hero
                    vie monstre = vie monstre - degat hero
                    on verifie si le monstre est mort ou pas:
                        si vie monstre <= 0:
                            monstre mort
                        sinon
                            monstre pas mort
                Seulement si le monstre pas mort -> nous attaque:
                    afficher vie hero
                    afficher vie et degat de monstre
                    vie hero = vie hero - degat monstre
                    on verifie si hero mort ou pas:
                        si vie hero <= 0:
                            hero mort
                            switch_hero:
                                recuperer liste de hero
                                piocher un hero dans la liste et le remplacer
                        sinon continuer combat:
                            relancer un round aleatoirement:
                            repeter la boucle a l'infini
                            comptez vague:
                                si monstre mort:
                                ajouter 1 a vague




from jeu.ui.affichage import Affichage
from jeu.ui.vue import (
    OPTIONS_ECRAN_TITRE,
    OPTIONS_TOUR,
    OPTIONS_GAME_OVER,
    VueEcranTitre,
    VueSelectionEquipe,
    VueTourJoueur,
    VueChoixCible,
    VueInfoTour,
    VueInventaire,
    VueSelectionCibleObjet,
    VueGameOver,
    VueLeaderboard,
    VueChargerSauvegarde,
    VueQuitter,
)

def main():
    while True:
        choice = Affichage.display_vue(
            VueEcranTitre(),
            max_index=len(OPTIONS_ECRAN_TITRE)
        )

        if choice is None:
            continue

        if choice == 0:
            player_name = Affichage.demander_input("Entrez le nom du joueur : ")
            player = Player(name = player_name, 0)
            player.create_team([])
        elif choice == 1:
            pass  # Charger une partie
        elif choice == 2:
            pass  # Afficher le leaderboard
        elif choice == 3:
            pass  # Quitter le jeu

if __name__ == "__main__":
    main()

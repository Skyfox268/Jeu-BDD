import db_init

def ask_pseudo(pseudo):
    pseudo = input("Entre le pseudo souhaité de maximum 10 caractères : ")
    if pseudo.isalpha() and len(pseudo) <= 10:
        return pseudo
    else:
        print("Le pseudo doit contenir uniquement des lettres et ne pas dépasser 10 caractères.")
        return ask_pseudo(pseudo)

def get_heros():
    return list(db_init.db["Heros"].find())

def show_heros():
    print("========================")
    print("Voici les heros disponibles")
    for hero in get_heros():
        print(f"{hero}\n")
    print()
    print("Veuillez en choisir le nombre necessaire pour former votre équipe pour votre équipe en utilisant les chiffres de 1 à 9 correspondant à chaque héros.")
    print("========================")

def team_complete(team):
    maximum_heros = None
    if len(team) == maximum_heros:
        return True

def choice_valide(choice):
    choice = input("Veuillez choisir les heros que vous souhaitez inserer dans votre équipe")
    if choice.isdigit() and choice <10 and choice >0:
        return True
    else:
        return ("Le choix des heros doit être fait avec les chiffres de 1 à 9 seulement")

def choose_heros(heros, choice):
    heros = get_heros()
    show_heros()
    chosen_heros = []
    while not team_complete(chosen_heros):
        chosen_heros.append(heros(choice[-1]))










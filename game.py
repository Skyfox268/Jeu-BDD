from dataclasses import dataclass

@dataclass
class Preparation:
    pseudo = str
    score = int

    def ask_pseudo(self, pseudo_user):
        pseudo_user = input("Choissisez un pseudo valide")
        

    def pseudo_valide(self,pseudo_user):
            if pseudo_user.isalpha():
                 return True
            return False



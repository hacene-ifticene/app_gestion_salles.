#Implémentation de la couche Modèle
#Création de la classe salle

class Salle:
    def __init__(self, code, libelle, type_salle, capacite):
        self.code=code
        self.libelle=libelle
        self.type_salle=type_salle
        self.capacite=capacite
    def afficher_infos(self):
        print("-----Salle-----")
        print("Code :", self.code)
        print("Libelle :", self.libelle)
        print("Type_salle:", self.type_salle)
        print("Capacite :", self.capacite)
#Étape 6 : Implémentation de la couche Service (Logique métier)

from Data.dao_salle import DataSalle


class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()
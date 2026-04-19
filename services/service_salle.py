#Étape 6 : Implémentation de la couche Service (Logique métier)

from Data.dao_salle import DataSalle


class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):


        if not salle.code or not salle.libelle or not salle.type_salle or not salle.capacite:
            return False, "Données incomplètes"

        if salle.capacite < 1:
            return False, "Capacité doit être >= 1"

        try:
            self.dao.insert_salle(salle)
            return True, "Salle ajoutée avec succès"
        except Exception as e:
            return False, str(e)

    def modifier_salle(self, salle):


        if not salle.code or not salle.libelle or not salle.type_salle or not salle.capacite:
            return False, "Données incomplètes"


        if salle.capacite < 1:
            return False, "Capacité doit être >= 1"

        try:
            self.dao.update_salle(salle)
            return True, "Salle modifiée avec succès"
        except Exception as e:
            return False, str(e)

    def supprimer_salle(self, code):

        if not code:
            return False, "Code invalide"

        try:
            self.dao.delete_salle(code)
            return True, "Salle supprimée avec succès"
        except Exception as e:
            return False, str(e)

    def rechercher_salle(self, code):

        if not code:
            return None

        try:
            return self.dao.get_salle(code)
        except Exception as e:
            print("Erreur :", e)
            return None

    def recuperer_salles(self):

        try:
            return self.dao.get_salles()
        except Exception as e:
            print("Erreur :", e)
            return []
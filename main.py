#etape 5: Implémentation de la couche Data (Accès aux données)


from Data.dao_salle import DataSalle

from Data.dao_salle import DataSalle

dao = DataSalle()

try:
    salles = dao.get_salles()

    if salles:
        print(" Liste des salles :\n")
        for s in salles:
            s.afficher_infos()
            print("--------------------")
    else:
        print(" Aucune salle trouvée")

except Exception as e:
    print(" Erreur :", e)
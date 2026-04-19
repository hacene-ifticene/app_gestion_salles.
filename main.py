#etape 5: Implémentation de la couche Data (Accès aux données)


from Data.dao_salle import DataSalle

from Data.dao_salle import DataSalle

dao = DataSalle()

try:
    code = "S4"

    salle = dao.get_salle(code)

    if salle:
        salle.afficher_infos()
    else:
        print("Salle introuvable !")

except Exception as e:
    print("Erreur :", e)
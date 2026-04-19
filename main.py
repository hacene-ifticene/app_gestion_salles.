#etape 5: Implémentation de la couche Data (Accès aux données)


from Data.dao_salle import DataSalle

from Data.dao_salle import DataSalle

dao = DataSalle()

try:
    code = "S3"

    dao.delete_salle(code)

    print("✅ Suppression réussie")

except Exception as e:
    print(" Erreur :", e)
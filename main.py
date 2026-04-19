#etape 5: Implémentation de la couche Data (Accès aux données)

from Data.dao_salle import DataSalle

dao = DataSalle()

try:
    connection = dao.get_connection()
    print("Connexion réussie")
    connection.close()
except Exception as e:
    print("Erreur :", e)
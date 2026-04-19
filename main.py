#etape 5: Implémentation de la couche Data (Accès aux données)


from Data.dao_salle import DataSalle

from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

try:

    salle = Salle("S4", "Salle Réseau Modifiée", "Laboratoire", 34)

    dao.update_salle(salle)

    print("✅ Modification réussie")

except Exception as e:
    print("Erreur :", e)
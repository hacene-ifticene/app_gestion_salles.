#etape6 Implémentation de la couche Service (Logique métier)



from services.service_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

try:
    salle = Salle("S21", "Salle Service", "Laboratoire", 30)

    result = service.ajouter_salle(salle)

    print(result)

except Exception as e:
    print("❌ Erreur :", e)
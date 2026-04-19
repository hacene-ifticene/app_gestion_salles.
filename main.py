#etape6 Implémentation de la couche Service (Logique métier)

from services.service_salle import ServiceSalle

service = ServiceSalle()

print("ServiceSalle initialisé avec succès")
print("DAO connecté :", service.dao)
#etape6 Implémentation de la couche Service (Logique métier)



from services.service_salle import ServiceSalle

service = ServiceSalle()

try:
    code = "S21"

    result = service.supprimer_salle(code)

    print(result)

except Exception as e:
    print("Erreur :", e)
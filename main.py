#etape6 Implémentation de la couche Service (Logique métier)


from services.service_salle import ServiceSalle

service = ServiceSalle()

try:
    code = "S2"

    salle = service.rechercher_salle(code)

    if salle:
        print("Salle trouvée ✔")
        salle.afficher_infos()
    else:
        print("Salle introuvable")

except Exception as e:
    print("Erreur :", e)
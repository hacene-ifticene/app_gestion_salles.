#etape6 Implémentation de la couche Service (Logique métier)


from services.service_salle import ServiceSalle

service = ServiceSalle()

try:
    print("=== LISTE DES SALLES ===")

    salles = service.recuperer_salles()

    if salles:
        for s in salles:
            s.afficher_infos()
            print("------------------")
    else:
        print("Aucune salle trouvée !")

except Exception as e:
    print("Erreur :", e)
#Étape4: test du modèle Salle dans main

from models.salle import Salle

salle=Salle("S2", "Salle Informatique", "Laboratoir", 36)
salle.afficher_infos()
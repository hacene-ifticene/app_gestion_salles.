#etape 5: Implémentation de la couche Data (Accès aux données)
#Implémentation de la classe DataSalle

import mysql.connector
import json
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r") as file:
            config = json.load(file)
        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connection

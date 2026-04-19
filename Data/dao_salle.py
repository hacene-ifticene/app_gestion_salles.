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

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type_salle, salle.capacite)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE salle
        SET libelle = %s,
            type = %s,
            capacite = %s
        WHERE code = %s
        """

        values = (salle.libelle, salle.type_salle, salle.capacite, salle.code)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM salle WHERE code = %s"
        cursor.execute(sql, (code,))

        conn.commit()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "SELECT * FROM salle WHERE code = %s"
        cursor.execute(sql, (code,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return Salle(row[0], row[1], row[2], row[3])
        return None
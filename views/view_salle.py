#Étape 7 : Implémentation de l’interface graphique (GUI)

import customtkinter as ctk
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("900x600")

        self.service_salle = ServiceSalle()

        self.creer_cadre_info()

    def creer_cadre_info(self):

        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10, padx=10, fill="x")

        # Code
        ctk.CTkLabel(self.frame_info, text="Code salle").grid(row=0, column=0)
        self.code_entry = ctk.CTkEntry(self.frame_info)
        self.code_entry.grid(row=0, column=1)

        # Libellé
        ctk.CTkLabel(self.frame_info, text="Libellé").grid(row=1, column=0)
        self.libelle_entry = ctk.CTkEntry(self.frame_info)
        self.libelle_entry.grid(row=1, column=1)

        # Type
        ctk.CTkLabel(self.frame_info, text="Type").grid(row=2, column=0)
        self.type_entry = ctk.CTkEntry(self.frame_info)
        self.type_entry.grid(row=2, column=1)

        # Capacité
        ctk.CTkLabel(self.frame_info, text="Capacité").grid(row=3, column=0)
        self.capacite_entry = ctk.CTkEntry(self.frame_info)
        self.capacite_entry.grid(row=3, column=1)
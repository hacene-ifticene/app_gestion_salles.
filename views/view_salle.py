#Étape 7 : Implémentation de l’interface graphique (GUI)

import customtkinter as ctk
from tkinter import ttk
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("900x600")

        self.service_salle = ServiceSalle()

        self.creer_cadre_info()
        self.creer_cadre_actions()
        self.creer_cadre_liste()

        self.lister_salles()


    def creer_cadre_liste(self):

        self.frame_list = ctk.CTkFrame(self)
        self.frame_list.pack(pady=10, padx=10, fill="both", expand=True)

        self.tree = ttk.Treeview(
            self.frame_list,
            columns=("code", "libelle", "type", "capacite"),
            show="headings"
        )


        self.tree.heading("code", text="CODE")
        self.tree.heading("libelle", text="LIBELLE")
        self.tree.heading("type", text="TYPE")
        self.tree.heading("capacite", text="CAPACITÉ")


        self.tree.column("code", width=80)
        self.tree.column("libelle", width=200)
        self.tree.column("type", width=150)
        self.tree.column("capacite", width=100)

        self.tree.pack(fill="both", expand=True)


    def lister_salles(self):

        self.tree.delete(*self.tree.get_children())

        salles = self.service_salle.recuperer_salles()

        for s in salles:
            self.tree.insert(
                "",
                "end",
                values=(s.code, s.libelle, s.type_salle, s.capacite)
            )


    def creer_cadre_info(self):

        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.frame_info, text="Code").grid(row=0, column=0)
        self.code_entry = ctk.CTkEntry(self.frame_info)
        self.code_entry.grid(row=0, column=1)

        ctk.CTkLabel(self.frame_info, text="Libellé").grid(row=1, column=0)
        self.libelle_entry = ctk.CTkEntry(self.frame_info)
        self.libelle_entry.grid(row=1, column=1)

        ctk.CTkLabel(self.frame_info, text="Type").grid(row=2, column=0)
        self.type_entry = ctk.CTkEntry(self.frame_info)
        self.type_entry.grid(row=2, column=1)

        ctk.CTkLabel(self.frame_info, text="Capacité").grid(row=3, column=0)
        self.capacite_entry = ctk.CTkEntry(self.frame_info)
        self.capacite_entry.grid(row=3, column=1)


    def creer_cadre_actions(self):

        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10, padx=10)

        self.btn_ajouter = ctk.CTkButton(self.frame_actions, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=5)

        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=5)

        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=5)

        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=5)
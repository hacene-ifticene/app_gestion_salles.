#Étape 8 : Affichage de la liste des salles

import customtkinter as ctk
from tkinter import ttk
from models.salle import Salle
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


    def creer_cadre_info(self):

        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.frame_info, text="Code salle").grid(row=0, column=0)
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
        self.frame_actions.pack(pady=10)

        ctk.CTkButton(self.frame_actions, text="Ajouter", command=self.ajouter_salle)\
            .grid(row=0, column=0, padx=5)

        ctk.CTkButton(self.frame_actions, text="Modifier", command=self.modifier_salle)\
            .grid(row=0, column=1, padx=5)

        ctk.CTkButton(self.frame_actions, text="Supprimer", command=self.supprimer_salle)\
            .grid(row=0, column=2, padx=5)

        ctk.CTkButton(self.frame_actions, text="Rechercher", command=self.rechercher_salle)\
            .grid(row=0, column=3, padx=5)

    def creer_cadre_liste(self):

#Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "libelle", "type", "capacite"),
            show="headings"
        )

#En-têtes
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

#Largeur des colonnes
        self.treeList.column("code", width=50)
        self.treeList.column("libelle", width=150)
        self.treeList.column("type", width=100)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

    def ajouter_salle(self):
        salle = Salle(
            self.code_entry.get(),
            self.libelle_entry.get(),
            self.type_entry.get(),
            int(self.capacite_entry.get())
        )
        self.service_salle.ajouter_salle(salle)

    def modifier_salle(self):
        salle = Salle(
            self.code_entry.get(),
            self.libelle_entry.get(),
            self.type_entry.get(),
            int(self.capacite_entry.get())
        )
        self.service_salle.modifier_salle(salle)

    def supprimer_salle(self):
        code = self.code_entry.get()
        self.service_salle.supprimer_salle(code)

    def rechercher_salle(self):
        code = self.code_entry.get()
        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.libelle_entry.delete(0, 'end')
            self.libelle_entry.insert(0, salle.libelle)

            self.type_entry.delete(0, 'end')
            self.type_entry.insert(0, salle.type_salle)

            self.capacite_entry.delete(0, 'end')
            self.capacite_entry.insert(0, salle.capacite)
#Étape 7 : Implémentation de l’interface graphique (GUI)


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

        self.lister_salles()

    # ================= CADRE A =================
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

    # ================= CADRE B =================
    def creer_cadre_actions(self):

        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

        self.btn_ajouter = ctk.CTkButton(self.frame_actions, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=5)

        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=5)

        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=5)

        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=5)

    # ================= CADRE C =================
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

    # ================= CRUD =================

    def ajouter_salle(self):

        salle = Salle(
            self.code_entry.get(),
            self.libelle_entry.get(),
            self.type_entry.get(),
            int(self.capacite_entry.get())
        )

        self.service_salle.ajouter_salle(salle)
        self.lister_salles()

    def modifier_salle(self):

        salle = Salle(
            self.code_entry.get(),
            self.libelle_entry.get(),
            self.type_entry.get(),
            int(self.capacite_entry.get())
        )

        self.service_salle.modifier_salle(salle)
        self.lister_salles()

    def supprimer_salle(self):

        code = self.code_entry.get()

        self.service_salle.supprimer_salle(code)
        self.lister_salles()

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

    def lister_salles(self):

        self.tree.delete(*self.tree.get_children())

        salles = self.service_salle.recuperer_salles()

        for s in salles:
            self.tree.insert("", "end", values=(s.code, s.libelle, s.type_salle, s.capacite))
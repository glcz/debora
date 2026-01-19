#!/usr/bin/env python
import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Définition de la fenêtre principale
root = tk.Tk()
root.title("Ajout code pays dans fichier DEB")
root.geometry('600x300')

# Variables de tkinter
codepays_vartk = tk.StringVar()
fichier_vartk = tk.StringVar()

# Fonction pour choisir le fichier
def fichier_input():
    filetypes = [("All Files", "*.*"), ("Text Files", "*.txt")]
    fichier_nom = fd.askopenfilename (title="Choisissez un fichier", initialdir='/home/gregoire/Téléchargements/demodeb/', filetypes=filetypes)
    fichier_vartk.set(fichier_nom)

def codepays_validation(*args):
    label = champs['codepays_check']
    verif, errorkey = check_code()
    if not verif:
        label.config(text=err[errorkey], foreground="red")
    else:
        label.config(text="Code pays correct", foreground="green")

# Validation du code pays
def check_code():
    code = codepays_vartk.get()
    if not code:
        return False, "vide"
    if not code.isalpha():
        return False, "alpha"
    elif len(code) != 2:
        return False, "taille"
    else:
        return True, ""

def check_fichier():
    fichier_path = fichier_vartk.get()
    if not fichier_path:
        return False, "nofile"
    else:
        return True, ""

# Traitement du fichier
def traitement():
    fichier = Path(fichier_vartk.get())
    verif, errorkey_code = check_code()
    fic, errorkey_fic = check_fichier()
    if not verif:
        showinfo("Erreur", err[errorkey_code])
    elif not fic:
        showinfo("Erreur", err[errorkey_fic])
    else:
        pays = codepays_vartk.get()
        temp = fichier.with_suffix(".tmp")
        with fichier.open('r', encoding='utf-8') as lecture, temp.open('w', encoding='utf-8') as ecriture:
            entete = next(lecture)
            ecriture.write(entete)
            for ligne in lecture:
                debut = ligne[0:57]
                fin = ligne[59:]
                ecriture.write(debut + pays + fin)
        os.remove(fichier)
        os.rename(temp, fichier)
        showinfo("", "Traitement terminé")

# Gestion des erreurs
err = {
    "taille": "Le code doit être sur 2 caractères",
    "alpha": "Le code doit être des lettres",
    "nofile": "Vous devez choisir un fichier",
    "vide": "",
}

# Elements de l'interface utilisateur
champs = {
    'codepays_label': ttk.Label(root, text="Code pays"),
    'codepays_boite': ttk.Entry(root, textvariable=codepays_vartk),
    'codepays_check': ttk.Label(root, width=50),
    'fichier_label': ttk.Label(root, text="Fichier"),
    'fichier_bouton': ttk.Button(root, text='Ouvrir', command=fichier_input),
    'fichier_boite': ttk.Entry(root, textvariable=fichier_vartk, state="disabled"),
}

for item in champs.values():
    item.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

# Valider et traiter le fichier
ttk.Button(text="Traiter", command=traitement).pack(anchor=tk.W, padx=10, pady=5)
codepays_vartk.trace_add("write", codepays_validation)
root.mainloop()
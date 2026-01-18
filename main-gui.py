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

# Traitement du fichier
def traitement():
    pays = codepays_vartk.get()
    fichier = Path(fichier_vartk.get())
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

# Vérifications sur le code pays
def codepays_validation(*args):
    code = codepays_vartk.get()
    label = champs['codepays_check']
    if not code:
        label.config(text="", foreground="red")
    elif not code.isalpha():
        label.config(text="Lettres uniquement", foreground="red")
    elif len(code) > 2:
        label.config(text="Code trop long", foreground="red")
    elif len(code) < 2:
        label.config(text="Code trop court", foreground="red")
    else:
        label.config(text="Code correct", foreground="green")
        codepays_vartk.set(code.upper())

# Valider et traiter le fichier
ttk.Button(text="Traiter", command=traitement).pack(anchor=tk.W, padx=10, pady=5)
codepays_vartk.trace_add("write", codepays_validation)
root.mainloop()

# # Demander, définir et vérifier le code pays
# def pays_input():
#     while True:
#         pays_code = input("Code pays d'origine : ")
#         # pays_code = "FR"
#         if not pays_code:
#             print("Pas de code pays !")
#         elif len(pays_code) > 2:
#             print("Code pays trop long !")
#         elif len(pays_code) < 2:
#             print("Code pays trop court !")
#         elif not pays_code.isalpha():
#             print("Lettres uniquement !")
#         else:
#             return pays_code.upper()
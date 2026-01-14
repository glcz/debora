#!/usr/bin/env python
import os
from pathlib import Path

# Demander, définir et vérifier le chemin du fichier
def fichier_input():
    while True:
        fichier_chemin = input("Chemin du fichier à modifier : ")
        # fichier_chemin = "/home/gregoire/Documents/dev/debora/demo/INTRACOM.TXT"
        if not fichier_chemin:
            print("Pas de fichier sélectionné !")
        elif not os.path.exists(fichier_chemin):
            print("Le chemin est incorrect !")
        elif not os.path.isfile(fichier_chemin):
            print("Ce n'est pas un fichier !")
        else:
            return fichier_chemin

# Demander, définir et vérifier le code pays
def pays_input():
    while True:
        pays_code = input("Code pays d'origine : ")
        # pays_code = "FR"
        if not pays_code:
            print("Pas de code pays !")
        elif len(pays_code) > 2:
            print("Code pays trop long !")
        elif len(pays_code) < 2:
            print("Code pays trop court !")
        elif not pays_code.isalpha():
            print("Lettres uniquement !")
        else:
            return pays_code.upper()

# Déclaration des variables
fichier = Path(fichier_input())
temp = fichier.with_suffix(".tmp")
pays = pays_input()

# Création du fichier temporaire avec insertion du code pays
with fichier.open('r', encoding='utf-8') as lecture, temp.open('w', encoding='utf-8') as ecriture:
    entete = next(lecture)
    ecriture.write(entete)
    for ligne in lecture:
        debut = ligne[0:57]
        fin = ligne[59:]
        ecriture.write(debut + pays + fin)

# Suppression du fichier d'origine et renommage du fichier temp
os.remove(fichier)
os.rename(temp, fichier)
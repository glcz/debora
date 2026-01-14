#!/usr/bin/env python
import os
from pathlib import Path

# Demander, définir et vérifier le chemin du fichier

def fichier_input():
    while True:
        # fichier_chemin = input("Chemin du fichier à modifier : ")
        fichier_chemin = "/home/gregoire/Documents/dev/debora/demo/test.txt"
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
        # pays_code = input("Code pays d'origine : ")
        pays_code = "FR"
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

fichier = Path(fichier_input())
temp = fichier.with_suffix(".tmp")
pays = pays_input()

with fichier.open('r', encoding='utf-8') as lecture, temp.open('w', encoding='utf-8') as ecriture:
    for ligne in lecture:
        debut = ligne[0:5]
        fin = ligne[7:]
        ecriture.write(debut + pays + fin)
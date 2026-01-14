#!/usr/bin/env python
import os

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
    # pays_code = "FR"
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

fichier = fichier_input()
pays = pays_input()
print("Fichier : ", fichier)
print("Code pays : ", pays)

# Identifier les lignes à modifier (pas l'entête)
# Modifier la ligne (début + nouveau code + fin, où début = caractères avant position 58 et fin = caractères après 59)
# Créer le nouveau fichier et l'enregistrer
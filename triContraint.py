import random

def creerListe(nVal : int)-> list:
    # Génère une liste de nVal éléments
    # A adapter pour obtenir des couleurs.
    return random.choices((True, False),k=nVal)

def couleurs2(L:list)->list:
    return

def couleurs3(L:list)->list:
    return

# Génère une liste de 10 éléments
print(creerListe(10))

def init():
    L1 = [0,0,0]
    L2 = [0,0,0]
    L3 = [0,0,0]
    return [L1, L2, L3]
#grille = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

##----- Définition des Fonctions -----##
def affichage(tableau: list):
    """Cette fonction affiche à l'écran chaque ligne d'un tableau."""
    n = len(tableau)
    for i in range(n):
        print(tableau[i])

def demande(numeroJoueur : int) -> list:
    """Cette fonction renvoie la case dans laquelle le joueur se place."""
    if numeroJoueur == 1:
        print('Au tour du joueur n°1 !')
    else:
        print('Au tour du joueur n°2 !')

    ligne, colonne = input('ligne, colonne ').split(',')
    return [int(ligne), int(colonne)]

def verif(tableau : list) -> int:
    """Cette fonction calcule les sommes de chaque
    ligne/colonne/diagonale pour vérifier l'alignement.
    Elle renvoie le n° du joueur gagnant
    - renvoie 1 si le joueur 1 a gagné
    - renvoie -1 si le joueur 2 a gagné
    - renvoie 0 sinon """

    S = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
    # Il y a 8 sommes à calculer

    # Les lignes (utiliser l'instruction sum?) :

    # les colonnes

    # les diagonales

maGrosseListe = [ ['vacances', 'pizza'],['pizza','noel']  ]
affichage(maGrosseListe)

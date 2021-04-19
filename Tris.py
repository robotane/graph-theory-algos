"""
Created on Dec 2020

@author: robotane
"""


def tri_topo(graphe):
    """
    Realise le tri topologique du graphe de maniere iterative

    Parameters
    ----------
    graphe : list
        Matrice d'adjacence du graphe.

    Returns
    -------
    tri : dict
        Dictionnaire contenant les sommets range selon le tri topologique, les
        valeurs etant les sommet et les cles l'ordre du sommet dans le tri.
    """

    # Initialisation
    E = list()
    comp = dict()
    tri = list()
    rang = 0

    long = len(graphe)
    for s in range(long):
        comp[s] = 0
        for t in range(long):
            if graphe[t][s] == 1:
                comp[s] += 1
        if comp[s] == 0:
            E.append(s)

    # Traitement
    while E:
        s = E.pop()

        tri.append(s+1)
        rang += 1

        for t in range(long):
            if graphe[s][t] == 1:
                comp[t] -= 1
                if comp[t] == 0:
                    E.append(t)
    return tri


def norme(graphe):
    """
    Calcule la norme de tous les sommets du graphe

    Parameters
    ----------
    graphe : list
        Matrice d'adjacence du graphe.

    Returns
    -------
    nor : dict
        Dictionaire dont les cles sont les sommets et les valeurs les normes
        de ces sommets.

    """
    # Initialisation
    E = list()
    comp = dict()
    nor = dict()
    long = len(graphe)
    for s in range(long):
        comp[s] = 0
        nor[s] = 0
        for t in range(long):
            if graphe[t][s] == 1:
                comp[s] += 1
        if comp[s] == 0:
            E.append(s)

    # Traitement
    while E:
        s = E.pop()

        for t in range(long):
            if (graphe[t][s] == 1) and (nor[t] >= nor[s]):
                nor[s] = nor[t] + 1

        for t in range(long):
            if graphe[s][t] == 1:
                comp[t] -= 1
                if comp[t] == 0:
                    E.append(t)

    # Affichage du resultat
    for k, v in nor.items():
        # print(f"|{k}| = {v}")
        print(f"|{k + 1}| = {v}")
    return nor


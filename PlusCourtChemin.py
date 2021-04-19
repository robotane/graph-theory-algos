"""
Created on Dec 2020

@author: robotane
"""

from fonctionsDeBase import INF, print_access_tree

def bellman(graphe, s0):
    """
    Recherche du plus court chemin entre s0 et tous les sommets du graphe par
    l'algorithme de Bellman

    Parameters
    ----------
    graphe : list
        Matrice d'adjacence du graphe.
    s0 : int
        Sommet initial.

    Returns
    -------
    d : dict
        Dictionare contenant les distances entre s0 et les sommets du graphe
        comme valeurs.
    p : dict
        Dictionare contenant les predecesseurs des sommets du graphe comme
        valeurs.

    """
    # Initialisation
    E = list()
    comp = dict()
    d = dict()
    p = dict()

    d[s0] = 0
    p[s0] = s0

    long = len(graphe)
    for s in range(long):
        if s != s0:
            d[s] = INF
            p[s] = s0
        comp[s] = 0
        for t in range(long):
            if s == t:
                continue
            if graphe[t][s] < INF:
                comp[s] += 1
        if comp[s] == 0:
            E.append(s)

    # Traitement
    while E:
        s = E.pop()

        for t in range(long):
            if s == t:
                continue
            if graphe[t][s] < INF:
                val = INF if d[t] == INF else d[t] + graphe[t][s]
                # if d[t] == INF:
                #     val = INF
                # else:
                #     val = d[t] +  graphe[t][s]
                if val < d[s]:
                    d[s] = val
                    p[s] = t

        for t in range(long):
            if s == t:
                continue
            if graphe[s][t] < INF:
                comp[t] -= 1
                if comp[t] == 0:
                    E.append(t)

    # Affichage du resultat
    print_access_tree(graphe, p, d, s0)
    return d, p


def dijkstra(graphe, s0):
    """
    Recherche du plus court chemin entre s0 et tous les sommets du graphe par
    l'algorithme de Dijkstra

    Parameters
    ----------
    graphe : list
        Matrice d'adjacence du graphe.
    s0 : int
        Sommet initial.

    Returns
    -------
    d : dict
        Dictionare contenant les distances entre s0 et les sommets du graphe
        comme valeurs.
    p : dict
        Dictionare contenant les predecesseurs des sommets du graphe comme
        valeurs.

    """
    # Initialisation
    E = [s0]

    d = dict()
    p = dict()

    d[s0] = 0
    p[s0] = s0

    long = len(graphe)
    for s in range(long):
        if s != s0:
            d[s] = INF
            p[s] = s0
            E.append(s)

    # Traitement
    while E:
        s = min(E, key=lambda t: d[t])
        E.remove(s)

        for t in range(long):
            if s == t:
                continue
            if graphe[s][t] < INF:
                val = INF if d[s] == INF else d[s] + graphe[s][t]
                if val < d[t]:
                    d[t] = val
                    p[t] = s

    # Affichage du resultat
    print_access_tree(graphe, p, d, s0)
    return d, p


def floyd(graphe):
    """
    Recherche du plus court chemin entre tous les sommets du graphe par
    l'algorithme de Floyd

    Parameters
    ----------
    graphe : list
        Matrice d'adjacence du graphe.

    Returns
    -------
    d : list
        Liste contenant la liste des distances entre l'indice vu sommet du
        graphe et tous les autres sommets.
    p : list
        Liste contenant la ssite des predecesseurs  de l'indice vu sommet du
        graphe.

    """
    n = len(graphe)
    d = []
    p = []
    for i in range(n):
        ld = []
        lp = []
        for j in range(n):
            ld.append(graphe[i][j])
            lp.append(i)
        d.append(ld)
        p.append(lp)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                val = INF if (d[i][k] == INF or d[k][j] == INF) else d[i][k] + d[k][j]
                if val < d[i][j]:
                    d[i][j] = val
                    p[i][j] = p[k][j]

    # Affichage du resultat
    for s0 in range(n):
        print_access_tree(graphe, p[s0], d[s0], s0)
    return d, p

    
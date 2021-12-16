"""
Created on Dec 2020

@author: robotane
"""

from fonctionsDeBase import mat_2_adj_list, print_list


def ordre_prefixe(graphe):
    """
    Trie le graphe dans l'ordre prefixe

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.

    Returns
    -------
    list
        Liste des sommets dans l'ordre prefixe.

    """
    n = len(graphe)
    parcouru = []
    li = []
    for s in range(n):
        parcouru.append(False)

    def profondeur(s):
        parcouru[s] = True
        # print(s+1)
        li.append(s + 1)
        for t in graphe[s]:
            if not parcouru[t]:
                profondeur(t)

    for s in range(n):
        if not parcouru[s]:
            # print("main",s+1)
            profondeur(s)
    return li


def ordre_suffixe(graphe):
    """
    Trie le graphe dans l'ordre suffixe

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.

    Returns
    -------
    list
        Liste des sommets dans l'ordre suffixe.

    """
    n = len(graphe)
    parcouru = []
    li = []
    for s in range(n):
        parcouru.append(False)

    def profondeur(s):
        parcouru[s] = True
        for t in graphe[s]:
            if not parcouru[t]:
                profondeur(t)
        # print(s+1)
        li.append(s + 1)

    for s in range(n):
        if not parcouru[s]:
            # print("main",s+1)
            profondeur(s)
    return li


def acces(graphe, s0, t0):
    """
    Teste l'existance d'un chemin entre s0 et t0

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.
    s0 : int
        Sommet source.
    t0 : int
        Sommet final ou but.

    Returns
    -------
    bool
        True s'il existe un chemin entre s0 et t0.

    """
    n = len(graphe)
    parcouru = []
    for s in range(n):
        parcouru.append(False)

    def profondeur(s, t):
        parcouru[s] = True
        if s == t:
            return True

        for x in graphe[s]:
            if not parcouru[x]:
                return profondeur(x, t)
        return False

    return profondeur(s0, t0)


def but(graphe):
    """
    Determine le nombre de chemin de but s pour s quelconque dans le graphe

    Parameters
    ----------
    graphe : list
        Liste d'incidence du graphe.

    Returns
    -------
    list
        Liste ayant pour indices les sommets et pour valeurs le nombre de
        chemins qui menent a ces sommets.

    """
    n = len(graphe)
    parcouru = []
    bu = []
    for s in range(n):
        parcouru.append(False)
        bu.append(1)

    def profondeur(s):
        parcouru[s] = True
        for t in graphe[s]:
            if not parcouru[t]:
                profondeur(t)
            bu[s] += bu[t]

    for s in range(n):
        if not parcouru[s]:
            profondeur(s)
    return bu


def nb_connexe(graphe):
    """
    Determine le nombre de composantes connexe du graphe

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.

    Returns
    -------
    nb : int
        Le nombre de composantes connexe du graphe.

    """
    n = len(graphe)
    parcouru = []
    nb = 0
    for s in range(n):
        parcouru.append(False)

    def profondeur(s):
        parcouru[s] = True
        for t in range(n):
            if (graphe[s][t] == 1 or graphe[t][s] == 1) and not parcouru[t]:
                profondeur(t)

    for s in range(n):
        if not parcouru[s]:
            nb += 1
            profondeur(s)
    return nb


def tri_topo_prof(graphe):
    """
    Fais le tri topologique du graphe

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.

    Returns
    -------
    l : list
        Liste des sommets du graphe range selon le tri topologique.
    """
    n = len(graphe)
    parcouru = []
    li = []
    for s in range(n):
        parcouru.append(False)

    def profondeur(s):
        parcouru[s] = True
        for t in graphe[s]:
            if not parcouru[t]:
                profondeur(t)
        li.insert(0, s + 1)

    for s in range(n):
        if not parcouru[s]:
            profondeur(s)
    return li


def aller_retour(graphe):
    """
    Determine le nombre d'aller-retour du graphe

    Parameters
    ----------
    graphe : list
        Matrice d'adjacence du graphe.

    Returns
    -------
    nb : int
        Le nombre d'aller-retour du graphe.

    """
    n = len(graphe)
    parcouru = []
    nb = 0
    for s in range(n):
        parcouru.append(False)

    def profondeur(s):
        global nb
        parcouru[s] = True
        for t in range(n):
            if (graphe[s][t] == 1 and graphe[t][s] == 1) and not parcouru[t]:
                nb += 1

        for t in range(n):
            if graphe[s][t] == 1 and not parcouru[t]:
                profondeur(t)

    for s in range(n):
        if not parcouru[s]:
            profondeur(s)
    return nb


def a_triangle(graphe):
    """
    Determine le nombre d'aller-retour du graphe

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.

    Returns
    -------
    bool
        True si le graphe a un triangle.

    """
    n = len(graphe)
    parcouru = []

    for s in range(n):
        parcouru.append(False)

    def profondeur(s):
        parcouru[s] = True
        ret = False
        for t in range(n):
            if graphe[s][t] or graphe[t][s] and not parcouru[t]:
                for x in range(n):
                    if (graphe[x][t] or graphe[t][x] and not parcouru[x]) and (graphe[s][x] or graphe[x][s]):
                        print(s + 1, t + 1, x + 1)
                        return True
        for t in range(n):
            if graphe[s][t] and not parcouru[t]:
                ret = ret or profondeur(t)
        return ret

    trig = False
    for s in range(n):
        if not parcouru[s]:
            trig = profondeur(s)
            if trig:
                break
    return trig


def a_circuit(graphe):
    """
    Determine si le graphe a un circuit ou non

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.

    Returns
    -------
    bool
        False si le graphe est sans circuit, True sinon.

    """
    n = len(graphe)
    parcouru = []
    fini = []
    for s in range(n):
        parcouru.append(False)
        fini.append(False)

    def profondeur(s):
        parcouru[s] = True
        ps = False
        for t in graphe[s]:
            if not fini[t]:
                if not parcouru[t]:
                    ps = ps or profondeur(t)
                else:
                    return True

        fini[s] = True
        return ps

    circ = False
    for s in range(n):
        if not parcouru[s]:
            circ = circ or profondeur(s)
            if circ:
                break
    return circ


k = 0


def a_circuit_el(graphe):
    """
    Determine si le graphe a un circuit ou non

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.

    Returns
    -------
    bool
        False si le graphe est sans circuit, True sinon.

    """
    n = len(graphe)
    parcouru = []
    fini = []
    pos = {}
    k = 0
    for s in range(n):
        parcouru.append(False)
        fini.append(False)

    def profondeur(s):
        global k
        parcouru[s] = True
        ps = False
        k += 1
        pos[s] = k
        for t in graphe[s]:
            if not fini[t]:
                if not parcouru[t]:
                    ps = ps or profondeur(t)
                else:
                    if (pos[s] - pos[t] - 1) % 2:
                        return True

        fini[s] = True
        return ps

    circ = False
    for s in range(n):
        if not parcouru[s]:
            circ = profondeur(s)
            if circ:
                break
    return circ


k = 0
c = 0


def a_circuit_el_trace(graphe):
    """
    Determine si le graphe a un circuit ou non

    Parameters
    ----------
    graphe : list
        Liste d'adjacence du graphe.

    Returns
    -------
    bool
        False si le graphe est sans circuit, True sinon.
    """
    n = len(graphe)
    parcouru = []
    fini = []
    pos = {}
    global k
    k = 0
    for s in range(n):
        parcouru.append(False)
        fini.append(False)

    def profondeur(s):
        global k, c
        parcouru[s] = True
        k += 1
        pos[s] = k
        for t in graphe[s]:
            if not fini[t]:
                if not parcouru[t]:
                    print("->", " " * pos[s], f"{s + 1}=>p({t + 1})")
                    profondeur(t)
                else:
                    if (pos[s] - pos[t] - 1) % 2:
                        print("-v", " " * pos[s], f"{s + 1}-->{t + 1}")
                        c += 1
            else:
                print("-x", " " * pos[s], f"{s + 1}-x->p({t + 1})")
        fini[s] = True
        print("<-", " " * pos[s], f"<=p({s + 1})")

    for s in range(n):
        if not parcouru[s]:
            k = 0
            print()
            profondeur(s)

    # print()
    # print(fini)
    # print(parcouru)
    return c != 0


if __name__ == "__main__":
    mt = [[0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1],
          [1, 1, 0, 0]]

    mt2 = [[0, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 1, 0]]

    # test()
    ad = mat_2_adj_list(mt2)
    print_list(ad)
    print()
    print(a_circuit_el_trace(ad))
    print()
    print(a_triangle(mt2))
    print()
    print(but(ad))

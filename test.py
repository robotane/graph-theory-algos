#! /usr/bin/env python3
"""
Created on Dec 2020

@author: robotane
"""

from fonctionsDeBase import *
from ParcoursEnProfondeur import *
from PlusCourtChemin import *
from Tris import *


def test():
    def prompt():
        if input("Appuez sur Entrer pour continuer, 'q' pour quitter: ") == "q":
            print(r"Au revoir!!! \(-_-)/")
            exit(0)

    print("Matrice d'adjacence initiale:")
    pprint(mp)

    prompt()

    adj_list = mat_2_adj_list(mp)
    print("\nListe d'adjacence obtenue de la matrice:")
    print_list(adj_list)

    prompt()

    pred_list = adj_list_2_pred_list(adj_list)
    print("\nListe d'incidence obtenue de la liste d'adjacence:")
    print_list(pred_list)

    prompt()

    mat = list_2_mat(adj_list)
    print("\nMatrice d'adjacence obtenue de la liste d'adjacence:")
    # pprint(mat)
    print(mat == mp)

    # print("Liste d'incidence 3:")
    # adj_list2 = adj_list_2_pred_list(pred_list)
    # print(adj_list == adj_list2)

    print("\nLes normes:")
    norme(m)

    prompt()

    print("\nLe tri topologique:")
    print_tri(tri_topo(m))

    prompt()

    # Algorithmes de plus courts chemins
    print("\nAlgorithme de Bellman:")
    bellman(mb, 0)

    prompt()

    print("\nAlgorithme de Dijkstra:")
    dijkstra(mc, 0)

    prompt()

    print("\nAlgorithme de Floyd:")
    floyd(mc)

    prompt()

    # Algorithmes bases sur le tri en profondeur

    print("\nOrdre prefixe: ")
    print(ordre_prefixe(adj_list))

    prompt()

    print("\nOrdre suffixe")
    print(ordre_suffixe(adj_list))

    prompt()

    s, t = 1, 0
    print(f"\nIl existe un chemin entre {s + 1} et {t + 1}:", end=" ")
    print("Oui" if acces(adj_list, s, t) else "Non")

    prompt()

    print("\nNombre de chemins de but")
    print_tri(but(pred_list))

    prompt()

    print("\nNombre de composantes connexe:", end=" ")
    print(nb_connexe(mp))

    prompt()

    print(" \nTri topologique iteratif:")
    print_tri(tri_topo(m))

    prompt()

    print("\nTri topologique par un parcours en profondeur:")
    print_tri(tri_topo_prof(mat_2_adj_list(m)))

    prompt()

    print("\nLe graphe a un circuit:", end=" ")
    print("Oui" if a_circuit(adj_list) else "Non")


test()

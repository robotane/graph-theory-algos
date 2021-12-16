#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:18:05 2020

@author: robotane
"""

from pprint import pprint
from sys import exit
from math import inf

# Matrices d'ajacences de quelques graphes
m = [[0, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0],
     ]

mp = [[0, 0, 1, 0, 1, 1, 1, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      ]

mq = [[0, 0, 1, 0, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      ]

ma = [[0, 1, -2, inf, inf, inf],
      [inf, 0, inf, -2, inf, inf],
      [inf, 1, 0, 5, 4, inf],
      [inf, inf, inf, 0, inf, inf],
      [inf, inf, inf, inf, 0, -1],
      [inf, inf, inf, -5, inf, 0],
      ]

mb = [[0, 2, inf, 1, 0, inf],
      [inf, 0, -2, inf, -1, -1],
      [inf, inf, 0, inf, inf, inf],
      [inf, -1, inf, 0, -1, inf],
      [inf, inf, 0, inf, 0, 2],
      [inf, inf, -2, inf, inf, 0]
      ]

mc = [[0, 10, 3, inf, 6, inf],
      [0, 0, inf, inf, inf, inf],
      [inf, inf, 0, inf, 2, inf],
      [inf, inf, 1, 0, 3, inf],
      [inf, 0, inf, inf, 0, 1],
      [2, 1, inf, inf, inf, 0]
      ]

md = [[0, 5, inf, 2, 6, inf],
      [inf, 0, 0, inf, 0, inf],
      [inf, inf, 0, inf, inf, 0],
      [inf, 1, inf, 0, 0, inf],
      [inf, inf, 1, 0, 0, 4],
      [inf, 0, 2, inf, 0, 0]
      ]


def print_list(lis):
    """
    Affiche la liste d'adjacence d'une maniere plus naturelle

    Parameters
    ----------
    lis : list
        Liste d'adjacence ou de d'incidence.

    Returns
    -------
    None.

    """
    for i, li in enumerate(lis):
        print(f"{i + 1}", end=":")
        for s in li:
            print(f"-->{s + 1}", end="")
        print()


def print_tri(tri):
    for v in tri:
        # print(f"{v}", end=" ")
        print(f"{v:2}", end=" ")
    print()

    for k in range(len(tri)):
        print(f"{k + 1:2}", end=" ")
    print()


def mat_2_adj_list(mat):
    """
    Convertis une matrice d'adjacence en liste d'adjacence

    Parameters
    ----------
    mat : list
        La matrice d'adjacence est une liste de listes.

    Returns
    -------
    adj_list : list
        La liste d'adjacence qui est aussi une liste de listes.

    """
    adj_list = list()
    long = len(mat)
    for s in range(long):
        li = []
        for t in range(long):
            if mat[s][t]:
                li.append(t)
        adj_list.append(li)

    return adj_list


def adj_list_2_pred_list(adj_list):
    """
    Convertis une liste d'adjacence en liste d'incidence et vice-versa

    Parameters
    ----------
    adj_list : list
        Une liste d'adjacence (resp une liste d'incidence).

    Returns
    -------
    pred_list : list
        Une liste d'incidence (resp une liste d'adjacence.)

    """
    pred_list = []
    long = len(adj_list)

    for s in range(long):
        li = []
        for t in range(long):
            if s in adj_list[t]:
                li.append(t)
        pred_list.append(li)

    # print_list(pred_list)

    return pred_list


def list_2_mat(adj_list):
    """
    Convertis une liste d'adjacence en une matrice d'adjacence

    Parameters
    ----------
    adj_list : list
        Une liste d'adjacence.

    Returns
    -------
    mat : list
        Une matrice d'adjacence.

    """
    mat = []
    long = len(adj_list)

    for s in range(long):
        li = []
        for t in range(long):
            if t in adj_list[s]:
                li.append(1)
            else:
                li.append(0)
        mat.append(li)

    return mat


def print_access_tree(g, p, d, s0):
    """
    Affiche l'arbre d'accessibilite en connaissant la liste des distance et
    des predecesseurs

    Parameters
    ----------
    g : list
        Matrice d'adjacence du graphe.
    p : Union[list, dict]
        Liste des predecesseurs des sommets.
    d : Union[list, dict]
        Liste des distances entre les sommets du graphe et le sommet initial.
    s0 : int
        Sommet initial.

    Returns
    -------
    None.

    """
    long = len(p)
    print(f"Sommet source {s0 + 1}\n")
    if isinstance(p, dict):
        print(", ".join([f"p({k + 1})={v + 1}" for k, v in p.items()]))
    else:
        print(", ".join([f"p({k + 1})={v + 1}" for k, v in enumerate(p)]))

    print()
    for t in range(long):
        if t == s0:
            continue
        t0 = t
        print(f"d({s0 + 1},{t0 + 1})={d[t0]}")
        chem = f"{t0 + 1}"
        while t0 != s0:
            di = g[p[t0]][t0]
            chem = f"{p[t0] + 1}=[{di}]=>" + chem
            t0 = p[t0]
        print(chem)
        print()

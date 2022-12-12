# coding: utf-8

# stolen from google : https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwifrKq4yfP7AhUJTKQEHXa6BOQQFnoECDMQAQ&url=https%3A%2F%2Fisn.irem.univ-mrs.fr%2F2011-2012%2Fmedia%2Fresources%2Fdijkstra.py&usg=AOvVaw0f5FtOBSHGuVpMNI0-koVU

# La bibliothèque standard "heapq" fournit les fonctions de manipulation d'un
# tas: juste ce qu'il nous faut pour implémenter la file des sommets à traiter.

from heapq import *

# Implémentation de l'algorithme de Dijkstra en Python.
#
# Les arguments sont:
#  - s : le sommet source
#  - t : le sommet but
#  - voisins : fonction qui pour un sommet renvoie une liste de couples
#      (poids, sommet) pour chaque arête sortante
# Les sommets doivent être des objets "hachables" (nombres, chaînes de
# caractères, n-uplets...).
def dijkstra (s, t, g):
    M = set()
    d = {s: 0}
    p = {}
    suivants = [(0, s)] # tas de couples (d[x],x)

    while suivants != []:

        dx, x = heappop(suivants)
        if x in M:
            continue

        M.add(x)

        for w, y in g[x]:
            if y in M:
                continue
            dy = dx + w
            if y not in d or d[y] > dy:
                d[y] = dy
                heappush(suivants, (dy, y))
                p[y] = x

    path = [t]
    x = t
    while x != s:
        x = p[x]
        path.insert(0, x)

    return d[t], path, d


# Exemple d'utilisation avec un graphe représenté par une liste d'adjacence.
"""
graph = {
    "A": [ (27, "D"), (2, "G") ],
    "B": [ (1, "A") ],
    "C": [ (1, "B"), (2, "F"), (3, "G") ],
    "D": [ (4, "G"), (7, "H") ],
    "E": [ (5, "A"), (3, "B"), (2, "C") ],
    "F": [ (8, "H"), (1, "D") ],
    "G": [ (4, "F") ],
    "H": []
}
"""

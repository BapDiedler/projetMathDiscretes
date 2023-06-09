# -------------GRAPHES ORIENTES---------------- #
import time

ID = 0  # id d'un sommet


class Graphe:
    def __init__(self, val):
        # Entrée : un entier
        # Sortie : rien
        # Crée un graphe avec un sommet de valeur val. L'id du sommet est donnée automatiquement
        s = Sommet(val)
        self.sommets = [s]
        self.aretes = []

    def get_nb_sommets(self):
        return len(self.sommets)

    def get_nb_arete(self):
        return len(self.aretes)

    def get_sommet_num(self, i):
        # Entrée : l'id d'un sommet
        # Sortie : la valeur de ce sommet, un entier
        return self.sommets[i].get_valeur()

    def add_sommets(self, val):
        # Entrée : un entier, une valeur
        # Sortie : rien
        # Créer un sommet avec cette valeur. L'id du sommet est donnée automatiquement
        s = Sommet(val)
        self.sommets += [s]

    def add_arete(self, v, w):
        # Entrées : deux entiers, les Id des sommets
        # Sortie : rien
        # Ajoute l'arête orienté si elle n'est pas déjà présente.
        if [v, w] not in self.aretes:
            self.aretes += [[v, w]]

    def succ(self, v):
        # Entrée : l'id d'un sommet, un entier
        # Sortie : la liste des id des sommets, un tableau d'entiers
        succ = []
        for w in self.sommets:
            if [v, w.get_id()] in self.aretes and not (w.get_id() in succ):
                succ += [w.get_id()]
        return succ


class Sommet:
    def __init__(self, valeur):
        global ID
        self.valeur = valeur
        self.id = ID
        ID += 1

    def get_valeur(self):
        return self.valeur

    def get_id(self):
        return self.id


def DFS(G, v):
    p = [v]
    n = []
    while len(p) > 0:
        v = p.pop()
        # print(v)
        n.append(v)
        for w in G.succ(v):
            if not (w in p) and not (w in n):
                p.append(w)
    return n


def BFS(G, v):
    p = [v]
    n = []
    while len(p) > 0:
        v = p.pop(0)
        # print(v)
        n.append(v)
        for w in G.succ(v):
            if not (w in p) and not (w in n):
                p.append(w)
    return n




# création du graphe :
#       5
#       |
#       8
#       |
#       5
#     /  \
#    2   6

G = Graphe(5)
G.add_sommets(8)
G.add_sommets(5)
G.add_sommets(2)
G.add_sommets(6)
# arête = id
G.add_arete(0, 1)
G.add_arete(1, 2)
G.add_arete(2, 3)
G.add_arete(2, 4)
print("Nb sommets : ", G.get_nb_sommets())
print("Nb arrêtes : ", G.get_nb_arete())
print("Valeur sommet num 1 : ", G.get_sommet_num(1))

print("succ de 2 : ")
for w in G.succ(2):
    print(w)

print("===DFS====")
n = DFS(G, 0)
print("liste postfixe inversée : ", n)

ID=0

# ajout des sommets
G1 = Graphe(1)
for i in range(2, 7):
    G1.add_sommets(i)



# ajout des arêtes
for i in range(1, 4):
    G1.add_arete(0, i)

G1.add_arete(3, 2)
G1.add_arete(2, 5)
G1.add_arete(2, 4)
G1.add_arete(4, 2)
G1.add_arete(5, 2)
G1.add_arete(5, 4)

# ajout des boucles
for i in [0, 1, 3, 4, 5]:
    G1.add_arete(i, i)


n = DFS(G1, 0)
print("liste postfixe inversée : ", n)
n = BFS(G1, 0)
print("liste suffixe inversée : ", n)


"""
ID=0

# Création du graphe avec 1000 sommets
graphe = Graphe(0)
for i in range(1, 1000):
    graphe.add_sommets(i)
graphe.add_arete(0, 1)
graphe.add_arete(0, 2)
graphe.add_arete(1, 2)

# Exécution de l'algorithme DFS avec chronomètre
start_time = time.time()
for i in range(10000):
    DFS(graphe, 0)
end_time = time.time()

# Affichage du temps d'exécution
execution_time = (end_time - start_time)/10000
print("Temps d'exécution : %.10f secondes" % execution_time)
Temps d'exécution : 0.0003893661 secondes
"""

""" 
l'algorithme BFS n'est pas optimal car toutes les arêtes sont parcourut une fois même si le sommets est déjà colorié. 
De plus l'implémentation du graphe n'est optimal pour l'implémentation du BFS qui utilise le coloriage des sommets. Car dans 
la recherche des successeurs d'un sommet, tous les sommets du graphe vont être parcourut. or la méthode succ qui permet
d'obtenir les successeurs d'un sommet est appelée pour chaque sommet. On a donc un complexité qui est de O(N+P)
avec P le nombre d'arêtes et N le nombre de sommets.
"""

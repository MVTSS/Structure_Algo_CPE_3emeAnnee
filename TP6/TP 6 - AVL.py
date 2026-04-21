class Noeud:
    def __init__(self, annee: int):
        self.annee   = annee
        self.gauche  = None
        self.droite  = None
        self.hauteur = 1
        self.refs    = []  # références catalogue pour cette année
 
 
 
def hauteur(n) -> int:
    # TODO 1 — renvoyer 0 si n est None, sinon n.hauteur (1 ligne)
    # ???
 
def facteur_equilibre(n) -> int:
    # TODO 2 — renvoyer h(gauche) − h(droite), utiliser hauteur() (1 ligne)
    # ???
 
def maj_hauteur(n) -> None:
    n.hauteur = 1 + max(hauteur(n.gauche), hauteur(n.droite))
 
 
 
def rotation_droite(y):
    x  = y.gauche
    T2 = x.droite
    # TODO 3 — effectuer la rotation : 2 affectations
    # Indice : x devient la racine, y son fils droit, T2 le fils gauche de y
    # ???
    maj_hauteur(y)
    maj_hauteur(x)
    return x
 
def rotation_gauche(x):
    y  = x.droite
    T2 = y.gauche
    # TODO 4 — effectuer la rotation (symétrique du TODO 3)
    # ???
    maj_hauteur(x)
    maj_hauteur(y)
    return y
 
 
 
def inserer(noeud, annee: int, ref: str):
    if noeud is None:
        n = Noeud(annee) ; n.refs.append(ref) ; return n
    if annee == noeud.annee:
        noeud.refs.append(ref) ; return noeud
 
    # TODO 5 — descente récursive : gauche si annee < noeud.annee, droite sinon
    # ???
 
    maj_hauteur(noeud)
    f = facteur_equilibre(noeud)
 
    # TODO 6 — 4 cas de rééquilibrage : LL, RR, LR, RL
    # LL : f > 1 et annee < noeud.gauche.annee  →  rotation_droite
    # RR : f < -1 et annee > noeud.droite.annee →  rotation_gauche
    # LR : f > 1 et annee > noeud.gauche.annee  →  rotation_gauche(gauche) puis rotation_droite
    # RL : f < -1 et annee < noeud.droite.annee →  rotation_droite(droite) puis rotation_gauche
    # ???
 
    return noeud
 
 
 
def plage(noeud, a: int, b: int, res: list) -> None:
    if noeud is None: return
 
    # TODO 7 — parcours in-order élagué :
    #   descendre à gauche seulement si noeud.annee > a
    #   collecter noeud.refs seulement si a <= noeud.annee <= b
    #   descendre à droite seulement si noeud.annee < b
    # ???
 
 
 
if __name__ == "__main__":
    racine = None
    disques = [
        (1973, "9782010000000"), (1975, "9782210000000"),
        (1977, "9782210000137"), (1979, "9782010138233"),
        (1994, "9782210000274"), (2014, "9782010276466"),
    ]
    for annee, ref in disques:
        racine = inserer(racine, annee, ref)
 
    res = []
    plage(racine, 1970, 1980, res)
    print(res)  # attendu : les 4 disques des années 70

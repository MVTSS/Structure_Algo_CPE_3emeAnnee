M = 1009  # taille de la table (nombre premier)

class _Sentinel:
    """Marqueur de case supprimée (tombstone)."""
    def __repr__(self): return "DELETED"

DELETED = _Sentinel()

class Disque:
    """Représente un disque vinyle dans le catalogue."""

    def __init__(self, ref_cat: int, titre: str, annee: int, prix: float):
        self.ref_cat = ref_cat
        self.titre = titre
        self.annee = annee
        self.prix  = prix

    def __repr__(self) -> str:
        return f"Disque({self.ref_cat}, {self.titre!r}, {self.annee})"

class TableHachage:
    """
    Table de hachage à adressage ouvert par sondage linéaire.
    Clé   : référence catalogue (entier 13 chiffres)
    Valeur: objet Disque
    """

    def __init__(self, m: int = M):
        self.m     = m
        self.table = [None] * m   # None = vide, DELETED = supprimé
        self.n     = 0        # nombre d'éléments actifs



    def _h(self, ref_cat: int) -> int:
        """Renvoie h(ref_cat) = ref_cat mod m."""
        return ref_cat%self.m



    def inserer(self, disque: Disque) -> None:
        """
        Insère disque dans la table par sondage linéaire.
        Lève ValueError si la table est pleine.
        """
        if self.n >= self.m:
            raise ValueError("Table pleine")

        position = _h(disque.ref_cat)
        while self.table[position] != None or self.table[position] != DELETED:
            position += 1

        self.table[position] = disque



    def rechercher(self, ref_cat: int) -> Disque | None:
        """Renvoie le Disque d'ref_cat donné, ou None s'il est absent."""
        # TODO 3



    def supprimer(self, ref_cat: int) -> bool:
        """Supprime par marquage DELETED. Renvoie True si trouvé."""
        # TODO 4



    def facteur_charge(self) -> float:
        """Renvoie alpha = n / m."""
        # TODO 5

    def __len__(self) -> int:
        return self.n




if __name__ == "__main__":

    t = TableHachage()

    disques = [
        Disque(9782010000000, "The Dark Side of the Moon", 1973, 24.90),
        Disque(9782210000000, "Wish You Were Here", 1975, 22.50),
        Disque(9782210000137, "Animals", 1977, 19.90),
        Disque(9782010138233, "The Wall", 1979, 29.90),
        Disque(9782210000274, "The Division Bell", 1994, 21.90),
        Disque(9782010276466, "The Endless River", 2014, 29.90)
    ]

    for d in disques:
        t.inserer(d)

    # Test recherche
    print(t.rechercher(9782010000000))  # doit afficher le disque
    print(t.rechercher(9999999999999))  # doit afficher None

    # Test tombstone : supprimer A, puis chercher B (qui avait collisionné avec A)
    t.supprimer(9782010000000)
    print(t.rechercher(9782010000000))  # doit afficher None
    print(t.rechercher(9782010138233))  # doit encore fonctionner (cf. question 1.3) !

    print(f"alpha = {t.facteur_charge():.3f}")

class Noeud():
    def __init__(self, nombre):
        self.nombre = nombre
        self.pointeur = None
    def __repr__(self):
        return str(self.nombre)

class ListeChainee():
    def __init__(self, *args):
        self.tete = None
        self.size = 0
        precedent_val = None

        for val in args:
            new_val = Noeud(val)
            if self.tete == None:
                self.tete = new_val
            else:
                precedent_val.pointeur = new_val
            precedent_val = new_val
            self.size += 1

    def inserer(self, valeur, k):
        if k > self.size:
            print("Supérieur au max, pas d'insert possible")
        else:
            precedent = self.tete
            # Avoir le kieme-1 élément pour faire pointer le noeud actuel
            for i in range(k-2):
                precedent = precedent.pointeur

            new_noeud = Noeud(valeur)
            new_noeud.pointeur = precedent.pointeur
            precedent.pointeur = new_noeud

            self.size += 1

    def supprimer(self, k):
        if k > self.size:
            print("Supérieur au max, pas de suppression possible")
        else:
            precedent = self.tete
            # Avoir le kieme-1 élément pour faire pointer le noeud actuel
            for i in range(k-2):
                precedent = precedent.pointeur

            noeud_a_supp = precedent.pointeur
            precedent.pointeur = noeud_a_supp.pointeur
            del noeud_a_supp

            self.size -=1

    def rechercher(self, valeur):
        noeud = self.tete
        for i in range(self.size):
            if valeur == noeud.nombre:
                print(f"Trouvé à la position {i}")
                return noeud
            else:
                noeud = noeud.pointeur
        print(f"Valeur {valeur} non trouvé")

    def obtenir(self, k):
        if k > self.size:
            print("Supérieur au max, pas d'obtention possible")
        else:
            noeud = self.tete
            for i in range(k):
                noeud = noeud.pointeur
            print(f"Noeud à la position {k} : [{noeud.nombre}, {noeud.pointeur}]")
            return noeud

    def taille():
        print(f"Taille : {self.size}")
        return self.size

    def estVide():
        return self.size == 0







    def print_noeud(self):
        noeud = self.tete
        while noeud.pointeur != None:
            print(noeud.nombre, end=" ")
            noeud = noeud.pointeur
        print(noeud.nombre)

    def print_noeud_plus(self):
        noeud = self.tete
        while noeud.pointeur != None:
            print(f"Noeud : {noeud.nombre}, pointe vers {noeud.pointeur}")
            noeud = noeud.pointeur
        print(f"Noeud : {noeud.nombre}, pointe vers {noeud.pointeur}")




test = ListeChainee(1,2,4,5)
test.print_noeud()
#
# test.inserer(3,3)
# test.print_noeud()
#
# test.supprimer(3)
# test.print_noeud()
#
# test.rechercher(2)
#
# test.obtenir(3)

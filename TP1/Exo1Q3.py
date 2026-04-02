class Vagon():
    def __init__(self, nombre):
        self.nombre = nombre
        self.pointeur = None
    def __repr__(self):
        return str(self.nombre)

class Train():
    def __init__(self, *args):
        self.tete = None
        self.size = 0
        precedent_val = None

        for val in args:
            new_val = Vagon(val)
            if self.tete == None:
                self.tete = new_val
            else:
                precedent_val.pointeur = new_val
            precedent_val = new_val
            self.size += 1


    def monter(self, k):
        if k > self.size:
            print(f"Pas de vagon {k}")
        else:
            vagon = self.tete
            for i in range(k-1):
                vagon = vagon.pointeur
            while k <= self.size:
                if vagon.nombre < 4:
                    print(f"Membre ajouté au vagon {k}")
                    return 0
                else:
                    print(f"Pas assez de place dans le vagon {k}")
                    vagon = vagon.pointeur
                k+=1


    def descendre(self, k):
        if k > self.size:
            print(f"Pas de vagon {k}")
        else:
            vagon = self.tete
            for i in range(k-1):
                vagon = vagon.pointeur
            if vagon.nombre != 0:
                print(f"1 membre est descendu du vagon")
                vagon.nombre -= 1
            else:
                print("Le vagon est vide")


    def print_vagon(self):
        noeud = self.tete
        while noeud.pointeur != None:
            print(noeud.nombre, end=" ")
            noeud = noeud.pointeur
        print(noeud.nombre)

TRAIN = Train(4,4,4,0)
TRAIN.descendre(3)
TRAIN.print_vagon()
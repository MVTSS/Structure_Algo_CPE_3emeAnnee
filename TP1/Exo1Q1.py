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
    
    def __repr__(self):
        noeud = self.tete
        to_return = ""
        for _ in range(self.size):
            to_return += f"Val {_} : {noeud.nombre}\n"
            noeud = noeud.pointeur
        
        return to_return


test = ListeChainee(1,2,4,5)
print(repr(test))

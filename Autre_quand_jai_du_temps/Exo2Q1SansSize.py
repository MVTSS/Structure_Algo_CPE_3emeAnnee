class Noeud():
    def __init__(self, nombre):
        self.nombre = nombre
        self.pointeur = None
    def __repr__(self):
        return str(self.nombre)

class Pile():
    def __init__(self, *args):
        self.tete = None
        precedent_val = None

        for val in args:
            new_val = Noeud(val)
            if self.tete == None:
                self.tete = new_val
            else:
                precedent_val.pointeur = new_val
            precedent_val = new_val
        
        
    
    def push(self, val):
        old_tete = self.tete
        new_tete = Noeud(val)
        new_tete.pointeur = old_tete
        self.tete = new_tete
        pass

    def peek(self):
        if self.isEmpty() == False:
            # print(f"Peek : {self.tete.nombre}")
            return self.tete.nombre
        else:
            print("La pile est vide, 'Pop' skipped")

    def pop(self):
        if self.isEmpty() == False:
            old_tete = self.tete
            # print(f"Pop: {old_tete.nombre}")
            self.tete = old_tete.pointeur
            del old_tete
        else:
            print("La pile est vide, 'Pop' skipped")

    def size(self):
        if self.isEmpty() == False:
            cp = 0
            noeud = self.tete
            while noeud.pointeur != None:
                cp+=1
            # print(f"Size : {cp}")
            return cp

    def isEmpty(self):
        return self.tete == None


    def print_pile(self):
        if self.isEmpty() == False:
            noeud = self.tete
            while noeud.pointeur != None:
                print(noeud.nombre, end=" ")
                noeud = noeud.pointeur
            print(noeud.nombre)
        else:
            print("La pile est vide, 'Print' skipped")

    
    # def __repr__(self):
    #     noeud = self.tete
    #     to_return = ""
    #     for _ in range(self.size):
    #         to_return += f"Val {_} : {noeud.nombre}\n"
    #         noeud = noeud.pointeur
        
    #     return to_return


test = Pile()
test.push(2)
test.print_pile()
test.pop()
test.print_pile()
test.isEmpty()

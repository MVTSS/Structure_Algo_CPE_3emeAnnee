class Noeud():
    def __init__(self, cara):
        self.cara = cara
        self.pointeur = None
    def __repr__(self):
        return str(self.cara)

class Pile():
    def __init__(self, *args):
        self.tete = None
        precedent_val = None
        self.size = 0

        for val in args:
            new_val = Noeud(val)
            if self.tete == None:
                self.tete = new_val
            else:
                precedent_val.pointeur = new_val
            precedent_val = new_val
            self.size+=1
        
        
    
    def push(self, val):
        old_tete = self.tete
        new_tete = Noeud(val)
        new_tete.pointeur = old_tete
        self.tete = new_tete
        self.size+=1
        pass

    def peek(self):
        if not self.isEmpty():
            # print(f"Peek : {self.tete.nombre}")
            return self.tete.cara
        else:
            # print("La pile est vide, 'Peek' skipped")
            return None

    def pop(self):
        if not self.isEmpty():
            old_tete = self.tete
            to_return = old_tete.cara
            # print(f"Pop: {old_tete.cara}")
            self.tete = old_tete.pointeur
            del old_tete
            self.size-=1
            return to_return
        else:
            # print("La pile est vide, 'Pop' skipped")
            return None

    def size_pile(self):
        # print(f"Size : {self.size}")
        return self.size

    def isEmpty(self):
        return self.tete == None


    def print_pile(self):
        if not self.isEmpty():
            noeud = self.tete
            while noeud.pointeur != None:
                print(noeud.cara, end=" ")
                noeud = noeud.pointeur
            print(noeud.cara)
        else:
            print("La pile est vide, 'Print' skipped")

    # def __repr__(self):
    #     noeud = self.tete
    #     to_return = ""
    #     for _ in range(self.size):
    #         to_return += f"Val {_} : {noeud.cara}\n"
    #         noeud = noeud.pointeur
        
    #     return to_return



def check_parenthese(string):
    every_par = list(string)
    cp = 0
    # if len(every_par)%2 !=0:
    #     return False
    
    fermante = {'(':')', '{':'}', '<':'>', '[':']'}
    pile = Pile()
    for parenthese in every_par:
        if parenthese in fermante or parenthese in fermante.values():
            cp +=1
        if parenthese in fermante:
            pile.push(parenthese)
            continue
        if pile.peek() != None and fermante[pile.peek()] == parenthese:
            pile.pop()
            cp-=2
    
    if pile.isEmpty() and cp == 0:
        return True

    return False

correct = "(123)"
res1 = check_parenthese(correct)
print("Res 1 : ", res1)
incorrect = ")"
res2 = check_parenthese(incorrect)
print("Res 2 : ", res2)
incorrect2 = "("
res3 = check_parenthese(incorrect2)
print("Res 3 : ", res3)
incorrect3 = ")("
res4 = check_parenthese(incorrect3)
print("Res 4 : ", res4)



correct2 = "({})"
final = check_parenthese(correct2)
print("Final : ", final)
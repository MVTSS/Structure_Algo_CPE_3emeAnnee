import time

#==========================================================
#==========================================================
# EXO 1                                                   =
#==========================================================
#Complexité O(n)
def decroissant(n):
    if n < 1:
        print(n)
        return 1
    print(n)
    return decroissant(n-1)

#Complexité O(n)
def croissant(n, keep=0):
    if n == keep:
        print(keep)
        return 0
    print(keep)
    return croissant(n, keep+1)
#==========================================================
# Lancement                                               =
#==========================================================
#croissant(10)
#decroissant(10)

#==========================================================
#==========================================================
# EXO 2                                                   =
#==========================================================
#Complexité O(2^n)
def fibonacci1(n):
    if n < 2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)

def get_fibo1_time(n):
    start = time.time()
    print(fibonacci1(n-1))
    end = time.time()
    print("Temps passé pour n = ",n,": ", end-start,"sec")
    return 0
#==========================================================
#Complexité O(n)
def fibonacci2(n, F):
    if F[n] != -1:
        return F[n]
    if n < 2:
        F[n] = 1
        return 1
    r = fibonacci2(n-1, F) + fibonacci2(n-2, F)
    F[n] = r
    return r

def get_fibo2_time(n):
    tab = [-1]*(n+1)
    start = time.time()
    print(fibonacci2(n-1, tab))
    end = time.time()
    print("Temps passé pour n = ",n,": ", end-start,"sec")
    return 0

#==========================================================
#Complexité ??
def fibonacci3(n, a=1, b=1, keep=0):
    pass

def get_fibo3_time(n):
    tab = [-1]*(n+1)
    start = time.time()
    print(fibonacci2(n-1, tab))
    end = time.time()
    print("Temps passé pour n = ",n,": ", end-start,"sec")
    return 0

#==========================================================
# Lancement                                               =
#==========================================================
#get_fibo1_time(10)
#get_fibo1_time(20)
#get_fibo1_time(30)
#get_fibo1_time(40)

#get_fibo2_time(10)
#get_fibo2_time(20)
#get_fibo2_time(30)
#get_fibo2_time(40)

#get_fibo3_time(10)
#get_fibo3_time(20)
#get_fibo3_time(30)
#get_fibo3_time(40)

#==========================================================
#==========================================================
# EXO 3                                                   =
#==========================================================
#Complexité ??
#Exercice "peu important" d'après le prof, pour plus tard
def maxliste(liste):
    pass
#==========================================================
# Lancement                                               =
#==========================================================
#exemple_liste = [1,2,3,4,234,4,5,6,7]
#maxliste(exemple_liste)

#==========================================================
#==========================================================
# EXO 4                                                   =
#==========================================================
#Complexité ??
def hanoi(n, start,mid,end):
    if n < 0: return
    hanoi(n-1, start, end, mid)
    print("Déplacement de ",start," à ", end)
    hanoi(n-1, mid,start,end)
    return 1

#==========================================================
# Lancement                                               =
#==========================================================
hanoi(3, "pillier 1", "pillier 2", "pillier 3")

#==========================================================
#==========================================================
# EXO 5                                                   =
#==========================================================
#Complexité ??
def dicho(n, start,mid,end):
    pass

#==========================================================
# Lancement                                               =
#==========================================================
#


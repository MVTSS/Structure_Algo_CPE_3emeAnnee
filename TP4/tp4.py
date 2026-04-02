# Exo 3
"""
Si on tri les 2 premiers tier, il n'y a que le dernier tier qui n'est pas trier.
De ce fait, le premier tier contient les plus petit chiffres des 2 tier, et le 2eme tier les plus grands.

Avec le 2., en triant 

"""

tab = [2,3,5,6,5,7]

def Tri_par_tier(tab):
    n = len(tab)
    if n == 0:
        return []
    if n == 1:
        return tab
    if n == 2:
        return tab if tab[0] < tab[1] else [tab[1], tab[0]]

    tier2 = (2*n)//3
    tier1 = n//3
    # tab[:tier2] = Tri_par_tier(tab[:tier2])
    # tab[tier1:] = Tri_par_tier(tab[tier1:])
    # tab[:tier2] = Tri_par_tier(tab[:tier2])

    premier_tiers  = Tri_par_tier(tab[:tier2])
    tab[:tier2] = premier_tiers

    dernier_tiers  = Tri_par_tier(tab[tier1:])
    tab[tier1:] = dernier_tiers

    premier_tiers2 = Tri_par_tier(tab[:tier2])
    tab[:tier2] = premier_tiers2

L = Tri_par_tier(tab)
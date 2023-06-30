import math
import numpy as np
from LesPremieresValeurs import*
from Apprentissage import*

def Apprentissage_avec_epoque(e, c, s):

    def variance():
        conteneur = np.zeros(50)
        for i in range(50):
            conteneur[i] = liste_X_n[i]
        return np.var(conteneur)
    
    def epoque_calc(e, c, s, Prototype, poid_2, poid_3, sortie_desire, liste_sortie_reseau):

        somme = 0

        for j in range(50):

            Reseau = algo_descente_gradient(e, c, s, Prototype, poid_2, poid_3, sortie_desire)
            poid_2 = Reseau[0]
            poid_3 = Reseau[1]
            Prototype = prototype(j + 1, e)
            sortie_desire = np.array([liste_X_n[j + 3]])
            liste_sortie_reseau[j] = Reseau[2]
            somme += math.pow( liste_X_n[j] - liste_sortie_reseau[j], 2)
        
        NMSE = (1 / (N * variance())) * somme

        return poid_2, poid_3, NMSE, liste_sortie_reseau
    

    poid_2 = init_poid(c, e)
    poid_3 = init_poid_2(s, c)

    print("\n",poid_2)
    print("\n",poid_3)

    Prototype = prototype(0, e)
    sortie_desire = np.array([liste_X_n[2]])
    liste_sortie_reseau = np.zeros(50)
    NMSE = 0
    N = 50

    def epoque(e, c, s, Prototype, poid_2, poid_3, sortie_desire, liste_sortie_reseau):
        NMSE_tab = np.zeros(9)
        liste = np.zeros((9, 50))
        liste_poid_2 = np.zeros(((9, c, e)))
        liste_poid_3 = np.zeros(((9, s, c)))
        for i in range(9):
            Epoque_calc = epoque_calc(e, c, s, Prototype, poid_2, poid_3, sortie_desire, liste_sortie_reseau)
            poid_2 = Epoque_calc[0]
            poid_3 = Epoque_calc[1]
            Prototype = prototype( (50 * (i+1)) + 1 , e)
            sortie_desire = np.array([liste_X_n[(50 * (i+1)) + 3]])
            NMSE_tab[i] = Epoque_calc[2]
            for j in range(50):
                liste[i, j] = Epoque_calc[3][j]
            
            for a in range(c):
                for b in range(e):
                    liste_poid_2[i, a, b] = poid_2[a, b]
            
            for a in range(s):
                for b in range(c):
                    liste_poid_3[i, a, b] = poid_3[a, b]

        return NMSE_tab, liste, liste_poid_2, liste_poid_3
    
    u_1 = epoque(e, c, s, Prototype, poid_2, poid_3, sortie_desire, liste_sortie_reseau)[0]
    u_2 = epoque(e, c, s, Prototype, poid_2, poid_3, sortie_desire, liste_sortie_reseau)[2]
    u_3 = epoque(e, c, s, Prototype, poid_2, poid_3, sortie_desire, liste_sortie_reseau)[3]

    #min NMSE
    
    return u_1, u_2, u_3

nombreUniteEntre = 2
nombreUniteCache = 2

a = Apprentissage_avec_epoque(nombreUniteEntre,nombreUniteCache,1)[0]
b = Apprentissage_avec_epoque(nombreUniteEntre,nombreUniteCache,1)[1]
c = Apprentissage_avec_epoque(nombreUniteEntre,nombreUniteCache,1)[2]

def courbe_nmse():
    X_nmse = np.arange(0, 9, dtype=int)
    Y_nmse = a

    plt.plot(X_nmse,Y_nmse)
    plt.show()

def min_loc():
    for i in range(9):
        if a[i] < a[i+1]:
            return i
            break

indice_min_loc_nmse = min_loc()

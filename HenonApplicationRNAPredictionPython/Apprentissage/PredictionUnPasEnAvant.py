from LesPremieresValeurs import*
import numpy as np
import math
from Apprentissage_2 import*

poid_1_2 = b[indice_min_loc_nmse]
poid_2_3 = c[indice_min_loc_nmse]
#g(somme_j(W_ij^m * V_j^m-1))

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def identite(x):
    return x

def predictionUnPasEnAvant():
    prototype = np.zeros((501, nombreUniteEntre))
    valeur_predite = np.zeros(500)
    v_cacher = np.zeros(nombreUniteCache)
    #creation prototype:
    for j in range(501):
        for i in range(nombreUniteEntre):
            prototype[j, i] = liste_X_n[j + i] 
    #prediction
    def val_couche_cacher(nbr):
        val_cacher = np.zeros(nombreUniteCache)

        for j in range(nombreUniteCache):
            for i in range(nombreUniteEntre):
                val_cacher[j] = poid_1_2[j, i] * prototype[nbr, i]
                v_cacher[j] = sigmoide(val_cacher[j])
        
        return v_cacher
    
    def val_couche_sortie(nbr):
        v_s_1 = 0
        for i in range(nombreUniteCache):
            v_s_1 += poid_2_3[0, i] * val_couche_cacher(nbr)[i]
        return identite(v_s_1)

    for i in range(500):
        valeur_predite[i] = val_couche_sortie(i)
    
    return  valeur_predite, prototype
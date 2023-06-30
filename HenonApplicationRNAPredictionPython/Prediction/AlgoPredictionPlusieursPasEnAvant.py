from LesPremieresValeurs import*
import numpy as np
import math

W11=0.32754594
W12=-1.18991807
W21=3.79660811
W22=1.76143971

#

Wd11=-0.68517821
Wd12=1.55664188

poid_1_2=np.array([[W11, W12], [W21, W22]])
poid_2_3=np.array([[Wd11, Wd12]])

nombreUniteCache=2
nombreUniteEntre=2

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def identite(x):
    return x

def prediction(tab):
    v_cacher = np.zeros(nombreUniteCache)
    #prediction
    def val_couche_cacher():
        val_cacher = np.zeros(nombreUniteCache)

        for j in range(nombreUniteCache):
            for i in range(nombreUniteEntre):
                val_cacher[j] = poid_1_2[j, i] * tab[i]
                v_cacher[j] = sigmoide(val_cacher[j])
        
        return v_cacher
    
    def val_couche_sortie():
        v_s_1 = 0
        for i in range(2):
            v_s_1 += poid_2_3[0, i] * val_couche_cacher()[i]
        return identite(v_s_1)
    
    predit = val_couche_sortie()

    return predit

""" la fonction suivante presente 2 paramètre "nbr" et "debut"
dont "nbr" represente le nombre de pas d' apprentissage en avant pour 
la prediction. Et "debut" represente l' indice du premier prototype
ou l' on veut commencer. """

def iteration(nbr, debut):
    val = np.empty(nbr)
    prototype = np.empty((nbr, nombreUniteEntre))
    tabPrototypes = np.zeros(nombreUniteEntre)

    for i in range(nombreUniteEntre):
        tabPrototypes[i] = liste_X_n[i + debut]
    
    predit = 0
    for i in range(nbr):
        predit = prediction(tabPrototypes)
        prototype[i] = tabPrototypes
        #modification de tabPrototypes
        tabPrototypes = np.append(predit, tabPrototypes)
        tabPrototypes = np.delete(tabPrototypes, nombreUniteEntre)
        
        val[i] = predit

    return val, prototype
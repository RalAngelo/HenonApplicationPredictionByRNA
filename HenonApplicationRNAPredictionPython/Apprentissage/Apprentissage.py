import math
import random
import numpy as np
from LesPremieresValeurs import*

#Etape 1: Initialisation des poids
def aleatoire(min, max, entier):
    if(entier == 1):
        return math.floor(random.random() * (max - min + 1) + min)
    if(entier == 0):
        return random.random() * (max - min + 1) + min
    else:
        print("erreur")

def init_poid(de, ar):
    w = np.zeros((de, ar))
    for i in range(de):
        for j in range(ar):
            w[i, j] = aleatoire(-2, 2, 0)
    return w

def init_poid_2(de, ar):
    w = np.zeros((de, ar))
    for i in range(de):
        for j in range(ar):
            w[i, j] = aleatoire(-2, 2, 0)
    return w

#Etape 2: choix prototype
def prototype(d, e):
    boritra = np.zeros(e)
    for i in range(e):
        boritra[i] = liste_X_n[d+i] #le tableau liste_X_n contient les 500 premiere valeurs de Xn 
    return boritra

def algo_descente_gradient(nbr_unites_entrer, nbr_unites_cacher, nbr_unites_sortie, Prototype, poid_2, poid_3, sortie_desire):

    neta = 0.47
    #Etape 3: Propager le signal vers l avant a travers le reseau
    def sigmoide(x):
        return 1 / (1 + math.exp(-x))
        
    def identite(x):
        return x

    def V_entrer(nbr):
        v = np.zeros(nbr)
        for a in range(nbr):
            v[a] = Prototype[a]
        return v
        
    def V_cacher(nbr, h):
        v = np.zeros(nbr)
        s = np.zeros(nbr)
        for i in range(nbr):
            somme = 0
            for j in range(nbr_unites_entrer):
                somme += (poid_2[i, j] * V_entrer(nbr_unites_entrer)[j])
            v[i] = sigmoide(somme)
            s[i] = somme
        if h == 1:
            return v
        if h == 0:
            return s
        
    def V_sortie(nbr):
        v = np.zeros(nbr)
        for i in range(nbr):
            somme = 0
            for j in range(nbr_unites_cacher):
                somme += (poid_3[i, j] * V_cacher(nbr_unites_cacher, 1)[j])
            v[i] = identite(somme)
        return v
        
    #Etape 4:  Calculer les deltas pour la couche de sortie
    def derive_sigmoide(x):
        return math.exp(-x) / math.pow((1 + math.exp(-x)), 2)

    def delta_sortie(nbr):
        delta = np.zeros(nbr)
        for i in range(nbr):
            somme = 0
            for j in range(nbr_unites_cacher):
                somme += (poid_3[i, j] * V_cacher(nbr_unites_cacher, 1)[j])
            delta[i] = derive_sigmoide(somme) * (sortie_desire[i] - V_sortie(nbr_unites_sortie)[i])
        return delta
        
    #Etape 5: Calculer les delta pour les couches precedentes en propageant les erreurs vers l arriere
    def delta_cacher(nbr):
        delta = np.zeros(nbr)
        for i in range(nbr):
            delta[i] = derive_sigmoide(V_cacher(nbr_unites_cacher, 0)[i]) * poid_3[0, i] * delta_sortie(nbr_unites_sortie)[0]
        return delta
        
    #Etape 6: Nouvelles valeurs des poids
    def new_poid_2():
        delta_poid_2 = np.zeros((nbr_unites_cacher, nbr_unites_entrer))
        New_poid_2 = np.zeros((nbr_unites_cacher, nbr_unites_entrer))
        for i in range(nbr_unites_cacher):
            for j in range(nbr_unites_entrer):
                delta_poid_2[i, j] = neta * delta_cacher(nbr_unites_cacher)[i] * V_entrer(nbr_unites_entrer)[j]
                New_poid_2[i, j] = poid_2[i, j] + delta_poid_2[i, j]
        return New_poid_2
        
    def new_poid_3():
        delta_poid_3 = np.zeros((nbr_unites_sortie, nbr_unites_cacher))
        New_poid_3 = np.zeros((nbr_unites_sortie, nbr_unites_cacher))
        for i in range(nbr_unites_sortie):
            for j in range(nbr_unites_cacher):
                delta_poid_3[i, j] = neta * delta_sortie(nbr_unites_sortie)[i] * V_cacher(nbr_unites_cacher, 1)[j]
                New_poid_3[i, j] = poid_3[i, j] + delta_poid_3[i, j]
        return New_poid_3
        
    nouvelle_poid_2 = new_poid_2()
    nouvelle_poid_3 = new_poid_3()

    return nouvelle_poid_2, nouvelle_poid_3, V_sortie(nbr_unites_sortie)      
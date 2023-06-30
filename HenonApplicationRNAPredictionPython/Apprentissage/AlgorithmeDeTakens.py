#Etape 1:
from LesPremieresValeurs import*
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

#Etape 2:
def x_bar(i, n, tau = 1):
    return np.array([liste_X_n[i + k * tau] for k in range(n)])

#Etape 3:
def theta(taille):
    Theta = np.zeros((taille, taille))
    for i in range(taille):
        Theta[i, i] = x_bar(0, taille)[i] * np.transpose(x_bar(0, taille)[i])    
    return Theta

#Etape 4:
def val_propre(matrice):
    valeur_propre = LA.eigvals(matrice)
    return valeur_propre

def tri_decroissant(liste_val_propre):
    tri = np.sort(liste_val_propre)[::-1]
    return tri

#etape 5:   
def erreur_approximation_moyenne(liste):
    lambda_l = tri_decroissant(liste)
    epsilon_lsquare = lambda_l[1 : 20]
    epsilon_l = np.sqrt(epsilon_lsquare)
    return epsilon_l

#etape 6:
def courbe_epsilon():
    X_epsilon = np.arange(0, 19, dtype=int)
    Y_epsilon = erreur_approximation_moyenne(val_propre(theta(20)))

    plt.plot(X_epsilon,Y_epsilon)
    plt.show()

#etape 7:
def indicePremierPlateau():
    for i in range(20):
        a = erreur_approximation_moyenne(val_propre(theta(20)))[i]
        b = erreur_approximation_moyenne(val_propre(theta(20)))[i + 1]
        c = a-b
        if c <= 0.01:
            return i
            break
import matplotlib.pyplot as plt
from AlgoPredictionPlusieursPasEnAvant import*
from LesPremieresValeurs import*

x = np.arange(0, 3, dtype=int)
def y():
    val_y = np.empty(3)
    for j in range(3):
        val_y[j] = liste_X_n[15 + j]
    return val_y
def z():
    val_z = np.empty(3)
    for j in range(3):
        val_z[j] = iteration(3, 15)[0][j-1]
    return val_z

y = y()
z = z()
def courbe_pred_3():        
    plt.plot(x, y, label = r'Valeurs à prédire')
    plt.plot(x, z, label = r'Valeurs donnée par le réseaux')
    plt.title('prédiction à trois pas en avant')
    plt.legend(loc=0)
    plt.show()
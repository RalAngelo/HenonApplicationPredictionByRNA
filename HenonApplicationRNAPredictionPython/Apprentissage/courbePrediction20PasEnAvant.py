import matplotlib.pyplot as plt
from AlgoPredictionPlusieursPasEnAvant import*
from LesPremieresValeurs import*

x = np.arange(0, 20, dtype=int)
def y():
    val_y = np.empty(20)
    for j in range(20):
        val_y[j] = liste_X_n[1 + j]
    return val_y
def z():
    val_z = np.empty(20)
    for j in range(20):
        val_z[j] = iteration(20, 1)[0][j-1]
    return val_z

y = y()
z = z()
def courbe_pred_20():        
    plt.plot(x, y, label = r'Valeurs à prédire')
    plt.plot(x, z, label = r'Valeurs donnée par le réseaux')
    plt.title('prédiction à vingt pas en avant')
    plt.legend(loc=0)
    plt.show()
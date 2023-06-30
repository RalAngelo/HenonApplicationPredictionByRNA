import numpy as np 
import matplotlib.pyplot as plt 

def henon_attractor(x, y, a=1.4, b=0.3):
	
	x_next = 1 - a * x ** 2 + y
	y_next = b * x
	return x_next, y_next
	
# nombre d' iteration et initialisation de l' "array"
steps = 699
X = np.zeros(steps + 1)
Y = np.zeros(steps + 1)

# point de depart
X[0], Y[0] = 0, 0

# ajout des points dans l' "array"
for i in range(steps):
	x_next, y_next = henon_attractor(X[i], Y[i])
	X[i+1] = x_next
	Y[i+1] = y_next

liste_X_n = X
liste_Y_n = Y
	
# figure
def courbe():
	plt.plot(X, Y, '^', alpha = 0.8, markersize=0.8)
	plt.title('courbe de Yn(Xn)')
	plt.show()
	plt.close()

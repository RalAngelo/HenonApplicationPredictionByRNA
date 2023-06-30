from tkinter import * 
import tkinter as tk
import numpy as np
from AlgoPredictionPlusieursPasEnAvant import * 
from LesPremieresValeurs import*

class App_Table_10(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.geometry("1142x345")
        self.resizable(width=0, height=0)
        self.title("Tableau de la prédiction à trois pas en avant")

        title = ['N°', 'Prototypes', 'Valeurs attendues', 'Valeurs données par le réseau']

        lst = np.empty((11, 4), dtype=object)
        for i in range(11):
            for j in range(4):
                if j==0 :
                    if i>0:
                        lst[i,j] = i 
                    if i==0:
                        lst[i,j] = title[0] 
        
                if j==1:
                    if i>0:
                        lst[i,j] = " \"{0}\"; \"{1}\" ".format(iteration(10, 1)[1][i-1, 0], iteration(10, 1)[1][i-1, 1])
                    if i==0:
                        lst[i,j] = title[1]

                if j==2:
                    if i>0:
                        lst[i,j] = liste_X_n[3 + (i-1)]
                    if i==0:
                        lst[i,j] = title[2]

                if j==3:
                    if i>0:
                        lst[i,j] = iteration(10, 1)[0][i-1]
                    if i==0:
                        lst[i,j] = title[3]

        total_rows = len(lst)
        total_columns = len(lst[0])

        #tableau
        for i in range(total_rows):
            for j in range(total_columns):
                if i>=0 and j==0:
                    if i==0:
                        self.e = tk.Entry(self, width=3, fg='blue', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                    else:
                        self.e = tk.Entry(self, width=3, fg='black', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                if i>=0 and j==1:
                    if i==0:
                        self.e = tk.Entry(self, width=43, fg='blue', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                    else:
                        self.e = tk.Entry(self, width=43, fg='black', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                if i>=0 and j==2:
                    if i==0:
                        self.e = tk.Entry(self, width=21, fg='blue', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                    else:
                        self.e = tk.Entry(self, width=21, fg='black', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                if i>=0 and j==3:
                    if i==0:
                        self.e = tk.Entry(self, width=26, fg='blue', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                    else:
                        self.e = tk.Entry(self, width=26, fg='black', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
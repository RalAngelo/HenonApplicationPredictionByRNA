from tkinter import * 
import tkinter as tk
from AlgorithmeDeTakens import*

class App_architect(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Algorithme de Takens")
        self.geometry("700x700")
        self.resizable(width=0, height=0)
        self.option_add("*header.font", "helvetica 18 bold")
        self.option_add("*agrandi.font", "helvetica 100 bold")
        self.create_label(name="header", text="Algorithme de Takens: ")


        label_Theta = tk.LabelFrame(self, text = "La matrice de covariance")
        label_Val_Propre = tk.LabelFrame(self, text="Les Valeurs Propres")
        label_indiceDuPremierPlateau = tk.LabelFrame(self, text="Indice du premier plateau")

        label_Theta.place(x=25, y=40, width = 650, height = 350)
        label_Val_Propre.place(x=25, y=435, width=320, height=200)
        label_indiceDuPremierPlateau.place(x=355, y=435, width=320, height=200)

        v=Scrollbar(label_Theta, orient='vertical')
        v.pack(side=RIGHT, fill='y')

        T = Text(label_Theta, height = 320, width = 630, yscrollcommand=v.set)
        v.config(command=T.yview)
        T.pack()

        T2 = Text(label_Val_Propre, height=170, width=300)
        T2.pack()        
        
        def AfficheTheta():
            Theta = theta(20)
            fact = str(Theta)
            T.insert(END, fact)

        def AfficheValPropre():
            ValPropre = tri_decroissant((val_propre(theta(20))))
            fact = str(ValPropre)
            T2.insert(END, fact)

        indice = indicePremierPlateau()
        def afficheIndice():
            label = tk.Label(label_indiceDuPremierPlateau, name="agrandi", text=str(indice))
            label.pack()
            courbe_epsilon()      

        btn_theta = tk.Button(self, text = "Afficher la matrice de covariance", command=AfficheTheta)
        btn_theta.place(x = 25, y = 392)
        btn_valPropre = tk.Button(self, text="Afficher les valeurs propres", command=AfficheValPropre)
        btn_valPropre.place(x=25, y=636)
        btn_indiceDuPremierPlateau = tk.Button(self, text="Afficher l'indice du premier plateau et la courbe", command=afficheIndice)
        btn_indiceDuPremierPlateau.place(x=355, y=636)

    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)
    
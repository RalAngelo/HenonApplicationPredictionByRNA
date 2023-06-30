from tkinter import * 
import tkinter as tk
import numpy as np
from Apprentissage_2 import*

class App231(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Apprentissage")
        self.geometry("700x700")
        self.option_add("*header.font", "helvetica 18 bold")
        self.create_label(name="header", text="Apprentissage: ")

        label231 = tk.LabelFrame(self, text="Information sur l'architecture")
        label231.place(x=50, y=50, width=600, height=400)

        labelPoid = tk.LabelFrame(self, text="Les poids pour la NMSE minimale")
        labelPoid.place(x=50, y=460, width=400, height=200)

        v=Scrollbar(label231, orient='vertical')
        v.pack(side=RIGHT, fill='y')

        T = Text(label231, width=590, height=490, yscrollcommand=v.set)
        v.config(command=T.yview)
        T.pack()

        v2=Scrollbar(labelPoid, orient='vertical')
        v2.pack(side=RIGHT, fill='y')

        T2 = Text(labelPoid, width=390, height=190, yscrollcommand=v2.set)
        v2.config(command=T2.yview)
        T2.pack()

        def affichage():
            for i in range(9):
                fact1 = ("""************ """+"""ÉPOQUE"""+str(i+1)+ """ ************""" + """\n""" +
                """ NMSE de l'époque """ + str(i+1) + """: """+ """\"""" + str(a[i])+ """\"""" + 
                """\n""" 
                + """les poids obtenus entre la couche d' entrée et la couche cachée: """ +
                """\n"""
                )

                affiche_poid_2 = np.zeros((nombreUniteCache, nombreUniteEntre))
                affiche_poid_3 = np.zeros((1, nombreUniteCache))
                for x in range(nombreUniteCache):
                    for y in range(nombreUniteEntre):
                        affiche_poid_2[x, y] = b[i, x, y]
                for x in range(1):
                    for y in range(nombreUniteCache):
                        affiche_poid_3[x, y] = c[i, x, y]
                
                fact2 = (str(affiche_poid_2) + """\n"""
                + """les poids obtenus entre la couche cachée et la couche de sortie: """ + """\n"""
                + str(affiche_poid_3) + """\n""" + """\n"""
                )

                T.insert(END, fact1 + fact2)
            
        def affichagePoids():
            fact1 = ("""NMSE minimale: """ + str(np.min(a)) + """\n""")
            fact2 = ("""les poids correspondant sont: """ + """\n""")
            affiche_2 = np.zeros((nombreUniteCache, nombreUniteEntre))
            affiche_3 = np.zeros((1, nombreUniteCache))
            for x in range(nombreUniteCache):
                for y in range(nombreUniteEntre):
                    affiche_2[x, y] = b[np.where(a == np.min(a))[0], x, y]
            for x in range(1):
                for y in range(nombreUniteCache):
                    affiche_3[x, y] = c[np.where(a == np.min(a))[0], x, y]
            
            fact3 = ("""les poids obtenus entre la couche d' entrée et la couche cachée: """ + 
            """\n""" + str(affiche_2) + """\n""" 
            + """les poids obtenus entre la couche cachée et la couche de sortie: """ + """\n"""
            + str(affiche_3) + """\n"""
            )

            T2.insert(END, fact1+fact2+fact3)

        bouton221 = tk.Button(self, text="Information sur l'architecture", command=affichage)
        bouton221.place(x=455, y=510)

        boutonPoid = tk.Button(self, text="POIDS", command=affichagePoids)
        boutonPoid.place(x=455, y=550)

        boutonCourbe = tk.Button(self, text="Courbe", command=courbe_nmse)
        boutonCourbe.place(x=455, y=590)

    
    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)

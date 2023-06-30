from tkinter import * 
import tkinter as tk
from tableauPrediction1PasEnAvant import*
from tableauPrediction3PasEnAvant import*
from tableauPrediction10PasEnAvant import*
from tableauPrediction20PasEnAvant import*
from courbePrediction1PasEnAvant import*
from courbePrediction3PasEnAvant import*
from courbePrediction10PasEnAvant import*
from courbePrediction20PasEnAvant import*

class App_prediction(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Prédiction")
        self.option_add("*header.font", "helvetica 18 bold")
        self.create_label(name="header", text="Prédiction: ")
        self.geometry("650x400")
        self.resizable(width=0, height=0)

        label_1 = tk.LabelFrame(self, text="prédiction à un pas en avant")
        label_3 = tk.LabelFrame(self, text="prédiction à trois pas en avant")
        label_10 = tk.LabelFrame(self, text="prédiction à dix pas en avant")
        label_20 = tk.LabelFrame(self, text="prédiction à vingt pas en avant")
        
        btnCourbe1 = tk.Button(self, text="Affiche courbe", command=courbe_pred_1)
        btnTab1 = tk.Button(self, text="Affiche Tab")

        btnCourbe3 = tk.Button(self, text="Affiche courbe", command=courbe_pred_3)
        btnTab3 = tk.Button(self, text="Affiche Tab")

        btnCourbe10 = tk.Button(self, text="Affiche courbe", command=courbe_pred_10)
        btnTab10 = tk.Button(self, text="Affiche Tab")

        btnCourbe20 = tk.Button(self, text="Affiche courbe", command=courbe_pred_20)
        btnTab20 = tk.Button(self, text="Affiche Tab")

        label_1.place(x=25, y=35, width=600, height=70)
        label_3.place(x=25, y=130, width=600, height=70)
        label_10.place(x=25, y=225, width=600, height=70)
        label_20.place(x=25, y=320, width=600, height=70)

        btnCourbe1.place(x=50, y=60)
        btnTab1.place(x=400, y=60)

        btnCourbe3.place(x=50, y=155)
        btnTab3.place(x=400, y=155 )

        btnCourbe10.place(x=50, y=250)
        btnTab10.place(x=400, y=250)

        btnCourbe20.place(x=50, y=345)
        btnTab20.place(x=400, y=345)

        btnTab1.bind("<Button>",
		lambda e: App_Table(self))

        btnTab3.bind("<Button>",
		lambda e: App_Table_3(self))

        btnTab10.bind("<Button>",
		lambda e: App_Table_10(self))

        btnTab20.bind("<Button>",
		lambda e: App_Table_20(self))
        

    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)
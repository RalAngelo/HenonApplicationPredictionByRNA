from LesPremieresValeurs import*
from tkinter import * 
import tkinter as tk
from PIL import Image, ImageTk

class App_win(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Les 500 premières valeurs")
        self.geometry("700x700")
        self.resizable(width=0, height=0)        
        
        label_formule = tk.LabelFrame(self, text = "APPLICATION DE HÉNON")
        label_valeur_canonique = tk.LabelFrame(self, text = "Valeurs de a et de b")
        label_valeur_X_n = tk.LabelFrame(self, text = "Valeurs des Xn")
        label_valeur_Y_n = tk.LabelFrame(self, text = "Valeurs des Yn")
                     
        l = Listbox(label_valeur_X_n)
        l.place(x=10, width = 305, height = 400)

        scroll=Scrollbar(label_valeur_X_n, command=l.yview)
        scroll.pack(side="right", fill="y")
        l.configure(yscrollcommand=scroll.set)

        l_y = Listbox(label_valeur_Y_n)
        l_y.place(x=10, width = 305, height = 400)

        scroll_y = Scrollbar(label_valeur_Y_n, command = l_y.yview)
        scroll_y.pack(side = "right", fill = "y")
        l_y.configure(yscrollcommand = scroll_y.set)
    
        label_formule.place(x = 13, y = 13, width = 330, height = 170)
        label_valeur_canonique.place(x = 358, y = 13, width = 330 , height = 170)
        
        label_valeur_X_n.place(x = 13, y = 250, width = 330, height = 430)
        label_valeur_Y_n.place(x = 358, y = 250, width = 330 , height = 430)
        
        btn_courbe = tk.Button(self, text = "Afficher la courbe", command = courbe)
        btn_courbe.place(x = 358, y = 200)
        
        def lister():
            l.insert(0, *liste_X_n)
            l_y.insert(0, *liste_Y_n)
        
        btn_500_valeurs = tk.Button(self, text = "Générer les 500 Premières valeurs", command = lister)
        btn_500_valeurs.place(x = 13, y = 200)

        monimage = Image.open("serie.png") 
        photo = ImageTk.PhotoImage(monimage)
        label = tk.Label(label_formule,image=photo)
        label.image = photo 
        label.place(x = 8, y = 0, width = 310, height = 146)

        monimage_2 = Image.open("valeurs.png") 
        photo_2 = ImageTk.PhotoImage(monimage_2)
        label_2 = tk.Label(label_valeur_canonique,image=photo_2)
        label_2.image = photo_2 
        label_2.place(x = 8, y = 0, width = 310, height = 146)  
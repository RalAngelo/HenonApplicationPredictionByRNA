import tkinter as tk
from Fen500PremiereValeurs import*
from FenPrediction import*

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fenêtre de gestion")
        self.option_add("*header.font", "helvetica 18 bold")
        btn_500_valeurs = tk.Button(self, text="Les 500 premières valeurs, et la courbe de Yn en fonction de Xn")
        btn_prediction = tk.Button(self, text="Les prédictions")

        self.create_label(name="header", text="PRÉDICTION DE LA SÉRIE DE HÉNON")

        opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}
        btn_500_valeurs.pack(**opts)
        btn_prediction.pack(**opts)

        btn_500_valeurs.bind("<Button>",
		lambda e: App_win(self))

        btn_prediction.bind("<Button>",
		lambda e: App_prediction(self))

    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)

if __name__ == "__main__":
    app = App()
    app.mainloop()
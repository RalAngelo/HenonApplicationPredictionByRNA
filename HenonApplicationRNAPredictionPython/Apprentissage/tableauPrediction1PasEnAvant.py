from tkinter import * 
import tkinter as tk
import numpy as np
from PredictionUnPasEnAvant import * 
from LesPremieresValeurs import*

class App_Table(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.geometry("1160x700")
        self.title("Tableau de la prédiction à un pas en avant")
        self.resizable(width=0, height=0)

        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        frame_main = tk.Frame(self)
        frame_main.grid(sticky='news')

        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = tk.Frame(frame_main)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        canvas = tk.Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        # Create a frame to contain the buttons
        frame_entry = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_entry, anchor='nw')

        title = ['N°', 'Prototypes', 'Valeurs attendues', 'Valeurs données par le réseau']
        lst = np.empty((30, 4), dtype=object)

        for i in range(30):
            for j in range(4):
                if j==0:
                    lst[i,j] = i
                    if i==0:
                        lst[i,j] = title[0] 
        
                if j==1:
                    lst[i,j] = " \"{0}\"; \"{1}\" ".format(predictionUnPasEnAvant()[1][i, 0], predictionUnPasEnAvant()[1][i, 1])
                    if i==0:
                        lst[i,j] = title[1]

                if j==2:
                    lst[i,j] = predictionUnPasEnAvant()[1][i + 1, 1]
                    if i==0:
                        lst[i,j] = title[2]

                if j==3:
                    lst[i,j] = predictionUnPasEnAvant()[0][i]
                    if i==0:
                        lst[i,j] = title[3]
        
        total_rows = len(lst)
        total_columns = len(lst[0])

        entry = [[tk.Button() for j in range(total_columns)] for i in range(total_rows)]

        #tableau
        for i in range(total_rows):
            for j in range(total_columns):
                if i>=0 and j==0:
                    if i==0:
                        self.e = tk.Entry(frame_entry, width=3, fg='blue', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                    else:
                        self.e = tk.Entry(frame_entry, width=3, fg='black', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                if i>=0 and j==1:
                    if i==0:
                        self.e = tk.Entry(frame_entry, width=43, fg='blue', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                    else:
                        self.e = tk.Entry(frame_entry, width=43, fg='black', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                if i>=0 and j==2:
                    if i==0:
                        self.e = tk.Entry(frame_entry, width=21, fg='blue', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                    else:
                        self.e = tk.Entry(frame_entry, width=21, fg='black', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                if i>=0 and j==3:
                    if i==0:
                        self.e = tk.Entry(frame_entry, width=26, fg='blue', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
                    else:
                        self.e = tk.Entry(frame_entry, width=26, fg='black', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j]) 

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        frame_entry.update_idletasks()

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = sum([entry[0][j].winfo_width() for j in range(0, total_columns)])
        first5rows_height = sum([entry[i][0].winfo_height() for i in range(0, total_columns)])
        frame_canvas.config(width=1157, height=700)

        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))